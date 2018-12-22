
import math
import numpy as np


def createNumpyArray():
    X = np.zeros((30, 25))
    Z = np.zeros((25))
    content = None
    with open('InputFile.txt', 'r', encoding='utf-8') as fInput:
        content = fInput.readlines()

    for i in range(len(content)):
        parts = content[i].strip().split(" ")
        Z[i] = int(parts[1])
        for j in range(2, len(parts)):
            X[j - 2][i] = int(parts[j])

    return X,Z

def AdaBoost(c,Z):
    samples = len(Z) + 1
    C = np.zeros((samples, len(c)))
    u = np.zeros((samples))   # Visited or not
    w = np.zeros((samples))
    k = []
    r = np.zeros((len(c)))
    alpha = np.zeros((samples))
    t = 0

    for m in range(1, samples):
        sum = 0
        for i in range(samples):
            temp = -(Z[i-1] * C[m-1][i])
            w[i] = math.exp(temp)
            sum += w[i]

        W = sum
        W2 = math.inf

        for j in range(0, samples):
            if u[j] == 0:
                Y = 0
                for i in range(samples):
                    print("Here")
                    if Z[i] != c[j][i]:
                        Y += w[i]
                if Y < W2:
                    W2 = Y
                    t = j

        k.append(c[t])
        u[t] = 1
        print(W2)
        print(W)
        print("---")
        r[m] = W2 / W

        alpha[m] = 0
        if not np.isinf(r[m]):
            alpha[m] = 0.5 * (math.log(int((1 - r[m]) / r[m])))

        for i in range(len(Z)):
            C[m][i] = C[m][i] + alpha[m] * k[m-1][i]

    print(C[15])


X,Z = createNumpyArray()
print(len(X))
print(len(Z))
AdaBoost(X, Z)
