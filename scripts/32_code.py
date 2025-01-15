# 33. Write a program to count the number of words in a user-input string (words are separated by spaces).
def count_words(s):
    words = s.split()
    return len(words)

 
string = input("Enter a string: ")
print("Number of words:", count_words(string))
