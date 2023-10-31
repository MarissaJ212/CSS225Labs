#Marissa Jones
#10=31-2023

#Mod6 Lab Activity

import math

def calculate_pi_approximation(n):
    approximation = 0
    for i in range(n):
        approximation += (-1) ** i / (2 * i + 1)
    return 4 * approximation

# Number of iterations (higher values will give a more accurate approximation)
iterations = 1000000

pi_approximation = calculate_pi_approximation(iterations)

print(f"Approximation of pi using Leibniz formula: {pi_approximation}")
print(f"Value of pi from the math module: {math.pi}")