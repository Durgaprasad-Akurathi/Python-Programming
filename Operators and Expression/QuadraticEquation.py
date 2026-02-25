'''
Formula: (-b ± √b^2 - 4ac)/(2a)

Note: The discriminant D = b**2 - 4*a*c determines the nature of the roots:

D > 0: Two distinct real roots.
D = 0: One real root (repeated).
D < 0: Two complex roots (not real).

A math domain error in your quadratic equation program occurs when the value inside the square root (math.sqrt(b**2 - 4*a*c)) is negative.

'''

import math

def QuadraticEquation(a, b, c):
    roots1 = (-b + math.sqrt((b**2) - 4*a*c)) / (2 * a)
    roots2 = (-b - math.sqrt((b**2) - 4*a*c)) / (2 * a)
    return roots1, roots2


a = int(input('Enter the "a" value: '))
b = int(input('Enter the "b" value: '))
c = int(input('Enter the "c" value: '))

# a, b, c = map(int, input('Enter the a, b and c values: ').split())

print("Quadratic roots are r1 & r2 is: ", QuadraticEquation(a, b, c))
