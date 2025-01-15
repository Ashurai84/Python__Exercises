# 45 Implement a linear search to find a given element in a list. Return the index if found, or -1 otherwise

def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

# Example usage
numbers = [4, 2, 9, 7, 5]
target = 9
index = linear_search(numbers, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
