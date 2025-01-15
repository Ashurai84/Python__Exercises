# 94  Demonstrate polymorphism by defining a method draw() in multiple classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.

def common_elements_three_lists(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 6, 7, 8]
print("Common elements in three lists:", common_elements_three_lists(list1, list2, list3))
