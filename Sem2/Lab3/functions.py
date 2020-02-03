# Script Name: functions.py
# Author: Conor Fox 119322236

# 1


def removeVowels(sentence):
    vowels = "aeiou"
    filtered_list = [l for l in sentence if l not in vowels]
    return " ".join(filtered_list)

# 2


def hailStone(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n + 1)
    else:
        print(n)

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
    day_total = []
    counter = 0
    for index in range(len(stepData)):
        for steps in stepData[index]:
            if index not in range(len(day_total)):
                day_total.append(steps)
                continue
            day_total[index] += steps
    for count_day in day_total:
        if count_day > 100000:
            counter += 1
    return counter, day_total


def mostSteps(stepData):
    # List of employee totals for the week
    week_total = []
    # Employee number in range of employee numbers
    for employee in range(len(stepData)):
        for day in stepData[employee]:
            # If employee number isn't already an index, append the value
            if employee not in range(len(week_total)):
                week_total.append(day)
                continue
            # Otherwise add that day to the existing value in the list
            week_total[employee] += day
    return week_total
