# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 2, 9, 0, 9]
    print(functions.chooseLargest(l1, l2))
    # for pair in zip(l1, l2):
    #     print(pair)
    # functions.lottery()


if __name__ == "__main__":
    main()
