
import math as m

X0 = [0.6, 0.1, 0.8, 0.3, 0.7, 0.7, 0.2]
X1 = [0.4, 0.2, 0.6, 0.7, 0.3, 0.7, 0.9]
Z = [1, 0, 0, 1, 1, 0, 1]

w = [1, 2, -1, 1, -2, 1]
alpha = 0.1

v0 = w[0]
v1 = w[1]
v2 = w[2]
v3 = w[3]
v4 = w[4]
v5 = w[5]

epoch  = 1000

counter = 0
while counter < epoch:
    for i in range(6):
        v0 = w[0]
        v1 = w[1]
        v2 = w[2]
        v3 = w[3]
        v4 = w[4]
        v5 = w[5]

        v6 = X0[i] * v0 + X1[i] * v2
        v7 = X0[i] * v1 + X1[i] * v3
        v8 = 1 + m.exp(-v6)
        v9 = 1 + m.exp(-v7)
        v10 = v4 / v8
        v11 = v5 / v9
        v12 = (v10 + v11 - Z[i]) ** 2 / 2
        z = v12

        dz = 1
        dv11 = v10 + v11 - Z[i]
        dv10 = v10 + v11 - Z[i]
        dv9 = -v5 / (v9 ** 2) * dv11
        dv8 = -v4 / (v8 ** 2) * dv10
        dv7 = -m.exp(-v7) * dv9
        dv6 = -m.exp(-v6) * dv8
        dv5 = dv11 / v9
        dv4 = dv10 / v8
        dv3 = X1[i] * dv7
        dv2 = X1[i] * dv6
        dv1 = X0[i] * dv7
        dv0 = X0[i] * dv6

        w[0] -= alpha * dv0
        w[1] -= alpha * dv1
        w[2] -= alpha * dv2
        w[3] -= alpha * dv3
        w[4] -= alpha * dv4
        w[5] -= alpha * dv5

    counter += 1

print("\n Weights -> ")
print(w)

Z_predicted = []
for i in range(len(X0)):
    Y = (w[4] / (1 + m.exp(-(w[0] * X0[i] + w[2] * X1[i])))) + (w[5] / (1 + m.exp(-(w[1] * X0[i] + w[3] * X1[i]))))
    if Y > 0.5: Z_predicted.append(1)
    else: Z_predicted.append(0)

print("\n\n Predicted Value -->\n")
print(Z_predicted)

print("\n\n Expected Training Value -> \n")
print(Z)

count = 0
for i in range(len(Z_predicted)):
    if (Z_predicted[i] == Z[i]): count += 1

accu = count * 1.0 / len(Z_predicted) * 100
print("Accuracy -> %0.2f" % accu)

# Testing Set
X0_Test = [0.55, 0.32, 0.24, 0.86, 0.53, 0.46, 0.16, 0.52, 0.46, 0.96]
X1_Test = [0.11, 0.21, 0.64, 0.68, 0.79, 0.54, 0.51, 0.94, 0.87, 0.63]
Z_Test = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

Z_predicted = []
for i in range(len(X0_Test)):
    Y = (w[4] / (1 + m.exp(-(w[0] * X0_Test[i] + w[2] * X1_Test[i])))) + (w[5] / (1 + m.exp(-(w[1] * X0_Test[i] + w[3] * X1_Test[i]))))
    if Y > 0.5: Z_predicted.append(1)
    else: Z_predicted.append(0)

print("\n\n Predicted Value for Testing Set -> \n")
print(Z_predicted)

print("\n\n Predicted value for Training Set -> \n")
print(Z_Test)

count = 0
for i in range(len(Z_predicted)):
    if (Z_predicted[i] == Z_Test[i]): count += 1

accu = count * 1.0 / len(Z_predicted) * 100
print("Accuracy -> %0.2f" % accu)
