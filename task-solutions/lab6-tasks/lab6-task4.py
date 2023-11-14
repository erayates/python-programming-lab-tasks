# Task 4
input = int(input("Enter a number: "))
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for item in d:
    if item == input:
        print("Your entered number key of this dictionary.")

# Another way
if input in d:
    print(f"The number {input} is a key in the dictionary.")
else:
    print(f"The number {input} is not a key in the dictionary.")
