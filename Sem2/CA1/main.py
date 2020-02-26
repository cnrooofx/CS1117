# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    # print('\nFractions\n')
    # print(functions.fractions("OTTACACTTAT"))  # ⇒ (0.2,0.0,0.5,0.3)
    # print(functions.fractions("CC"))  # ⇒ (1.0,0.0,0.0,0.0)
    # print(functions.fractions("F"))  # ⇒ (0.0,0.0,0.0,0.0)
    # print(functions.fractions("FT"))  # ⇒ (0.0,0.0,1.0,0.0)
    # print(functions.fractions("1"))  # ⇒ (0.0,0.0,0.0,0.0)
    # print(functions.fractions(1))  # ⇒ "input must be a string character"
    # print(functions.fractions('OTTACACTTATTTTTTC'))
    # print('\nF\n')
    # S1 = [105, 101, 105, 100, 105]
    # S2 = [100, 102, 101, 102, 101]
    # print(functions.F(S1, S2))
    # print(functions.F_while(S1, S2))
    # print(functions.F_list_comp(S1, S2))
    # print(functions.F_lambda(S1, S2))
    # print('\nFrequencies\n')
    # print(functions.frequencies("CCABBADCAC"))  # ⇒ {"A":3, "B":2, "C":4, "D":1}
    # print(functions.frequencies([4, 7, 4, 7, 4]))  # ⇒ {4:3, 7:2}
    # print(functions.frequencies(1))  # ⇒ "input is incorrect"
    print('\nFirsts\n')
    # print(functions.firsts("mississippi"))  # ⇒ "misp"
    # print(functions.firsts("abcdefg"))  # ⇒ " abcdefg "
    # print(functions.firsts("aaaaaaaa"))  # ⇒ "a"
    # print(functions.firsts(""))  # ⇒ ""
    # print(functions.firsts(123454321))  # ⇒ "12345"
    print(functions.firsts([1, 2, 3, 4, 5, 4, 3, 2, 1]))
    # print('\nExtract\n')
    # print(functions.extract("Yesterday I saw an aardvark while walking my pet tortoise, Frank. What a sight this was! Aardvarks are nocturnal animals appearing in daylight with caution. Make sure to bring kippers when you visit", 1, 5))


if __name__ == "__main__":
    main()
