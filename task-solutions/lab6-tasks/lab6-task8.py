# Task 8
lst = [1, 2, 3, 4]

nested_dict = {}
current_dict = nested_dict
for item in lst[:-1]:
    current_dict[item] = {}
    current_dict = current_dict[item]
current_dict[lst[-1]] = {}

print(f"Output: {nested_dict}")
