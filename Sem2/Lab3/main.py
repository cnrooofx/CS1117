# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    # print(functions.removeVowels("Conor"))
    # print(functions.hailStone(100))
    # print(functions.hexToBinary("FACE", {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    #                                   '5': '0101', '6': '0110', '7': '0111', '8': '1000 ', '9': '1001',
    #                                   'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
    #                                   'F': '1111'}))
    # print(functions.proteins("AUGUUUUCUUAAAUG", codon_map = {'AUG' : 'Methionine', 'UUU' : 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA' : 'Leucine', 'UUG' : 'Leucine', 'UCU' : 'Serine', 'UCC' : 'Serine', 'UCA' : 'Serine', 'UCG' : 'Serine', 'UAU' : 'Tyrosine', 'UAC' : 'Tyrosine', 'UGU' : 'Cysteine', 'UGC' : 'Cysteine', 'UGG' : 'Tryptophan', 'UAA' : 'stop', 'UAG' : 'stop', 'UGA' : 'stop' }))
    print(functions.mostSteps([[1, 9315, 9990, 10812, 9459], [10362, 9549, 10324, 9833, 10252], [10658, 10045, 10680, 9291, 10602], [9051, 9703, 9427, 10774, 9681], [9574, 10371,
 9104, 10571, 9786], [10528, 10016, 9611, 9672, 10826], [10223, 9597, 9867, 10733, 10082], [9470, 9608, 9611, 10743, 9491], [10383, 9226, 10535, 10738,
 9965], [9836, 10099, 9808, 9169, 0]]))


if __name__ == "__main__":
    main()
