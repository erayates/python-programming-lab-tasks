# Task 2
total_sum = 0
total_number_of_negatives = 0
nums_arr = []

while True:
    num = int(input("Enter an integer number: "))
    nums_arr.append(num)
    total_sum += num

    if num < 0:
        total_number_of_negatives += 1
        if total_number_of_negatives > 10:
            print('You entered more than 10 negative number.')
            break

    if total_sum > 100:
        print('Total value of the numbers that you entered was exceed the 100.')
        break

    if len(nums_arr) > 1:
        if nums_arr[nums_arr.index(num) - 1] == num:
            print("You entered same number with previous number.")
            break
