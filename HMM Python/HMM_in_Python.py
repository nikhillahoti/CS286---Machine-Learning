import random
import numpy as np
import math
import time

class EnglishTextModel:
    A = []
    B = []
    iniProb = []
    N = 27
    M = 27
    threshold = 0

    def __init__(self, T, threshold = 0.005, minIterations = 100):
        self.T = T
        self.minimumIters = minIterations
        self.threshold = threshold


    def initialize(self):
        # Initializing the Initial Probability Matrix
        self.iniProb = np.ones(shape=(self.N))
        sum = 0
        for i in range(self.N - 1):
            val = (1 / self.N)
            # Randomizing the Initial Probabilities
            val += ((random.randint(-9, 9) * val) / 100)
            val = round(val, 5)
            sum += val
            self.iniProb[i] = val
        self.iniProb[self.N-1] -= sum

        # Initializing the A - Transition Matrix
        self.A = np.ones(shape=(self.N, self.N))
        for i in range(self.N):
            sum = 0
            for j in range(self.N - 1):
                val = 1 / self.N
                val += ((random.randint(-9, 9) * val) / 100)
                sum += val
                self.A[i][j] = val
            self.A[i][self.N-1] -= sum

        # Initializing the B - Observation Matrix
        self.B = np.ones(shape=(self.N, self.M))
        for i in range(self.N):
            sum = 0
            for j in range(self.M - 1):
                val = 1 / self.M
                val += ((random.randint(-9, 9) * val) / 100)
                val = round(val, 5)
                sum += val
                self.B[i][j] = val
            self.B[i][self.M-1] -= round(sum, 5)

        # Checking for row stochastic properties
        #print("\n --- Row Stochastic Properties ---")
        #print(self.B.sum(axis=1))

    def Train(self):

        # Initialize the parameters
        self.initialize()

        iters = 0
        prevLog = 0

        start = time.time()
        while True:

            # The Alpha pass
            c = np.zeros(shape=len(self.T))
            alpha = np.zeros(shape=(self.N, len(self.T)))
            for i in range(self.N):
                alpha[i][0] = self.iniProb[i] * self.B[i][ord(self.T[0]) - 97]
                c[0] += alpha[i][0]

            c[0] = 1 / c[0]

            # Scaling the alpha
            for i in range(self.N):
                alpha[i][0] *= c[0]

            # Computing alpha-t
            for t in range(1, len(self.T)):
                c[t] = 0
                for i in range(self.N):
                    alpha[i][t] = 0
                    for j in range(self.N):
                        alpha[i][t] += (alpha[j][t - 1] * self.A[j][i])

                    if ord(self.T[t]) == 32:
                        # Space is at index 26
                        alpha[i][t] *= self.B[i][26]
                    else:
                        # Normal Character are fron 0 - 25
                        alpha[i][t] *= self.B[i][ord(self.T[t]) - 97]
                    c[t] += alpha[i][t]

                c[t] = 1 / c[t]
                for i in range(self.N):
                    alpha[i][t] *= c[t]
            #print(alpha)

            # The Beta pass
            beta = np.zeros(shape=(self.N, len(self.T)))
            for i in range(self.N):
                beta[i][len(self.T) - 1] = c[len(self.T) - 1]

            for t in range(len(self.T) - 2, -1, -1):
                for i in range(self.N):
                    beta[i][t] = 0
                    for j in range(self.N):
                        if ord(self.T[t+1]) == 32:
                            # Space is found
                            beta[i][t] += (self.A[i][j] * self.B[j][26] * beta[j][t+1])
                        else:
                            # Other characters
                            beta[i][t] += (self.A[i][j] * self.B[j][ord(self.T[t+1]) - 97] * beta[j][t + 1])
                    beta[i][t] *= c[t]
            #print(beta)


            # Compute the Gammas and Di-Gammas
            gammas = np.zeros(shape=(self.N, len(self.T)))
            diGammas = np.zeros(shape=(self.N, self.N, len(self.T)))
            for t in range(len(self.T) - 1):
                denom = 0
                for i in range(self.N):
                    for j in range(self.N):
                        if ord(self.T[t+1]) == 32:
                            # Space is found
                            denom += (alpha[i][t] * self.A[i][j] * self.B[j][26] * beta[j][t+1])
                        else:
                            # Character is found
                            denom += (alpha[i][t] * self.A[i][j] * self.B[j][ord(self.T[t+1]) - 97] * beta[j][t + 1])

                for i in range(self.N):
                    gammas[i][t] = 0
                    for j in range(self.N):
                        if ord(self.T[t+1]) == 32:
                            # Space is found
                            diGammas[i][j][t] = (alpha[i][t] * self.A[i][j] * self.B[j][26] * beta[j][t + 1]) / denom
                        else:
                            # Character is found
                            diGammas[i][j][t] = (alpha[i][t] * self.A[i][j] * self.B[j][ord(self.T[t+1]) - 97] * beta[j][t + 1]) / denom
                        gammas[i][t] += diGammas[i][j][t]


            # Special Case for Gamma of T - 1
            denom = 0
            for i in range(self.N):
                denom += alpha[i][len(self.T) - 1]

            for i in range(self.N):
                gammas[i][len(self.T) - 1] = alpha[i][len(self.T) - 1] / denom


            # --- Re-Estimation Step ---

            # Re-estimating Initial Probabilities
            sum = 0
            for i in range(self.N - 1):
                self.iniProb[i] = gammas[i][0]
                sum += gammas[i][0]
            self.iniProb[self.N - 1] = 1 - sum

            #print(" --- The Initial Matrix ---")
            #print(self.iniProb.sum(axis=0))

            # Re-estimating A - Transition Probability Matrix
            for i in range(self.N):
                for j in range(self.N):
                    numer = 0
                    denom = 0
                    for t in range(len(self.T) - 1):
                        numer += diGammas[i][j][t]
                        denom += gammas[i][t]
                    self.A[i][j] = numer / denom

            #print(" --- The Transition Matrix ---")
            #print(self.A.sum(axis=1))

            # Re-estimating the Observation Probability Matrix
            for i in range(self.N):
                for j in range(27):
                    numer = 0
                    denom = 0
                    for t in range(len(self.T)):
                        if ord(self.T[t]) == 32 and j == 26:
                            numer += gammas[i][t]
                        else:
                            if (ord(self.T[t]) - 97) == j:
                                numer += gammas[i][t]
                        denom += gammas[i][t]
                    self.B[i][j] = (numer / denom)

            # Handling the Row Stochastic Case
            """for i in range(self.N):
                diff = 1 - self.B.sum(axis=1)[i]
                perItem = diff / 27
                sum = 0
                for j in range(26):
                    self.B[i][j] += perItem
                    sum += perItem
                self.B[i][26] += diff - sum
            """

            #print(" --- The Observation Matrix ---")
            #print(self.B.sum(axis=1))

            # Computing Log Prob
            logProb = 0
            for i in range(len(self.T)):
                logProb += math.log10(c[i])

            logProb = -logProb
            iters += 1

            print("\n --- End of Iteration " + str(iters) + " ---")
            print(" Improvement " + str(logProb - prevLog))
            print(" Log Prob --> " + str(logProb))
            print("--------------")

            if iters > self.minimumIters:
                # Checking for change in Progess
                if logProb - prevLog < self.threshold:
                    end = time.time()
                    print("Total Training Time --> ")
                    print(end - start)
                    return self.iniProb, self.A, self.B
            prevLog = logProb

oSeq = "winston is one of the most laidback people i know he is tall and slim with black hair and he always wears a tshirt and black jeans"\
 "his jeans have holes in them and his baseball boots are scruffy too he usually sits at the back of the class and he often seems to be asleep however\
  when the exam results are given out he always gets an a i dont think hes as lazy as he appears to be need some text for padding this text"\

miniterations = 100
m = EnglishTextModel(T = oSeq, minIterations=miniterations)
pi, A, B = m.Train()
print("\nInitial Matrix")
print(pi)
print("\n Checking Row Stochastic Properties for Initial Matrix (Pi) : ")
print(pi.sum(axis=0))

print("\nTransition Matrix")
print(A)
print("\n Checking Row Stochastic Properties for Matrix A : ")
print(A.sum(axis=1))

print("\nObservation Matrix")
print(B.transpose())
print("\n Checking Row Stochastic Properties for Matrix B : ")
print(B.sum(axis=1))





