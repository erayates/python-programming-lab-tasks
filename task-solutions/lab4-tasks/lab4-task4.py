# Task 4
def calculate_easter(year):
    if year < 1900 or year > 2099:
        print("Please enter valid year within the range.")

    a = year % 19
    b = year % 4
    c = year % 7
    d = (a * 19 + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    if d + e < 10:
        print(d + e + 22,".III")
    else:
        print(d + e - 9,".IV")


calculate_easter(1999)
calculate_easter(2013)
calculate_easter(2008)
calculate_easter(2022)
calculate_easter(2023)
calculate_easter(2024)
