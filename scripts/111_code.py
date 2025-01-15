# 113 Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.
from functools import reduce

def filter_and_sum(lst):
    filtered = list(filter(lambda x: x % 2 != 0, lst))
    total_sum = reduce(lambda x, y: x + y, filtered)
    return total_sum

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print("Sum of odd numbers:", filter_and_sum(numbers))
