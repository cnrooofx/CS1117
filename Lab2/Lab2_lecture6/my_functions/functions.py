#  Script Name : functions.py
#  Author: Conor Fox 119322236


def separated_input(string1, string2, sep_string_value, end_string_value):
    """
    :string1: str -- First input
    :string2: str -- Second input
    :sep_string_value: str -- Value to assign to sep
    :end_string_value: str -- Value to assign to end
    """
    string1 = str(string1.lower())
    string1 = str(string1.capitalize())
    string2 = str(string2.lower())
    string2 = str(string2.capitalize())
    sep_string_value = str(sep_string_value.lower())
    sep_string_value = str(sep_string_value.capitalize())

    print(string1+" ", string2+" ", sep=sep_string_value+" ", end=end_string_value)


def main():
    separated_input("phineas", "ferb", "and", "rock!!!\n")
    separated_input("doofenshmirtz", "incorporated", "Evil", "!!!\n")


if __name__ == '__main__':
    main()

print("The value of __name__ is:", repr(__name__))
