# Write a Python program that calculates simple interest. Prompt for principal, rate, and time, then compute the interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple interest:", simple_interest)
