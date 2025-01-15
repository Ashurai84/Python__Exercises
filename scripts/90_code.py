#  91 .In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).

def remove_duplicates(lst):
    return list(set(lst))


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates:", unique_numbers)
