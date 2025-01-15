#34.  Write a function to check if a 3-digit number is an Armstrong number (e.g., 153 -> 1^3 + 5^3 + 3^3 = 153)
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number

# Example usage
num = int(input("Enter a 3-digit number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
