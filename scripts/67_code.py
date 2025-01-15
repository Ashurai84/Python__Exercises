# 68 . Write a recursive function power(base, exp) that computes base^exp.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Example usage
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(base, "raised to the power of", exponent, "is", power(base, exponent))
