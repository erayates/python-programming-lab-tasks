# Task 3
input_list = [2, 6, 7, 1, 34, 64, 2, 7, 35, 1]
output_list = []
seen = set()

for item in input_list:
    if item not in seen:
        output_list.append(item)
        seen.add(item)

print(f"Output: {output_list}")