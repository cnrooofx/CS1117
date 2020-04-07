# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    # print(functions.what_am_I(['hi', 'conor', 123, 0.123, [1, 2], ('hi', 'there')], my_type='all'))
    # print(functions.what_am_I(['hi', 'conor', 123, 0.123, [1, 2], ('hi', 'there')], my_type='bob'))
    # print(functions.what_am_I([]))
    # input_list = [1, "It's", 1.2, "fun", {"hi": "you"}, "time", 2]
    # print(functions.what_am_I(input_list, my_type=str))  # ⇒ {'str': ["It's", 'fun', 'time']}
    # print(functions.who_am_I('file.txt'))
    # print(functions.who_am_I("input.txt"))  # ⇒ {'int': [1, 2], 'float': [2.4, 1.4], 'bool': [True, False], 'str': ['Oops', 'OK']}
    # print(functions.matrices('input2.txt'))
    # matrices_list = matrices('input2.txt')
    matrices_list = [[1, 2, 3, 4, 5, 1],
                     [1, 2, 3, 4, 5, 2],
                     [1, 2, 3, 4, 5, 3],
                     [1, 2, 3, 4, 5, 4],
                     [1, 2, 3, 4, 5, 5],
                     [1, 2, 3, 4, 5, 6]]
    print(functions.sum_me(matrices_list))


if __name__ == "__main__":
    main()
