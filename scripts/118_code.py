# Write a script that repeatedly asks the user for a number, catches ValueError if the input is invalid, and stops when a valid number is entered.

def get_valid_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            print("You entered:", number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

 
get_valid_number()
