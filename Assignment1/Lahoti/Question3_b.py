
# Package imports
import numpy as np

# generate all permutations of patterns for the ring sizes (4 in this case. Please update length below for different size)
def generatePatterns(currentPattern):
    if len(currentPattern) == length:
        return ForwardAlgorithm(currentPattern)
    prob = 0
    for i in range(len(observations)):
        prob += generatePatterns(currentPattern + [i])
    return prob

def ForwardAlgorithm(currentPattern):

    alpha = np.zeros(shape=(len(A)))

    # Initializing the result from the pi matrix
    for i in range(len(A)):
        alpha[i] = pi[i] * B[i][currentPattern[0]]

    for i in range(1, len(currentPattern)):
        interm = np.zeros(shape=(len(A)))

        # Loop for States
        for j in range(len(A)):
            temp = 0.0

            # Loop for Alpha. Alpha is where intermediate results are stored
            # Alpha is over-ridden after each iteration as there is no need for previous alpha state (except one step back)
            # in future value calculation
            for k in range(len(A)):
                temp += (alpha[k] * A[k][j])
            interm[j] = round(temp, 5) * B[j][currentPattern[i]]

        # Reassigning the intermediate result list to alpha
        alpha = interm

    # return the sum over the first row, which has N columns.
    return alpha.sum(axis=0)


length = 4

# all unique observations. Our M.
observations = [0, 1, 2]

pi = [0.6, 0.4]
#pi = [0.0, 1.0]

A = [[0.7, 0.3],
     [0.4, 0.6]
]

B = [[0.1, 0.4, 0.5],
     [0.7, 0.2, 0.1]
]

lst = [1, 0, 2]
prob = generatePatterns([])
print("Final Prob ---> " + str(round(prob, 5)))


