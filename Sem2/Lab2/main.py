# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    print(functions.reducedFeeEntitlement({"Conor": ["cs1112", "cs1117", "cs1131"], "Katie": ["ma1101", "cs1112"]}))
    # print(functions.commonModules({"Conor": ["cs1112", "cs1117", "cs1131"], "Katie": ["ma1101", "cs1112", "cs1117"]}, "Conor", "Katie"))
    # print(functions.iter_factorial(10))
    # functions.fizz_buzz()


if __name__ == "__main__":
    main()
