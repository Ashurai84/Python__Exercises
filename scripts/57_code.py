# 58.Write a function that inverts a dictionary (keys become values, values become keys).

def invert_dict(d):
    return {v: k for k, v in d.items()}


original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = invert_dict(original_dict)
print("Inverted dictionary:", inverted_dict)


