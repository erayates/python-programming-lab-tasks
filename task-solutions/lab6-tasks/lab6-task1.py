# Task 1
ct = 0
l = ['aba','abc','b','3223','sue','34231','xy']
for item in l:
    if len(item) > 2 and item[0] == item[-1]:
        ct += 1

print(ct)
