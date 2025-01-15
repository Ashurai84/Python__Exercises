# Write a program to display the multiplication table of a given integer up to 10.

 

number = int(input("Enter a number: "))

print("Multiplication Table for", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
