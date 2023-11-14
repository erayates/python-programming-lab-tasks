# Task 7
listOne = [1, 2, 3]
listTwo = ["a", "b", "c"]

for i in listOne:
    for j in listTwo:
        print(i,j)
    print()  # Adding a blank line after each group

mixed_values = 'abc'
numbers = [1, 2, 3]

for num in numbers:
    for letter in mixed_values:
        print(f"{num} {letter}")
    print()  # Adding a blank line after each group
