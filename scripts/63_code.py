# 64 Given a list with duplicates, use a set to create a list of unique elements (in any order).

def unique_elements(lst):
    return list(set(lst))


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = unique_elements(numbers)
print("Unique elements in the list:", unique_numbers)
