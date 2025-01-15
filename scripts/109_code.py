#111. Demonstrate advanced list slicing (e.g., reversing a list with slicing, skipping elements) in a script.

def list_slicing_demo(lst):
    reversed_list = lst[::-1]
    skipped_elements = lst[::2]
    print("Original list:", lst)
    print("Reversed list:", reversed_list)
    print("List with skipped elements:", skipped_elements)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_slicing_demo(numbers)
