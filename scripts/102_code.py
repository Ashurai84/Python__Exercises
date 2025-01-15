# 103 Write a script that gets the current date and time and formats it as YYYY-MM-DD HH:MM:SS.
def is_prime_iterative(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime_iterative(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
