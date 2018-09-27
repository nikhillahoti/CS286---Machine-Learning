
S = {}
def initializeS():
    S["EE"] = 9
    S["GG"] = 9
    S["CC"] = 10
    S["JJ"] = 10
    S["EG"] = S["GE"] = -4
    S["EC"] = S["CE"] = 2
    S["EJ"] = S["JE"] = 2
    S["GC"] = S["CG"] = -5
    S["GJ"] = S["JG"] = -5
    S["CJ"] = S["JC"] = 7

def getMatchValue(str1, str2, penalty):

    initializeS()
    alignmentScores =  [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    # Initialize the first column to the degree of gap create
    for i in range(1, len(alignmentScores[0])):
        alignmentScores[0][i] = i * penalty

    # Initialize the first row to the degree of gap create
    for i in range(1, len(alignmentScores)):
        alignmentScores[i][0] = i * penalty

    for i in range(1, len(alignmentScores)):
        for j in range(1, len(alignmentScores[0])):
            alignmentScores[i][j] = max(
                alignmentScores[i-1][j-1] + S[str1[i-1] + str2[j-1] + ""] ,
                alignmentScores[i-1][j] + penalty,
                alignmentScores[i][j-1] + penalty
            )

    """
    for i in range(len(alignmentScores)):
        print(alignmentScores[i])
    """

    return alignmentScores[len(alignmentScores) - 1][len(alignmentScores[0]) - 1]

lst = []
lst.append("EJG")
lst.append("GEECG")
lst.append("CGJEE")
lst.append("JJGECCG")

alignmentScores = [[0 for x in range(len(lst))] for y in range(len(lst))]
penalty = -3
for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        alignmentScores[j][i] = alignmentScores[i][j] = getMatchValue(lst[i], lst[j], penalty)

for i in range(len(alignmentScores)):
    print(alignmentScores[i])


