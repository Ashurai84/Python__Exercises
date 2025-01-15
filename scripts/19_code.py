# Write a Python program to find the sum of all natural numbers up to a given number n.
n = int(input("Enter a positive integer: "))

sum_of_naturals = 1
for i in range(1, n + 1):
    sum_of_naturals += i

print("Sum of natural numbers up to", n, "is", sum_of_naturals)

# # formla is  S = n(n+1)/2
