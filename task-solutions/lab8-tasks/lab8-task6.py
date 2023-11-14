# Task 6
userInput = input("Enter a comma-seperated string: ")
striped_ver = " ".join(userInput.split())
split_ver = striped_ver.split(", ")
sorted_ver = sorted(split_ver)

output = ""
for item in sorted_ver:
    if sorted_ver.index(item) == len(sorted_ver) - 1:
        output += item
    else:
        output += item + ","

print(output)

