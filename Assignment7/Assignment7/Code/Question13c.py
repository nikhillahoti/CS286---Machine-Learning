from sklearn import mixture
import numpy as np
import matplotlib.pyplot as plt

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

meu = np.array([[2, 90], [1.5, 10], [3.4, 50]])
GMixModel = mixture.GaussianMixture(n_components=3)
GMixModel.means_init = meu
GMixModel.fit(oldFaithfulData)

print GMixModel.means_
y_pred = GMixModel.predict(oldFaithfulData)
print y_pred

x = []
y = []
for i in range(3):
    x.append([])
    y.append([])

for i in range(len(y_pred)):
    x[y_pred[i]].append(oldFaithfulData[i][0])
    y[y_pred[i]].append(oldFaithfulData[i][1])

colors = ['red', 'blue', 'green']
for i in range(len(x)):
    plt.scatter(x[i], y[i], color=colors[i])
plt.show()