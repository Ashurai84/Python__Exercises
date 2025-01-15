# 92. Create classes Rectangle and Square. Square should inherit from Rectangle (or implement composition) in a way that automatically sets the length and width to the same value.

def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4]
occurrences = count_occurrences(numbers)
print("Occurrences of each element:", occurrences)
