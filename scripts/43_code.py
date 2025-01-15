# 44. Write a Python function that removes duplicate elements from a list and returns the new list.
def remove_duplicates(lst):
    return list(set(lst))

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates:", unique_numbers)

