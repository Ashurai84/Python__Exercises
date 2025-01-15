# 82 Write a program that finds the longest word in a text file and prints it.

def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage
string = "hello world"
char_freq = char_frequency(string)
print("Character frequencies:", char_freq)
