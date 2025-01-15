# 66.Implement a function factorial(n) that calculates n! using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a positive integer: "))
print("Factorial of", number, "is", factorial(number))