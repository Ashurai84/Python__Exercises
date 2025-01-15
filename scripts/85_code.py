# 86 Define a class Person with attributes name and age. Create an instance of this class and print its attributes.


def intersection_list(lst1, lst2):
    return list(set(lst1) & set(lst2))


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Intersection of the lists:", intersection_list(list1, list2))
