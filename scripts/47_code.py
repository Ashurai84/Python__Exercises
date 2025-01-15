# 48.Write a Python program that counts the number of times a given element appears in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
element = 4
count = count_occurrences(numbers, element)
print("Number of occurrences of", element, "in the list:", count)
