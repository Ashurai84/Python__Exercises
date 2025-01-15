# 53 Write a program to remove all even numbers from a list of integers.

def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = remove_even_numbers(numbers)
print("List after removing even numbers:", filtered_numbers)

