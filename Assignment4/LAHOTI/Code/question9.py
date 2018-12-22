import numpy as np

A = np.array([[0.25,0.25,-0.75,0.25],
              [-0.75,1.25,-1.75,1.25],
              [-1.25,-0.25,1.75,-0.25],
              [1,0,1,-2],
              [-1,1,-1,1],
              [0,-1,0,1]]
        ,dtype=float)

C = A.dot(A.transpose()) / 4
print(C)

variance = 0
for i in range(C.shape[0]):
    variance += C[i][i]
print(variance)