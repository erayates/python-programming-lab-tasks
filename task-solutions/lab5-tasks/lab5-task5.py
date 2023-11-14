# Task 5
l1 = [1,3,6,78,35,24,55]
l2 = [12,24,35,24,88,120,155]

common_items = []


# 1. way
for item in l1:
    if item in l2 and item not in common_items:
        common_items.append(item)

print(f"Common items: {', '.join(map(str, common_items))}")


# 2.way
set1 = set(l1)
set2 = set(l2)
common_items = set1.intersection(set2)

print(f"Common items: {list(common_items)}")

