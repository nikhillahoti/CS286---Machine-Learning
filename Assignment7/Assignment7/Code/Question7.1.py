
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

X_red = [
    [0.5, 3.0],
    [1, 4.25],
    [1.5, 2],
    [2, 2.75],
    [2.5, 1.65],
    [3, 2.7],
    [3.5, 1],
    [4, 2.5],
    [4.5, 2.1],
    [5, 2.75]
]
Y_red = [1,1,1,1,1,1,1,1,1,1]

X_blue = [
    [0.5, 1.75],
    [1.5, 1.5],
    [2.5, 4],
    [2.5, 2.1],
    [3, 1.5],
    [3.5, 1.85],
    [4, 3.5],
    [5, 1.45]
]
Y_blue = [0,0,0,0,0,0,0,0]

X = np.array(X_red + X_blue)
Y = np.array(Y_red + Y_blue)

n_neighbors = 3


# Create color maps
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

h = .02  # step size in the mesh
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X, Y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("(k = %i, '%s')"
          % (n_neighbors, 'Decision Boundary'))

plt.show()
