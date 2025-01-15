#57  Write a program that counts the frequency of each element in a list using a dictionary.

def frequency_count(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = frequency_count(numbers)
print("Frequency count of elements:", frequency)
