
def EMAlgo(theta1, theta2, T1, T2, iterationn):
    Iterations = 2
    iter = 0

    while iter < Iterations:
        sum_Prob = [0, 0]
        sum_meu = [0, 0]
        for k in range(len(iterationn)):
            n_a = T1 * (theta1 ** iterationn[k][0]) * ((1 - theta1) ** iterationn[k][1])
            n_b = T2 * (theta2 ** iterationn[k][0]) * ((1 - theta2) ** iterationn[k][1])
            interm_a = (n_a / (n_a + n_b))
            interm_b = (n_b / (n_a + n_b))
            sum_Prob[0] += interm_a
            sum_Prob[1] += interm_b

            sum_meu[0] += interm_a * iterationn[k][0]
            sum_meu[1] += interm_b * iterationn[k][0]

        T1 = sum_Prob[0] / len(iterationn)
        T2 = sum_Prob[1] / len(iterationn)
        theta1 = sum_meu[0] / (10 * T1 * 5)
        theta2 = sum_meu[1] / (10 * T2 * 5)
        iter += 1

    return T1, T2, theta1, theta2

iterationn = [
    [8, 2],
    [5, 5],
    [9, 1],
    [4, 6],
    [7, 3]
]

theta1 = 0.6
theta2 = 0.5
T1 = 0.7
T2 = 0.3
T1, T2, theta1, theta2 = EMAlgo(theta1, theta2, T1, T2, iterationn)

print("\n\nOriginal Case -->")
print("Theta 1 -->", theta1)
print("Theta 2 -->", theta2)
print("Tow 1 -->", T1)
print("Tow 1 -->", T2)

# Different Initialization 1
theta1 = 0.8
theta2 = 0.4
T1 = 0.8
T2 = 0.2
T1, T2, theta1, theta2 = EMAlgo(theta1, theta2, T1, T2, iterationn)
print("\n\nDifferent Initialization Case 1-->")
print("Theta 1 -->", theta1)
print("Theta 2 -->", theta2)
print("Tow 1 -->", T1)
print("Tow 1 -->", T2)


# Different Initialization 1
theta1 = 0.9
theta2 = 0.1
T1 = 0.65
T2 = 0.35
T1, T2, theta1, theta2 = EMAlgo(theta1, theta2, T1, T2, iterationn)
print("\n\nDifferent Initialization Case 2-->")
print("Theta 1 -->", theta1)
print("Theta 2 -->", theta2)
print("Tow 1 -->", T1)
print("Tow 1 -->", T2)


# Different Initialization 1
theta1 = 0.1
theta2 = 0.9
T1 = 0.25
T2 = 0.75
T1, T2, theta1, theta2 = EMAlgo(theta1, theta2, T1, T2, iterationn)
print("\n\nDifferent Initialization Case 3-->")
print("Theta 1 -->", theta1)
print("Theta 2 -->", theta2)
print("Tow 1 -->", T1)
print("Tow 1 -->", T2)
