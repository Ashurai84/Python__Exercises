# 70. Implement binary search recursively to find an element in a sorted list.

def binary_search(lst, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, right)
    else:
        return binary_search(lst, target, left, mid - 1)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target number: "))
index = binary_search(numbers, target, 0, len(numbers) - 1)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
