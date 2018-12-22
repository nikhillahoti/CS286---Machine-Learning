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

meu = np.array([[2.5, 65], [3.5, 70]])
GMixModel = mixture.GaussianMixture(n_components=2)
GMixModel.means_init = meu
GMixModel.fit(oldFaithfulData)

print GMixModel.means_
y_pred = GMixModel.predict(oldFaithfulData)
print y_pred

x_red = []
y_red = []
x_blue = []
y_blue = []
for i in range(len(y_pred)):
    if y_pred[i] == 1:
        x_red.append(oldFaithfulData[i][0])
        y_red.append(oldFaithfulData[i][1])
    else:
        x_blue.append(oldFaithfulData[i][0])
        y_blue.append(oldFaithfulData[i][1])

plt.scatter(x_red, y_red, color='blue')
plt.scatter(x_blue, y_blue, color='red')
plt.show()