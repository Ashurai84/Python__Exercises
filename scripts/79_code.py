# 80 Write a program that counts how many lines are in a file.

def line_count_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        print("Number of lines in the file:", len(lines))
    except FileNotFoundError:
        print("File not found.")

# Example usage
file_path = input("Enter the path to the file: ")
line_count_in_file(file_path)
