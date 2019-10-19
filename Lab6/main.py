# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    '''
    # functions.count([1, 2, 3, 4, 5, 2, 5, 2, 1], 2)
    functions.index([1, 2, 3, 4, 5, 2, 5, 2, 1], 2)
    functions.index("hello", "o")
    functions.index("hello", "p")
    functions.get_value("hello", 7)
    functions.insert("hello", 1, "a")
    functions.insert("hello", 7, "a")
    functions.insert([1, 2, 3, 4, 5, 2, 5, 2, 1], 2, 7)
    functions.insert([1, 2, 3, 4, 5, 2, 5, 2, 1], 12, 7)
    '''
    print(functions.value_in_list("hello", "o"))
    print(functions.value_in_list("hello", "p"))


if __name__ == "__main__":
    main()
