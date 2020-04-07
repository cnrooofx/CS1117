# Script Name: main.py
# Author: Conor Fox 119322236

from functions import *


def main():
    print(what_am_I(['hi', 'conor', 123, 0.123, [1, 2], ('hi', 'there')], my_type='all'))
    print(what_am_I(['hi', 'conor', 123, 0.123, [1, 2], ('hi', 'there')], my_type='bob'))
    print(what_am_I([]))
    input_list = [1, "It's", 1.2, "fun", {"hi": "you"}, "time", 2]
    print(what_am_I(input_list, my_type=str))  # ⇒ {'str': ["It's", 'fun', 'time']}



if __name__ == "__main__":
    main()
