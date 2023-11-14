# Task 4
list1 = [2, 58, 4, 12, 6, 8, 7, 9]
list2 = [12, 9, 25, 8, 64, 58]

unique_list = []

# 1.way
for item in list1:
    if item not in list2:
        unique_list.append(item)

for item in list2:
    if item not in list1 and item  not in unique_list:
        unique_list.append(item)

print(f"The elements present in list1 but not in list2 and vice versa are: {unique_list}")

# 2.way
set1 = set(list1)
set2 = set(list2)

unique_elements = list(set1 ^ set2)

print(f"The elements present in list1 but not in list2 and vice versa are: {unique_elements}")
