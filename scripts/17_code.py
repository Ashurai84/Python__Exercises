# Write a program that calculates the factorial of a given positive integer using a for loop.
number = int(input("Enter a positive integer: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)
