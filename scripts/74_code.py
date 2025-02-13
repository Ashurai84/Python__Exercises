# 75. Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of", num1, "and", num2, "is", gcd(num1, num2))

