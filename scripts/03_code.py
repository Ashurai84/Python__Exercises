# 2. Write a Python program that prompts the user for two numbers and prints their sum, difference, product, and quotient.

 
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

 
calculator = input("Choose an operation (+, -, *, /): ")

# Step 3: Perform the chosen operation
if calculator == "+":   
    result = number1 + number2
    print("Sum:", result)
elif calculator == "-":
    result = number1 - number2
    print("Difference:", result)
elif calculator == "*":
    result = number1 * number2
    print("Product:", result)
elif calculator == "/":
    if number2 != 0:
        result = number1 / number2
        print("Quotient:", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation!")
