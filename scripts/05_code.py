#4.  Write a Python program that asks the user to input a float number, then prints the integer part (truncate), and the fraction part separately.
 
float_number = float(input("Enter a float number: "))

 
integer_part = int(float_number)

 
fraction_part = float_number - integer_part

 
print("Integer part:", integer_part)
print("Fraction part:", fraction_part)
