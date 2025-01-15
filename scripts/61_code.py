# 62 . Generate a dictionary that contains numbers (1 to n) as keys and their squares as values.

def generate_dict(n):
    return {i: i**2 for i in range(1, n + 1)}

# Example usage
n = 5
generated_dict = generate_dict(n)
print("Generated dictionary:", generated_dict)
