# Task 2
email = input("Enter your email: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")
    if at_index < dot_index:
        print("Your entered email", email, "is valid.")
    else:
        print("Your entered email", email, "is not valid.")
else:
    print("Your entered email", email, "is not valid.")




