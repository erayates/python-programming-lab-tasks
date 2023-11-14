# Input dictionary
input_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

# Sorting the lists alphabetically
sorted_dict = {k: sorted(v) for k, v in input_dict.items()}

# Printing the sorted dictionary
print(f"Output: {sorted_dict}")
