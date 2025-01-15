# 49.Write a function to rotate a list by k positions to the right. For instance, [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

 
numbers = [1, 2, 3, 4, 5]
k = 2
rotated_numbers = rotate_list(numbers, k)
print("List after rotating by", k, "positions:", rotated_numbers)

