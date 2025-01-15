# 31.A perfect number is a number that is equal to the sum of its positive divisors (excluding itself). Write a program to check if a number is perfect.
number = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

if sum_of_divisors == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
