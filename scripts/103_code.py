# 104 Write a program that lists all files and directories in the current directory using os.listdir().
import os

def list_files_and_directories():
    current_directory = os.getcwd()  
    items = os.listdir(current_directory) 

    print("Files and Directories in '", current_directory, "':")
    for item in items:
        print(item)

# Call the function
list_files_and_directories()
