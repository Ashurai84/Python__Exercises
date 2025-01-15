# 85 Write a Python script to read a CSV file and print each row.

def is_subset(set1, set2):
    return set1.issubset(set2)

# Example usage
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Is set1 a subset of set2?", is_subset(set1, set2))
