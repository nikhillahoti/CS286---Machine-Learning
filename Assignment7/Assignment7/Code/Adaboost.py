import math
import numpy as np


def createNumpyArray():
    X = np.zeros((30, 25))
    Z = np.zeros((25))
    content = None
    with open('InputFile.txt', 'r') as fInput:
        content = fInput.readlines()

    for i in range(len(content)):
        parts = content[i].strip().split(" ")
        Z[i] = int(parts[1])
        for j in range(2, len(parts)):
            X[j - 2][i] = int(parts[j])

    return X,Z


# C <- Number of classifiers
# Z <- length of each sequence
def AdaBoost(c,Z):

    C = np.zeros((len(X), len(Z)))
    w = np.zeros((len(Z)))
    k = []
    k.append([])
    u = np.zeros((len(c)))

    for m in range(1, len(c)):
        sum = 0
        for i in range(len(Z)):
            w[i] = math.exp(-1 * C[m-1][i] * Z[i])
            sum += w[i]

        W = sum
        W2 = math.inf

        for j in range(0, len(c)):
            if u[j] == 0:
                Y = 0
                for k1 in range(len(Z)):
                    if Z[k1] != c[j][k1]:
                        Y += w[k1]
                if Y < W2:
                    W2 = Y
                    t = j

        k.append(c[t])
        u[t] = 1
        rm = W2 / W
        alpham = (0.5) * math.log((1 - rm) / rm)

        for i in range(0, len(Z)):
            C[m][i] = C[m-1][i] + alpham * k[m][i]

    print(C[3])
    print(C[4])
    print(C[29])

X,Z = createNumpyArray()
print(len(X))
print(len(Z))
AdaBoost(X, Z)