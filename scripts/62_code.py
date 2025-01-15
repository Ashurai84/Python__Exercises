# 63 Write a Python program to perform union, intersection, and difference operations on two sets.

def set_operations(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    return union_set, intersection_set, difference_set


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union, intersection, difference = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)

