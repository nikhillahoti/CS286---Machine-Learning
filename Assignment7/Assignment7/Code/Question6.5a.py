import random as rand
import math
import matplotlib.pyplot as plt

def getClusters(X, c):
    C = []
    for i in range(len(c)):
        C.append([])

    # Assing the points to the nearest centroids
    for i in range(len(X)):
        closest = -1
        closestDist = 10000

        # Looping over all the centroids
        j = 0
        for j in range(K):
            distance = math.sqrt((X[i][0] - c[j][0]) ** 2 + (X[i][1] - c[j][1]) ** 2)
            if distance < closestDist:
                closestDist = distance
                closest = j
        C[closest].append(X[i])
    return C

def KMeans(X, K):
    C = []
    c = []

    # Pick k random centroids
    for i in range(K):
        dimension1 = rand.uniform(1.75, 4.8)
        dimension2 = rand.randint(47, 85)
        c.append([dimension1, dimension2])

    # Stopping condition
    for k in range(8):
        C = getClusters(X, c)
        # Getting new centroids
        c = []
        for i in range(len(C)):
            lst = C[i]
            dimension1 = 0
            dimension2 = 0
            for j in range(len(lst)):
                dimension1 += lst[j][0]
                dimension2 += lst[j][1]
            dimension1 /= len(lst)
            dimension2 /= len(lst)
            c.append([dimension1, dimension2])

    color = ['red', 'blue']
    for i in range(len(C)):
        x = []
        y = []
        lst = C[i]
        for j in range(len(lst)):
            x.append(lst[j][0])
            y.append(lst[j][1])
            plt.scatter(x, y, color=color[i])

    plt.show()






oldFaithfulData = [
    [3.6, 79],
    [1.8, 54],
    [2.283, 62],
    [3.333, 74],
    [2.883, 55],
    [4.533, 85],
    [1.950, 51],
    [1.833, 54],
    [4.7, 88],
    [3.6, 85],
    [1.600, 52],
    [4.350, 85],
    [3.917, 84],
    [4.2, 78],
    [1.750, 62],
    [1.8, 51],
    [4.7, 83],
    [2.167, 52],
    [4.800, 84],
    [1.750, 47],
]
K = 2
KMeans(oldFaithfulData, K)





