# Write a Python program to calculate compound interest given principal, rate, and time in years.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest applied per year: "))

compound_interest = principal * (1 + (rate / (n * 100)))**(n * time)
print("Compound interest:", compound_interest)
