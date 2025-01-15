# 117  Write a Python program that spawns two threads: one prints numbers 1 to 5, the other prints letters A to E.



import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in "ABCDE":
        print(letter)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
