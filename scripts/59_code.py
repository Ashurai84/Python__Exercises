# 60 Write a function to merge two dictionaries. If a key appears in both, add their values

def merge_dictionaries(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Example usage
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)
