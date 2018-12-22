import numpy as np

X1 = np.array([2, -1, 0, 1, 1, -3, 5, 2], dtype=float)
X2 = np.array([-2, 3, 2, 3, 0, 2, -1, 1], dtype=float)
X3 = np.array([-1, 3, 3, 1, -1, 4, 5, 2], dtype=float)
X4 = np.array([3, -1, 0, 3, 2, -1, 3, 0], dtype=float)

# Concatenating to get a combined matrix
M = np.array([X1, X2, X3, X4]).transpose()

meu = M.mean(axis=1)
#print(meu)

for i in range(M.shape[0]):
    M[i] -= meu[i]

C = np.cov(M)
#print(C)

eigenvalue, eigenvector = np.linalg.eig(C)
U = eigenvector[:,:3]

Delta  = np.dot(U.T,M)
print(Delta)
Delta = Delta.transpose()

# Part b: Scoring the samples

def getLowestDistance(result):
    lowest = float("infinity")
    for i in range(Delta.shape[0]):
        value = np.linalg.norm(Delta[i] - result)
        #print(value)
        if value < lowest:
            lowest = value
    return lowest

u1, u2, u3 = U.T


Y1 = np.array([1,5,1,5,5,1,1,3])
Y1 = Y1 - meu
#print(Y1)
res = np.array([Y1.dot(u1), Y1.dot(u2), Y1.dot(u3)], dtype=float)
print("\n\n For Y1 --> ")
print(res)
print("Minimum distance Y1: ", getLowestDistance(res))
print("----")

Y2 = np.array([-2,3,2,3,0,2, -1, 1])
Y2 = Y2 - meu
#print(Y2)
res = np.array([Y2.dot(u1), Y2.dot(u2), Y2.dot(u3)], dtype=float)
print("\n\n For Y2 --> ")
print(res)
print("Minimum distance Y2: ", getLowestDistance(res))
print("----")

Y3 = np.array([2,-3,2,3,0,0,2,-1])
Y3 = Y3 - meu
#print(Y3)
res = np.array([Y3.dot(u1), Y3.dot(u2), Y3.dot(u3)], dtype=float)
print("\n\n For Y3 --> ")
print(res)
print("Minimum distance Y3: ", getLowestDistance(res))
print("----")

Y4 = np.array([2,-1,2,2,-1,1,2,2])
Y4 = Y4 - meu
#print(Y4)
res = np.array([Y4.dot(u1), Y4.dot(u2), Y4.dot(u3)], dtype=float)
print("\n\n For Y4 --> ")
print(res)
print("Minimum distance Y4: ", getLowestDistance(res))
print("----")





