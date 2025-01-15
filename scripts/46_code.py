# 47. Write a program to reverse a list in-place (without using reversed() or slicing).
def reverse_list(lst):
    return lst[::-1]

 
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]   

reversed_numbers = reverse_list(numbers)
print("Reversed list:", reversed_numbers)



