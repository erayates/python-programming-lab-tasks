# Tasl 2
list = [2, 6, 7, 1, 34, 64, 2, 7, 35, 1]
new_list = []

for i in range(len(list), 0, -1):
    new_list.append(list[i - 1])

print(new_list)