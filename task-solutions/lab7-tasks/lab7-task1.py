# Task 1
user_input = input("Enter a string to check that string palindrome or not: ")
ct = len(user_input)

string = ""
for letter in user_input:
    if letter == user_input[ct - 1]:
        string += letter
    ct -= 1

if string == user_input:
    print(user_input, "is a palindrome string.")
else:
    print(user_input, "is not a palindrome string.")
