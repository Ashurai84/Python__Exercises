# 93 Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.

def second_smallest(lst):
    unique_lst = sorted(set(lst))
    if len(unique_lst) >= 2:
        return unique_lst[1]
    else:
        return None


numbers = [5, 3, 9, 1, 7, 3]
print("Second smallest element:", second_smallest(numbers))
