
import pandas as pd
p = pd.read_csv("malwareBenignScores.csv")

# Splitting the dataframe into two parts
X = p[['HMM', 'SSD', 'OGS']]
Y = p[['SCORE']]

X_train = X[:41]
Y_train = Y[:41]
X_test = X[41:]
Y_test = Y[41:]

from sklearn import svm
svc = svm.SVC(kernel='linear')
svc.fit(X_train, Y_train.values.ravel())

Y_test_Pred = svc.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test_Pred, Y_test)
print("With all 3 features")
print(acc)

print("Respective Weights of HMM, SSD, OGS")
print(svc.coef_)

X = p[['SSD', 'OGS']]
X_train = X[:41]
Y_train = Y[:41]
X_test = X[41:]
Y_test = Y[41:]

svc = svm.SVC(kernel='linear')
svc.fit(X_train, Y_train.values.ravel())

Y_test_Pred = svc.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test_Pred, Y_test)
print("Accuracy after removing the HMM feature -> ")
print(acc)

print("Respective Weights of SSD, OGS")
print(svc.coef_)

X = p[['SSD']]
X_train = X[:41]
Y_train = Y[:41]
X_test = X[41:]
Y_test = Y[41:]

svc = svm.SVC(kernel='linear')
svc.fit(X_train, Y_train.values.ravel())

Y_test_Pred = svc.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test_Pred, Y_test)
print("Accuracy after removing the HMM and OGS feature -> ")
print(acc)
print("Weight of SSD")
print(svc.coef_)


# I brainstormed on this problem with Ashraf Saber, Parth Jain and Sushmit Gaikwad
# No code was being shared or copied. Just Brainstorming.