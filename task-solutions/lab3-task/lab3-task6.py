# Task 6
five_counter = 0
for i in range(1, 7, 1):
    num = int(input("Enter any number from 1 to 10: "))
    if num == 5:
        five_counter += 1
print("The number 5 was entered", five_counter, "times.")

