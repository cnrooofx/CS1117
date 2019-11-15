# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    """
    Call the functions defined in the functions.py file
    print(to_engligh(314))
    """
    '''
    print(functions.to_english(142))  # -> “One hundred and forty two”
    print(functions.to_english(-142))  # -> “Minus one hundred and forty two”
    print(functions.to_english(11))  # -> “Eleven"
    print(functions.to_english(42))  # -> “Forty two"
    print(functions.to_english(9))  # -> “Nine"
    print(functions.to_english(716))  # -> “Nine hundred and ninety nine"
    print(functions.to_english(305))  # -> Minus eleven
    print(functions.to_english(0))  # -> Zero
    print(functions.to_english(-9))  # -> Minus nine
    print(functions.to_english(-999))  # -> Minus nine hundred and ninety nine
    print(functions.to_english(10))  # -> Ten
    print(functions.to_english(70))  # -> Seventy
    print(functions.to_english(-1))  # -> Minus one
    i = 0
    while i < 1000:
        print(functions.to_english(i))
        i += 1
    '''
    '''
    print(functions.sort_a_list([2, -3]))  # -> [-3,2]
    print(functions.sort_a_list([2, 3, 2]))  # -> [2,3]
    print(functions.sort_a_list([2, 3, 1]))  # -> [1,2,3]
    print(functions.sort_a_list(['z', 'a']))  # -> ['a', 'z']
    print(functions.sort_a_list(['H', 'B']))  # -> ['B', 'H']
    print(functions.sort_a_list(['a', 'B']))  # -> ['B', 'a']
    print(functions.sort_a_list([1, 3, 6, 8, 3, 2, 0]))
    print(functions.sort_a_list(["a", "j", "d", "g", "e", "f", "g", "r"]))
    print(functions.sort_a_list(["A", "j", "d", "G", "e", "f", "g", "r"]))
    print(functions.sort_a_list(['M', 'p', 'V', 'Z', 'V', 'q', 'D', 'q', 'B', 'B',
                       'n', 'k', 'H', 'm', 'p', 'K', 'W', 'j', 'Y', 'Z']))
    '''
    '''
    print(functions.ascii_difference([1, 2], [3, 4]))  # -> ([100, 102], [2, 2])
    print(functions.ascii_difference(['a', 2], [3, 4]))  # -> ([148, 102], [46, 2])
    print(functions.ascii_difference([1, 'b'], [3, 4]))  # -> ([100, 150], [2, 46])
    print(functions.ascii_difference(['1', '2', '3'], []))  # -> ([49, 50, 51], [49, 50, 51])
    print(functions.ascii_difference([1, 2], [3, 'C']))  # -> ([100, 117], [2, 17])
    print(functions.ascii_difference(['a', 'b'], ['z', 'd']))  # -> ([219, 198], [25, 2])
    '''
    print(functions.ascii_difference([1, 2], [3, 4]))
    print(functions.ascii_difference(['a', 2], [3, 4]))


if __name__ == "__main__":
    main()
