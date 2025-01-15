# Write a program that checks if a number is a palindrome (e.g., 121 -> palindrome).
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if original_number == reversed_number:
    print(original_number, "is a palindrome.")
else:
    print(original_number, "is not a palindrome.")
