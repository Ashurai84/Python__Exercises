#83 write a program to search for a specific substring in a file and print the lines where it appears.

def max_min_list(lst):
    max_val = max(lst)
    min_val = min(lst)
    return max_val, min_val

# Example usage
numbers = [1, 2, 3, 4, 5]
max_value, min_value = max_min_list(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
