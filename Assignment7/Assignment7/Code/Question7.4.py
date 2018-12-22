import pandas as pd
from sklearn.ensemble import RandomForestClassifier

A = [1, 2, 3, 5, 10]
B = [3, 5, 7, 9, 10]
C = [1, 2, 6, 8, 10]

A_In = [[120,7],
     [120,7],
     [100,6],
     [100,6],
     [110,6],
     [120,4],
     [130,5],
     [140,5],
     [110,6],
     [120,7]
]
A_out = [1,1,1,1,1,0,0,0,0,0]
model1 = RandomForestClassifier()
model1.fit(A_In, A_out)

B_In = [[100,34],
        [100,35],
        [100,32],
        [100,32],
        [110,34],
        [140,26],
        [110,20],
        [140,28],
        [100,24],
        [120,25]
        ]
B_out = [1,1,1,1,1,0,0,0,0,0]

C_In = [[7,32],
        [7,28],
        [5,27],
        [6,33],
        [6,34],
        [4,22],
        [5,23],
        [7,20],
        [4,21],
        [7,25]
        ]
C_out = [1,1,1,1,1,0,0,0,0,0]

model2 = RandomForestClassifier()
model2.fit(B_In, B_out)

model3 = RandomForestClassifier()
model3.fit(C_In, C_out)

modelEvalA = [
    [100, 7],
    [130, 7],
    [115, 4],
    [105, 4],
    [140, 6]
]
predA = model1.predict(modelEvalA)


modelEvalB = [
    [100, 27],
    [130, 28],
    [115, 30],
    [105, 35],
    [140, 20]
]
predB = model2.predict(modelEvalB)

modelEvalC = [
    [7, 27],
    [7, 28],
    [4, 30],
    [4, 35],
    [6, 20]
]
predC = model3.predict(modelEvalC)

print(predA)
print(predB)
print(predC)

output = []
for i in range(len(predA)):
    count = 0
    if predA[i] == 1: count += 1
    if predB[i] == 1: count += 1
    if predC[i] == 1: count += 1
    if count > 1: output.append('Malware')
    else: output.append("Benign")

print output
