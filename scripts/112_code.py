# 114 Write a script that demonstrates the difference between a list comprehension and a generator expression for large data.



def list_vs_generator_comprehension(n):
    # List comprehension
    list_comp = [i * 2 for i in range(n)]
    # Generator expression
    gen_expr = (i * 2 for i in range(n))
    
    # Print first 10 elements from list comprehension
    print("First 10 elements from list comprehension:", list_comp[:10])
    # Print first 10 elements from generator expression
    print("First 10 elements from generator expression:", [next(gen_expr) for _ in range(10)])


n = 1000000
list_vs_generator_comprehension(n)
