# ScriptName: main.py
# Author: Conor Fox 119322236

import functions


def main():

    print(functions.seasons(1))
    print(functions.seasons(2))
    print(functions.seasons(3))
    print(functions.seasons(4))
    print(functions.seasons(5))
    print(functions.seasons("a"))


    print(functions.grades("F"))
    print(functions.grades("E"))
    print(functions.grades("D"))
    print(functions.grades("C"))
    print(functions.grades("B"))
    print(functions.grades("A"))
    print(functions.grades(10))
    print(functions.grades(30))
    print(functions.grades(60))
    print(functions.grades(80))
    print(functions.grades(99))
    print(functions.grades(300))


    print(functions.fizz_buzz(15, 3, 5))
    print(functions.fizz_buzz(20, 10, 6))
    print(functions.fizz_buzz(81, 8, 9))


    print(functions.slice_reverse("Racecar"))
    print(functions.slice_reverse(("r", "o", "t", "a", "v", "a", "t", "o", "r")))


    print(functions.add_to_list("c", ["o", "n", "r"]))


if __name__ == "__main__":
    main()
