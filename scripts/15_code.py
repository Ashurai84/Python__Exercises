# Write a Python program to round a float to 2 decimal places without using the built-in round() function.
def round_float(number):
    return int(number * 100) / 100

 
float_number = float(input("enter your float number : "))
print("Rounded float:", round_float(float_number))
