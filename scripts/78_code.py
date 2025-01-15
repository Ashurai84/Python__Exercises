# 79 Write a Python program that reads a file and counts the number of words in it.

def word_count_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        print("Number of words in the file:", len(words))
    except FileNotFoundError:
        print("File not found.")

# Example usage
file_path = input("Enter the path to the file: ")
word_count_in_file(file_path)


