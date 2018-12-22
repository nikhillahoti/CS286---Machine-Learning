import numpy as np

B1 = np.array([-1, 2, 1, 2, -1, 0], dtype=float)
B2 = np.array([-2, 1, 2, 3,  2, 1], dtype=float)
B3 = np.array([-1, 3, 0, 1, 3, -1], dtype=float)
B4 = np.array([0, 2, 3, 1, 1, -2], dtype=float)

# Concatenating to get a combined matrix
B = np.array([B1, B2, B3, B4]).transpose()

meu = B.mean(axis=1)
#print(meu)

for i in range(B.shape[0]):
    B[i] -= meu[i]

C = np.cov(B)
#print(C)

eigenvalue, eigenvector = np.linalg.eig(C)
U = eigenvector[:,:3]

InverseDelta  = np.dot(U.T,B)
print(InverseDelta)