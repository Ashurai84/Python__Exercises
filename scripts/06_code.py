# 5. Write a Python function that takes a string and returns its length without using the built-in len() function

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

my_string = input("Enter the string: ")

 
print("Length:", string_length(my_string))
