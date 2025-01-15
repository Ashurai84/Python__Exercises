# 118 Use the multiprocessing module to run a function in parallel processes and aggregate the results.

import multiprocessing

def compute_square(number):
    return number * number

def main():
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_square, numbers)
    print("Squares:", results)

if __name__ == "__main__":
    main()
