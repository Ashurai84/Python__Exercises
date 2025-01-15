# 55. Write a Python function to check if a given list is sorted in ascending order.

def is_sorted(lst):
    return lst == sorted(lst)


numbers = [1, 2, 3, 4, 5]
print("Is the list sorted?", is_sorted(numbers))
