# Write a Python script to print the multiplication table for numbers 1 through 5 (using nested loops).
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
