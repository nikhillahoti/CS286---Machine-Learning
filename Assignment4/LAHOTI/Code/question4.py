
import numpy as np

A = np.array([[1,2], [3, 1],[2, 3]], dtype=float)
C = A.dot(A.transpose()) / 2
print(C)

eigenV, eigenVec = np.linalg.eig(C)
print("\n\n\n Eigen Vectors ---> ")
print(eigenVec[:, 0])
print(eigenVec[:, 2])
#print(eigenV)

print("\n\n\n Eigen Values ---> ")
print(eigenV[0])
print(eigenV[2])


print("\n\n\n Verification part --->")
print(C.dot(eigenVec[:, 0]))
print(eigenVec[:, 0] * eigenV[0])
print("----")
print("----")
print(C.dot(eigenVec[:, 2]))
print(eigenVec[:, 2] * eigenV[2])