# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    '''
    # functions.count([1, 2, 3, 4, 5, 2, 5, 2, 1], 2)
    functions.index([1, 2, 3, 4, 5, 2, 5, 2, 1], 2)
    print(functions.index("hello", "o"))
    print(functions.index("hello", "p"))
    print(functions.get_value("hello", 7))
    print(functions.get_value("hello", 1))
    print(functions.insert("hello", 1, "p"))
    print(functions.insert("hello", 7, "p"))
    print(functions.insert([1, 2, 3, 4, 5, 2, 5, 2, 1], 2, 7))
    print(functions.insert([1, 2, 3, 4, 5, 2, 5, 2, 1], 12, 7))
    print(functions.insert(12345, 3, "p"))
    print(functions.value_in_list("hello", "o"))
    print(functions.value_in_list("hello", "p"))
    '''
    print(functions.concat("hello", " world"))
    print(functions.concat(["hello"], ["world"]))
    '''
    print(functions.remove("h", "hello"))
    print(functions.remove("p", "hello"))
    '''


if __name__ == "__main__":
    main()
