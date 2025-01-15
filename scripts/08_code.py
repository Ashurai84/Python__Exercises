# Write a Python program that takes three numbers and prints the largest and the smallest numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)

print("Smallest number:", min_num)
print("Largest number:", max_num)
