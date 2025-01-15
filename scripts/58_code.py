# 59. Write a program to check if a given key exists in a dictionary.

def check_key_existence(d, key):
    return key in d

# Example usage
my_dict = {"a": 1, "b": 2, "c": 3}
key = "a"
print("Does the key exist?", check_key_existence(my_dict, key))
