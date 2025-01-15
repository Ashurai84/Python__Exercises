# 54. Write a program to shuffle a list in-place (you can use random.shuffle or implement your own shuffling algorithm).


import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst


numbers = [1, 2, 3, 4, 5]
shuffled_numbers = shuffle_list(numbers)
print("Shuffled list:", shuffled_numbers)

