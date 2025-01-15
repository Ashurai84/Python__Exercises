#77.  Write a program that prompts the user for a line of text and writes that line to a file.

def write_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text has been written to the file.")
    except IOError:
        print("An error occurred while writing to the file.")

# Example usage
file_path = input("Enter the path to the file: ")
text = input("Enter the text to write: ")
write_file(file_path, text)
