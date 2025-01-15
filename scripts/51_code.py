# 52. Given a list, write a Python function to find all duplicate elements.
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

 
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Duplicate elements in the list:", find_duplicates(numbers))
