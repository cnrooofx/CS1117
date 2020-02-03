# Script Name: functions.py
# Author: Conor Fox 119322236

# 1


def removeVowels(sentence):
    vowels = "aeiou"
    return " ".join([l for l in sentence if l not in vowels])

# 2


def hailStone(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n + 1)
    else:
        print(1)

# 3


def hexToBinary(hex, d):
    return "".join([d[val] for val in hex])

# 4


def proteins(rna, codon_map):
    rna_list = []
    protein_list = []
    while len(rna) > 0:
        val = rna[:3]
        if codon_map[val] == 'stop':
            break
        rna_list.append(val)
        protein_list.append(codon_map[val])
        rna = rna[3:]
    return rna_list, protein_list

# 5


def tenkSteps(stepData):
    total = [0, 0, 0, 0, 0]
    counter = 0
    for employee in stepData:
        day_index = 0
        for day in employee:
            total[day_index] += day
            day_index += 1
    for count_day in total:
        if count_day > 100000:
            counter += 1
    return counter


def mostSteps(stepData):
    # List of employee totals
    week_total = []
    for employee in range(len(stepData)):
        for day in stepData[employee]:
            if employee not in range(len(week_total)):
                week_total.append(day)
                continue
            week_total[employee] += day
    return week_total
