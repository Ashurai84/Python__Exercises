# 100 Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.

def generate_even_numbers(n):
    return [i for i in range(2, n+1) if i % 2 == 0]


n = 10
print("List of even numbers from 2 to", n, ":", generate_even_numbers(n))
