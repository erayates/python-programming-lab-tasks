def check_common_elements(l1, l2):
    common_elements = set(l1) & set(l2)
    return len(common_elements) == 2

# Input lists
l1_1 = [1, 2, 3, 4, 5]
l2_1 = [4, 5, 6, 7, 8]

l1_2 = [1, 2, 3, 4, 5]
l2_2 = [5, 6, 7, 8, 9]

# Checking for common elements
result1 = check_common_elements(l1_1, l2_1)
result2 = check_common_elements(l1_2, l2_2)

# Output
print(f"Output: {result1}")
print(f"Output: {result2}")