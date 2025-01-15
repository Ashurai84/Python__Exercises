# 67.	Implement a function fib(n) to return the nth Fibonacci number using recursion.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = int(input("Enter a positive integer: "))
for i in range(n):
    print(fibonacci(i), end=" ")
