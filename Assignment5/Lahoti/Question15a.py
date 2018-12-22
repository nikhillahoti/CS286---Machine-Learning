import numpy as np

X = np.array([[3,3],
              [3,4],
              [2,3],
              [1,1],
              [1,3],
              [2,2]
])

z = np.array([1,1,1,-1,-1,-1])
C = 2.5

e = 0.00001
b = 0
lambd = np.zeros(len(X))
lambd_bar = np.zeros(len(X))
E = np.zeros(len(X))
b_arr = np.zeros(len(X))

def Func(XCurr):
    result = 0
    for i in range(len(X)):
        result += (lambd[i] * z[i] * np.dot(X[i],XCurr))
    return result + b

for iteration in range(10):
    for i in range(len(X)):
        for j in range(len(X)):
            if i == j: continue

            d = 2 * (np.dot(X[i], X[j])) - np.dot(X[i], X[i]) - np.dot(X[j], X[j])
            if abs(d) > e:
                E[i] = Func(X[i]) - z[i]
                E[j] = Func(X[j]) - z[j]
                lambd_bar[i] = lambd[i]
                lambd_bar[j] = lambd[j]
                lambd[j] = lambd[j] - (z[j] * ((E[i] - E[j]) / d))

                l = 0
                h = 0
                if z[i] == z[j]:
                    l = max(0, lambd[i] + lambd[j] - C)
                    h = min(C, lambd[i] + lambd[j])
                else:
                    l = max(0, lambd[j] - lambd[i])
                    h = min(C, C + lambd[j] - lambd[i])

                if lambd[j] > h:
                    lambd[j] = h
                else:
                    if lambd[j] < l:
                        lambd[j] = l

                lambd[i] = lambd[i] + z[i] * z[j] * (lambd_bar[j] - lambd[j])
                b_arr[i] = b - E[i] - z[i] * (lambd[i] - lambd_bar[i]) * np.dot(X[i], X[i]) - z[j] * (lambd[j] - lambd_bar[j]) * np.dot(X[i], X[j])
                b_arr[j] = b - E[j] - z[i] * (lambd[i] - lambd_bar[i]) * np.dot(X[i], X[j]) - z[j] * (lambd[j] - lambd_bar[j]) * np.dot(X[j], X[j])

                if lambd[i] > 0 and lambd[i] < C:
                    b = b_arr[i]
                elif lambd[j] > 0 and lambd[j] < C:
                    b = b_arr[j]
                else:
                    b = (b_arr[i] + b_arr[j]) / 2


print(lambd)
print(b)

for i in range(len(X)):
    print("F[" + str(i) + "] = " + str(Func(X[i])))
    print("z[" + str(i) + "] = " + str(z[i]))