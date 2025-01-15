# 106  Write a script that takes command-line arguments and prints them.
import sys

def print_args():
    arguments = sys.argv[1:]  # Exclude the script name itself
    for i, arg in enumerate(arguments):
        print(f"Argument {i + 1}: {arg}")

# Example usage
print_args()
