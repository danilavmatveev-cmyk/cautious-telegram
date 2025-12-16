import math

def estimate_pi(epsilon=1e-15):
    k = 0
    total = 0
    while True:
        x = math.factorial(4 * k) * (1103 + 26390 * k) / (math.factorial(k)**4 * (396 ** (4 * k)))
        total += x



        if abs(x) < epsilon:
            break
        k += 1

    pi_approx = 9801 / (2 * math.sqrt(2) * total)
    return pi_approx


print(estimate_pi())



