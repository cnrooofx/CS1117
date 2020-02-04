# Script Name: main.py
# Author: Conor Fox 119322236

import functions

codon_map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine',
             'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
             'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine',
             'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
             'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
             'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}

hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

steps = [[10740, 9098, 10450, 10850, 9864], [9973, 9975, 10909, 9880, 9274],
         [10436, 10070, 10704, 10539, 10148], [9488, 10021, 9180, 9570, 10809],
         [10196, 10364, 9333, 10027, 9551], [10520, 9428, 10041, 9735, 9802],
         [9058, 9200, 9249, 9458, 10795], [9440, 10020, 9966, 9647, 10936],
         [10462, 9574, 9718, 9119, 9360], [12886, 9051, 10066, 9426, 15025]]


def main():
    print(functions.removeVowels("Conor"))
    print(functions.hailStone(10))
    print(functions.hexToBinary("FACE", hexToBinaryTable))
    print(functions.proteins("AUGUUUUCUUAAAUG", codon_map))
    print(functions.tenkSteps(steps))
    print(functions.mostSteps(steps))


if __name__ == "__main__":
    main()
