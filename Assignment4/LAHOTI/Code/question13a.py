import numpy as np

# Means of each row
mew = np.array([1.75,1.75,1.25,2,2,1] ,dtype=float)
#print(mew)

# Delta Values
Delta = np.array([[-1.1069, 1.2794, -2.6800, 2.5076]
                  ,[1.5480, 0.5484, -1.2085, -0.8879]])
Delta = Delta.transpose()
#print(Delta)

u1 = np.array([0.1641,0.6278,-0.2604,-0.5389,0.4637,0.0752], dtype=float)
#print(u1)
u2 = np.array([0.2443,0.1070,-0.8017,0.4277,-0.1373,-0.2904], dtype=float)
#print(u2)

# Testing Samples

def getLowestDistance(result):
    lowest = float("infinity")
    for i in range(Delta.shape[0]):
        value = np.linalg.norm(Delta[i] - result)
        #print(value)
        if value < lowest:
            lowest = value
    return lowest

Y1 = np.array([1, -1, 1, -1, -1, 1], dtype=float)
Y2 = np.array([-2, 2, 2, -1, -2, 2], dtype=float)
Y3 = np.array([1, 3, 0, 1, 3, 1], dtype=float)
Y4 = np.array([2, 3, 1, 1, -2, 0], dtype=float)

#print(Y1)
Y1 = Y1 - mew
#print(Y1)
res = np.array([Y1.dot(u1), Y1.dot(u2)], dtype=float)
print(res)
print("Minimum distance Y1: ", getLowestDistance(res))

# for Y2
Y2 = Y2 - mew
res = np.array([Y2.dot(u1), Y2.dot(u2)], dtype=float)
print(res)
print("Minimum distance Y2: ", getLowestDistance(res))

# for Y3
Y3 = Y3 - mew
res = np.array([Y3.dot(u1), Y3.dot(u2)], dtype=float)
print(res)
print("Minimum distance Y3: ", getLowestDistance(res))

# for Y4
Y4 = Y4 - mew
res = np.array([Y4.dot(u1), Y4.dot(u2)], dtype=float)
print(res)
print("Minimum distance Y4: ", getLowestDistance(res))


