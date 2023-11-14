# Task 1
list = [0, 3, 12, 8, 2]
sum = 0
for num in list:
    if num == 0:
        sum = 0
        break
    sum *= num

print("Sum: ", sum)