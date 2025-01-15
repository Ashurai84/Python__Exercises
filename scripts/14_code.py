# Write a function that takes a string s and an integer n, and returns the string repeated n times.
def repeat_string(s, n):
    result = ""
    for _ in range(n):
        result += s
    return result

 
string = input("enter your string :  ")
times = int(input("enter your number : "))
print("Repeated string: ", repeat_string (string , times))
