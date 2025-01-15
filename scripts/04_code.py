
# 3. Write a Python program that swaps the values of two variables without using a temporary variable.

# Step 1: Get two numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

 
number1, number2 = number2, number1

 
print("After swapping:")
print("First number:", number1)
print("Second number:", number2)
