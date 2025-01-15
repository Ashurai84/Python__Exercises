# 96 Implement a Python class that overloads the __str__ method to return a string representation of the object.

def is_palindrome_list(lst):
    return lst == lst[::-1]

# Example usage
numbers = [1, 2, 3, 2, 1]
print("Is the list a palindrome?", is_palindrome_list(numbers))
