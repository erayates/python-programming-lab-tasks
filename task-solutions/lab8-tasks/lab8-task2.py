def is_anagram(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        return True
    return False

# Taking user input
string1 = input("Enter the first string: ").strip()
string2 = input("Enter the second string: ").strip()

if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")