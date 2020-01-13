# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    # functions.three_numbers("one", "two", "three")
    '''
    print(functions.seasons(4.5))
    print(functions.seasons("hello"))
    print(functions.equal_numbers(16, 16))
    print(functions.equal_numbers(4, 9))
    print(functions.equal_numbers("five", 5))
    print(functions.seasons(3))
    print(functions.seasons(6))
    print(functions.grades(99))
    print(functions.grades(144))
    print(functions.grades("hello"))
    '''
    print(functions.three_numbers(1, 2, 3))
    print(functions.three_numbers("one", "two", "three"))
    print(functions.three_numbers(1, 1, 1))
    print(functions.fizz_buzz(15))
    print(functions.fizz_buzz("hrllo"))


if __name__ == '__main__':
    main()
