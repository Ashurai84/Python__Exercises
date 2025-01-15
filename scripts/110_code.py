# 112 Use a lambda function inside map to transform a list of numbers (e.g., multiply each by 2).
def transform_numbers(lst):
    transformed = list(map(lambda x: x * 2, lst))
    return transformed

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Transformed list:", transform_numbers(numbers))
