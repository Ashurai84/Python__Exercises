# 81 Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.

def merge_dicts(d1, d2):
    merged = d1.copy()  # Copy the first dictionary to avoid modifying it directly
    merged.update(d2)   # Update with the second dictionary
    return merged

# Example usage
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)
