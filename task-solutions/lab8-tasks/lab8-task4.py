# Task 4
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    n = int(input("Enter the number of the word in the Fibonacci sequence: "))
    result = fibonacci(n)
    print(f"The value of {n}-th element is: {result}")

