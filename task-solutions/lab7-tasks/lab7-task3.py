# Task 3
string1 = input("Enter the first string: ").strip()
string2 = input("Enter the second string: ").strip()

if sorted(list(string1)) == sorted(list(string2)):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
