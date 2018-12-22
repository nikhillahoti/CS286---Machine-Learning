import numpy as np

M1 = np.array([1, -1, 1, -1, -1, 1], dtype=float)
M2 = np.array([-2, 2, 2, -1,  -2, 2], dtype=float)
M3 = np.array([1, 3, 0, 1, 3, 1], dtype=float)
M4 = np.array([2, 3, 1, 1, -2, 0], dtype=float)

# Concatenating to get a combined matrix
M = np.array([M1, M2, M3, M4]).transpose()

meu_M = M.mean(axis=1)
#print(meu_M)

for i in range(M.shape[0]):
    M[i] -= meu_M[i]

C_M = np.cov(M)
#print(C_M)

eigenvalue, eigenvector = np.linalg.eig(C_M)
U_M = eigenvector[:,:3]

Delta  = np.dot(U_M.T,M).transpose()
print(Delta)


B1 = np.array([-1, 2, 1, 2, -1, 0], dtype=float)
B2 = np.array([-2, 1, 2, 3,  2, 1], dtype=float)
B3 = np.array([-1, 3, 0, 1, 3, -1], dtype=float)
B4 = np.array([0, 2, 3, 1, 1, -2], dtype=float)

# Concatenating to get a combined matrix
B = np.array([B1, B2, B3, B4]).transpose()

meu_B = B.mean(axis=1)
#print(meu_B)

for i in range(B.shape[0]):
    B[i] -= meu_B[i]

C_B = np.cov(B)
#print(C_B)

eigenvalue, eigenvector = np.linalg.eig(C_B)
U_B = eigenvector[:,:3]

InverseDelta  = np.dot(U_B.T,B).transpose()
print(InverseDelta)

def getLowestDistance(result, Det):
    lowest = float("infinity")
    for i in range(Det.shape[0]):
        value = np.linalg.norm(Det[i] - result)
        #print(value)
        if value < lowest:
            lowest = value
    return lowest

u1_M, u2_M, u3_M = U_M.T
u1_B, u2_B, u3_B = U_B.T


# Scoring Y1
Y1 = np.array([1, 5, 1, 5, 5, 1])

Y_in_M = Y1 - meu_M
res = np.array([Y_in_M.dot(u1_M), Y_in_M.dot(u2_M), Y_in_M.dot(u3_M)], dtype=float)

Y_in_B = Y1 - meu_B
res1 = np.array([Y_in_B.dot(u1_B), Y_in_B.dot(u2_B), Y_in_B.dot(u3_B)], dtype=float)

print("\n\n For Y1 --> ")
if getLowestDistance(res, Delta) < getLowestDistance(res1, InverseDelta):
    print(" Y1 is Malware")
else:
    print(" Y1 is Benign!")
print("----")


# Scoring Y2
Y2 = np.array([-2, 3, 2, 3, 0, 2])

Y_in_M = Y2 - meu_M
res = np.array([Y_in_M.dot(u1_M), Y_in_M.dot(u2_M), Y_in_M.dot(u3_M)], dtype=float)

Y_in_B = Y2 - meu_B
res1 = np.array([Y_in_B.dot(u1_B), Y_in_B.dot(u2_B), Y_in_B.dot(u3_B)], dtype=float)

#print(getLowestDistance(res, Delta))
#print(getLowestDistance(res1, InverseDelta))

print("\n\n For Y2 --> ")
if getLowestDistance(res, Delta) < getLowestDistance(res1, InverseDelta):
    print(" Y2 is Malware")
else:
    print(" Y2 is Benign!")
print("----")


# Scoring Y3
Y3 = np.array([2, -3, 2, 3, 0, 0])

Y_in_M = Y3 - meu_M
res = np.array([Y_in_M.dot(u1_M), Y_in_M.dot(u2_M), Y_in_M.dot(u3_M)], dtype=float)

Y_in_B = Y3 - meu_B
res1 = np.array([Y_in_B.dot(u1_B), Y_in_B.dot(u2_B), Y_in_B.dot(u3_B)], dtype=float)

print("\n\n For Y3 --> ")

if getLowestDistance(res, Delta) < getLowestDistance(res1, InverseDelta):
    print(" Y3 is Malware")
else:
    print(" Y3 is Benign!")
print("----")


# Scoring Y3
Y4 = np.array([2, -2, 2, 2, -1, 1])

Y_in_M = Y4 - meu_M
res = np.array([Y_in_M.dot(u1_M), Y_in_M.dot(u2_M), Y_in_M.dot(u3_M)], dtype=float)

Y_in_B = Y4 - meu_B
res1 = np.array([Y_in_B.dot(u1_B), Y_in_B.dot(u2_B), Y_in_B.dot(u3_B)], dtype=float)

print("\n\n For Y4 --> ")
if getLowestDistance(res, Delta) < getLowestDistance(res1, InverseDelta):
    print(" Y4 is Malware")
else:
    print(" Y4 is Benign!")
print("----")






