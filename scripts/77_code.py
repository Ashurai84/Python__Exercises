# 78 Write a Python program to copy the contents of one file to another.


def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        print("File has been copied.")
    except FileNotFoundError:
        print("Source file not found.")
    except IOError:
        print("An error occurred while copying the file.")

# Example usage
source_path = input("Enter the path to the source file: ")
destination_path = input("Enter the path to the destination file: ")
copy_file(source_path, destination_path)
