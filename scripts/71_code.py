# 72 . Write a recursive function that returns the number of vowels in a string.

def count_vowels(s):
    if not s:
        return 0
    if s[0] in "aeiouAEIOU":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
