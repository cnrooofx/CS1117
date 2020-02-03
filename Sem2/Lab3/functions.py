# Script Name: functions.py
# Author: Conor Fox 119322236

# 1
def removeVowels(sentence):
    vowels = "aeiou"
    filtered_list = [l for l in sentence if l not in vowels]
    return " ".join(filtered_list)

# 2
def hailStone(n):
    """
    n -- Positive integer
    Generates the hailstone sequence of a given positive number n. If n is
    even, the next value is n/2. If n is odd, the next value is 3n + 1.
    """
    while n > 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n + 1)
    else:
        print(n)

# 3
def hexToBinary(hex, d={'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                        '8': '1000 ', '9': '1001', 'A': '1010', 'B': '1011',
                        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}):
    """
    hex -- Hexadecimal string to be converted
    d -- Dictionary of hexadecimal to binary digits
    return -- Binary string value
    Accepts a hex string and returns the corresponding binary string value.
    """
    # Creates a list of the binary digits and joins them into a string.
    return "".join([d[val] for val in hex])

# 4
def proteins(rna, codon_map={'AUG': 'Methionine', 'UUU': 'Phenylalanine',
                             'UUC': 'Phenylalanine', 'UUA': 'Leucine',
                             'UUG': 'Leucine', 'UCU': 'Serine',
                             'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
                             'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
                             'UGU': 'Cysteine', 'UGC': 'Cysteine',
                             'UGG': 'Tryptophan', 'UAA': 'stop', 'UAG': 'stop',
                             'UGA': 'stop'}):
    """
    rna -- String of RNA
    codon_map -- Dictionary that maps the codons to proteins.
    return -- Tuple with two lists, one of the RNA ans one of the proteins.
    """
    # List of the RNA values
    rna_list = []
    # List of the corresponding protein names
    protein_list = []
    while len(rna) > 0:
        # Takes the first three letters
        val = rna[:3]
        # Breaks out of the loop if a stop codon is encountered
        if codon_map[val] == 'stop':
            break
        # Add the RNA value to the list
        rna_list.append(val)
        # Takes the protein name from the dictionary and adds to the list
        protein_list.append(codon_map[val])
        # Takes off those three letters to check the next RNA value
        rna = rna[3:]
    return rna_list, protein_list

# 5
def tenkSteps(stepData):
    """
    stepData -- Table (list of lists) with employees step counts for the week.
    return -- The number of days with over 100,000 total steps.
    Takes a table and returns the number of week-days on which at least 100,000
    steps were made cumulatively by all employees.
    """
    # List of total steps of all employees per day
    day_total = []
    # Count of days with more than 100,000 steps
    counter = 0
    # Loop through each employee in the table
    for employee in stepData:
        # Index is employee number, get employees steps for the week
        for index, steps in enumerate(employee):
            # If day isn't already an index, append the value
            if index not in range(len(day_total)):
                day_total.append(steps)
                continue
            # Otherwise add steps to the existing day in the list
            day_total[index] += steps
    # Counter for days with over 100,000 steps
    for count_day in day_total:
        if count_day > 100000:
            counter += 1
    return counter


def mostSteps(stepData):
    """
    stepData -- Table (list of lists) with employees step counts for the week.
    return -- Employee number with the highest step count
    The number of the employee who took the most steps in the week.
    """
    # List of employee totals for the week
    week_total = []
    # Loop through the table with indexes as employee numbers
    for employee, steps_list in enumerate(stepData):
        # Loops through daily steps in each employees week
        for day in steps_list:
            # If employee number isn't already an index, append the value
            if employee not in range(len(week_total)):
                week_total.append(day)
                continue
            # Otherwise add that day to the existing value in the list
            week_total[employee] += day
    # Return the employee with the highest weekly total
    return week_total.index(max(week_total))
