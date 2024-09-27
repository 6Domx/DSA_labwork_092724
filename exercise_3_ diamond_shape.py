# Pseudocode 
# 1. Create a python function named print_diamond.
# 2. It should take an odd integer n as an argument and prints a diamond shape with the with of n
#    using the width of n using the character " * " .


def print_diamond():
    n = int(input("Please input an odd number only: "))
    if n % 2 == 0:
        print("Please provide an odd integer.")
    else:
        for i in range(n):
            if i < n // 2:
                print(" " * (n // 2 - i) + " * " * (2 * i + 1))
            else:
                print(" " * (i - n // 2) + " * " * (2 * (n - i) - 1))

print_diamond()