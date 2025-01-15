# 76 Write a Python script that reads a text file and prints its contents.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File contents:")
        print(content)
    except FileNotFoundError:
        print("File not found.")

# Example usage
file_path = input("Enter the path to the file: ")
read_file(file_path)
