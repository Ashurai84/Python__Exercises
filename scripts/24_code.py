
# Write a simple “guess the number” game. The program randomly generates a number between 1 and 10, and the user has to guess it.

# import random

# number_to_guess = random.randint(1, 10)
# user_guess = int(input("Guess a number between 1 and 10: "))

# if user_guess == number_to_guess:
#     print("Congratulations! You guessed the number.")
# else:
#     print("Sorry, the correct number was", number_to_guess)


#  another one 

from random import randint
Low , High = 1 , 10
secret_number = randint( Low , High)
while True:
 guess = input(f"guess a number between {Low} and {High}")
 number = int(guess)
 if number > secret_number:
     print(f"secret_number is less than {number}")
 elif number< secret_number:
     print(f" secret number is greater than {number}")
 else:
     break
print(f"you guessed it !!! the secret number is {number}")