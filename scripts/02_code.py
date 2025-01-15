# 1. Write a Python program that takes a user’s name and prints a greeting with that name in uppercase and lowercase

def greet_user():
     
    name = input("Enter your name: ")
    
 
    print(f"Hello, {name.upper()}! (in uppercase)")
    print(f"Hello, {name.lower()}! (in lowercase)")

greet_user()
