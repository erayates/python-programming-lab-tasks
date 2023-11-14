# Task 5
import random

print('Please provde the range (in the form of integers)')
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

random_values = [round(random.uniform(start_range, end_range), 3) for _ in range(5)]

# Displaying the results
print("The list of 5 random real values within the given range is:")
print(random_values)