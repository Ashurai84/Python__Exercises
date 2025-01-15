# Write a program that counts the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
