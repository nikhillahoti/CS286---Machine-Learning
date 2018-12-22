# Package imports
import time

# Calculating probability for a given sequence
def calculateProbforSequence(seq, pattern):
    prob = pi[seq[0]] * B[seq[0]][pattern[0]]
    for i in range(1, len(seq)):
        prob *= (A[seq[i-1]][seq[i]] * B[seq[i]][pattern[i]])
    return prob

# Generating all permutation of sequences like [HHHH, HHHC, ..., CCCC]
def generateSequence(currentSequence, currentPattern):
    if len(currentSequence) == length:
        return calculateProbforSequence(currentSequence, currentPattern)
    prob = 0
    for i in range(2):
        prob += generateSequence(currentSequence + [i], currentPattern)
    return prob

# Generating all permutation of Patterns like [S, S, S, S] to [L, L, L, L]
def generatePatterns(currentPattern):
    if len(currentPattern) == length:
        return generateSequence([], currentPattern)
    prob = 0
    for i in range(len(observations)):
        prob += generatePatterns(currentPattern + [i])
    return prob


length = 4
observations = [0, 1, 2]

pi = [0.6, 0.4]

A = [[0.7, 0.3],
     [0.4, 0.6]
]

B = [[0.1, 0.4, 0.5],
     [0.7, 0.2, 0.1]
]


#prob = generateSequence([], [0, 1, 0, 2])

start = time.time()
prob = generatePatterns([])
end = time.time()

print("Final Probability --> " + str(round(prob, 5)))
print("Total Time " + str(end - start))
