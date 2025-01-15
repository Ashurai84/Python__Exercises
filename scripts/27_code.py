# Write a program to print a left-aligned triangle of stars of height n.
n = int(input("Enter the height of the triangle: "))

for i in range(1, n + 1):
    print("*" * i)
