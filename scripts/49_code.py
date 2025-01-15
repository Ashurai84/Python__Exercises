#50. Write a function to find the second-largest element in a list.
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

# Example usage
numbers = [1, 2, 3, 4, 5, 5]
print("Second largest element in the list:", second_largest(numbers))
