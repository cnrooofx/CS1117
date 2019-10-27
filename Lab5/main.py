# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    print(functions.while_loop(-10, False, True))
    print(functions.while_loop())  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(functions.while_loop(5))  # -> [1, 2, 3, 4, 5]
    print(functions.while_loop(-5))  # -> [1, 0, -1, -2 ,-3, -4 ,-5]
    print(functions.while_loop(5))  # -> [1, 2, 3, 4, 5, 15]
    print(functions.while_loop(14))  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
    print(functions.while_loop(14, True))  # -> [2, 4, 6, 8, 10, 12, 42]
    print(functions.while_loop(14, False))  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
    print(functions.while_loop())  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]
    print(functions.while_loop())  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]
    print(functions.while_loop(14, False, True))  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 479001600]
    print(functions.while_loop(14, even=False, factorial=True))
    # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 479001600]


if __name__ == "__main__":
    main()
