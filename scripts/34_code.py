# 35. Write a Python program to calculate the sum of the series 1 + 1/2 + 1/3 + … + 1/n using a for loop.
def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

# Example usage
n = int(input("Enter a positive integer: "))
print("Sum of the series 1 + 1/2 + 1/3 + ... + 1/", n, "is", sum_of_series(n))
