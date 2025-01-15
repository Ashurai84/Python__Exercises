# 37.Write a program that displays the Collatz sequence for any positive integer given by the user.
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

# Example usage
num = int(input("Enter a positive integer: "))
print("Collatz sequence for", num, "is:", collatz_sequence(num))
