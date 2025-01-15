# 61. Write a Python program to sort a dictionary by its values in ascending order.

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


my_dict = {"a": 3, "b": 1, "c": 2}
sorted_dict = sort_dict_by_value(my_dict)
print("Dictionary sorted by values:", sorted_dict)
