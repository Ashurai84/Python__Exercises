# 74 .Write a recursive function that checks if a string is a palindrome.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")