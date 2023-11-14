# Task 9

# Task 9 - 1
from math import *

float_num = float(input("Enter a float number to calculate the equation: "))
calculated_equation = 0
if float_num == 0:
    calculated_equation = -1
    print(calculated_equation)
else:
    calculated_equation = (3 * pow(float_num, 3)) - (2 * pow(float_num, 2)) + (3 * float_num) - 1
    print(int(calculated_equation))


# Task 9 - 2
float_num_2 = float(input("Enter a float number to calculate the equation: "))
calculated_equation_2 = 0

if float_num_2 == 0:
    print(calculated_equation_2)
else:
    sqrt_float = pow(float_num_2, 2)
    sqrt_pi = pow(pi, 2)
    left_side_of_equation = sqrt_float / (sqrt_pi * (sqrt_float + 0.5))
    right_side_of_equation = 1 + (sqrt_float / (sqrt_pi * sqrt(sqrt_float - 0.5)))
    calculated_equation_2 = left_side_of_equation / right_side_of_equation
    print(calculated_equation_2)


# Task 9 - 3

float_num_3 = float(input("Enter a float number to calculate the equation: "))
calculated_equation_3 = 1 / (float_num_3 + (1 / (float_num_3 + (1 / float_num_3 + (1 / float_num_3)))))
print(calculated_equation_3)