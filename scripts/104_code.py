#105 Use the statistics module to compute the mean, median, and mode of a list of numbers.


import statistics

def compute_statistics(numbers):
    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    mode_value = statistics.mode(numbers)
    return mean_value, median_value, mode_value

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6]
mean, median, mode = compute_statistics(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
