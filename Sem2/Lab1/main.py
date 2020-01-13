# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    print("\t Seasons")
    print(functions.seasons(1))
    print(functions.seasons(2))
    print(functions.seasons(3))
    print(functions.seasons(4))
    print(functions.seasons(5))
    print(functions.seasons("S"))
    print("\t Three Numbers")
    print(functions.three_numbers(1, 2, 3))
    print(functions.three_numbers(1, 1, "a"))
    print(functions.three_numbers(2, 2, 2))


if __name__ == "__main__":
    main()
