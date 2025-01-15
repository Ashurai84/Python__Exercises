# 115 Write a simple decorator timer that measures the execution time of a function.
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Example usage
example_function(1000000)
