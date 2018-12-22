import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

def evaluateCoreOrBorder(X, epsilon, NNeighbor):

        global neighbor
        global dictCore

        dictCore = {}
        neighbor = []
        for i in range(len(X)): neighbor.append([])

        #epsilon = epsilon ** 2
        for i in range(0, len(X)):
            nCount = 0
            for j in range(i + 1, len(X)):
                dist = ((X[i][0] - X[j][0]) ** 2) + ((X[i][1] - X[j][1]) ** 2)
                dist = math.sqrt(dist)
                if dist <= epsilon:
                    nCount += 1
                    neighbor[i].append(j)
                    neighbor[j].append(i)

            # check if the point is a Core point
            if nCount >= NNeighbor:
                # It is a core point
                dictCore[i] = True

        #print neighbor
        #print dictCore
        #print len(dictCore)

def getMyNeighbor(point, clusterIndex):
    global dictCore
    global neighbor
    global Clusters
    global X
    global visited

    itsneighbor = neighbor[point]
    for i in range(len(itsneighbor)):
        # check if it is already visited
        if visited[itsneighbor[i]]: continue

        # set as visited
        visited[itsneighbor[i]] = True

        # add it to the current cluster
        Clusters[clusterIndex].append(itsneighbor[i])

        if itsneighbor[i] in dictCore:
             # it is a core point
             getMyNeighbor(itsneighbor[i], clusterIndex)

def DBScan():
    global dictCore
    global neighbor
    global Clusters
    global X
    global visited

    visited = []
    for i in range(len(X)):
        visited.append(False)

    clusterIndex = 0
    for key in dictCore:
        if visited[key]: continue

        Clusters.append([])
        # set as visited
        visited[key] = True
        getMyNeighbor(key, clusterIndex)

        clusterIndex += 1

X = [   [1.0,5.0],
        [1.25,5.35],
        [1.25,5.75],
        [1.5,6.25],
        [1.75,6.75],
        [2.0,6.5],
        [3.0,7.75],
        [3.5,8.25],
        [3.75,8.75],
        [3.95,9.1],
        [4.0,8.5],
        [2.5,7.25],
        [2.25,7.75],
        [2.0,6.5],
        [2.75,8.25],
        [4.5,8.9],
        [9.0,5.0],
        [8.75,5.85],
        [9.0,6.25],
        [8.0,7.0],
        [8.5,6.25],
        [8.5,6.75],
        [8.25,7.65],
        [7.0,8.25],
        [6.0,8.75],
        [5.5,8.25],
        [5.25,8.75],
        [4.9,8.75],
        [5.0,8.5],
        [7.5,7.75],
        [7.75,8.25],
        [6.75,8.0],
        [6.25,8.25],
        [4.5,8.9],
        [5.0,1.0],
        [1.25,4.65],
        [1.25,4.25],
        [1.5,3.75],
        [1.75,3.25],
        [2.0,3.5],
        [3.0,2.25],
        [3.5,1.75],
        [3.75,8.75],
        [3.95,0.9],
        [4.0,1.5],
        [2.5,2.75],
        [2.25,2.25],
        [2.0,3.5],
        [2.75,1.75],
        [4.5,1.1],
        [5.0,9.0],
        [8.75,5.15],
        [8.0,2.25],
        [8.25,3.0],
        [8.5,4.75],
        [8.5,4.25],
        [8.25,3.35],
        [7.0,1.75],
        [8.0,3.5],
        [6.0,1.25],
        [5.5,1.75],
        [5.25,1.25],
        [4.9,1.25],
        [5.0,1.5],
        [7.5,2.25],
        [7.75,2.75],
        [6.75,2.0],
        [6.25,1.75],
        [4.5,1.1],
        [3.0,4.5],
        [7.0,4.5],
        [5.0,3.0],
        [4.0,3.35],
        [6.0,3.35],
        [4.25,3.25],
        [5.75,3.25],
        [3.5,3.75],
        [6.5,3.75],
        [3.25,4.0],
        [6.75,4.0],
        [3.75,3.55],
        [6.25,3.55],
        [4.75,3.05],
        [5.25,3.05],
        [4.5,3.15],
        [5.5,3.15],
        [4.0,6.5],
        [4.0,6.75],
        [4.0,6.25],
        [3.75,6.5],
        [4.25,6.5],
        [4.25,6.75],
        [3.75,6.25],
        [6.0,6.5],
        [6.0,6.75],
        [6.0,6.25],
        [5.75,6.75],
        [5.75,6.25],
        [6.25,6.75],
        [6.25,6.25],
        [9.5,9.5],
        [2.5,9.5],
        [1.0,8.0]]
dictCore = {}
neighbor = []
Clusters = []
visited = []
epsilon = 2
m = 10

evaluateCoreOrBorder(X, epsilon, m)
DBScan()

#print(Clusters)
print("Number of Clusters: " + str(len(Clusters)))
colors = ['red','blue', 'black', 'cyan', 'pink', 'orange', 'violet', 'yellow', 'darkgreen', 'grey', 'darkblue', 'darkgreen', 'purple']

sum = 0
for i in range(len(Clusters)):
    x = []
    y = []
    currentCluster = Clusters[i]

    print("Elements in Cluster " + str(i) + " -> " +  str(len(currentCluster)))
    sum += len(currentCluster)

    for j in range(len(currentCluster)):
        x.append(X[currentCluster[j]][0])
        y.append(X[currentCluster[j]][1])

    plt.scatter(x,y,color=colors[i])

print("Number of Outliers --> " + str(len(X) - sum))
plt.show()




#print(len(X))