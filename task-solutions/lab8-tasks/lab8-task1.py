# Task 1
def is_palindrome(str):
    ct = len(str)
    string = ""
    for letter in str:
        if letter == str[ct - 1]:
            string += letter
        ct -= 1

    if string == str:
        return True
    else:
        return False


user_input = input("Enter a string to check that string palindrome or not: ")
if is_palindrome(user_input):
    print(user_input, "is a palindrome string.")
else:
    print(user_input, "is not a palindrome string.")



