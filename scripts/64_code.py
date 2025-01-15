# 65 Given two lists, write a program to find the common elements using sets.Given two lists, write a program to find the common elements using sets.

def common_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))

 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = common_elements(list1, list2)
print("Common elements between the lists:", common)
