# 56 Given two lists of the same length, create a dictionary mapping elements of one list to the corresponding elements of the other.
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage
keys = ["a", "b", "c"]
values = [1, 2, 3]
result_dict = lists_to_dict(keys, values)
print("Dictionary from two lists:", result_dict)
