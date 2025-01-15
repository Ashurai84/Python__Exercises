#39 .  Write a program to count how many times a specific character appears in a given string.
def count_occurrences(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# Example usage
string = input("Enter a string: ")
character = input("Enter a character to count: ")
print("Number of occurrences of", character, "in the string:", count_occurrences(string, character))


