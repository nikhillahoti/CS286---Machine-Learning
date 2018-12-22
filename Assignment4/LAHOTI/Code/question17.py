import numpy as np

u1 = np.array([0.1614, 0.6278, -0.2604, -0.5389, 0.4637, 0.0752], dtype=float)
u2 = np.array([0.2443, 0.1070, -0.8017, 0.4277, -0.1373, -0.2904], dtype=float)
u3 = np.array([-0.0710, 0.2934, 0.3952, 0.3439, 0.3644, -0.7083], dtype=float)

#print(u1)
#print(u2)
#print(u3)

lambda1 = 4.0833
lambda2 = 1.2364
lambda3 = 0.7428

CLV1 = lambda1 * u1
CLV2 = lambda2 * u2
CLV3 = lambda3 * u3

print("Component Loading Vector --> ")
print("CLV1: ", CLV1)
print("CLV2: ", CLV2)
print("CLV3: ", CLV3)

print("\n\n The relative importance of each features -> ")
print(CLV1 + CLV2)