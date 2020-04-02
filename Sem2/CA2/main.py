# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    print(functions.what_am_I(['hi', 'conor', 123, 0.123, [1, 2], ('hi', 'there')], my_type='hello'))
    print(functions.what_am_I([]))



if __name__ == "__main__":
    main()
