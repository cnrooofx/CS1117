# Script Name: functions.py
# Author: Conor Fox 119322236
# Semester 2 - Continuous Assessment 1


# 1
def fractions(DNA):
    if type(DNA) == str:
        c = 0.0
        g = 0.0
        t = 0.0
        a = 0.0
        dna_string = ''
        for char in DNA:
            char = char.upper()
            if char in ('C', 'G', 'T', 'A'):
                dna_string += char
        if dna_string != '':
            length = len(dna_string)
            count = [0, 0, 0, 0]
            for char in dna_string:
                if char == 'C':
                    count[0] += 1
                elif char == 'G':
                    count[1] += 1
                elif char == 'T':
                    count[2] += 1
                else:
                    count[3] += 1
            c = count[0] / length
            g = count[1] / length
            t = count[2] / length
            a = count[3] / length
        return c, g, t, a
    else:
        return "input must be a string character"


# 2
def F(S1, S2):
    R = []
    for e1 in S1:
        for e2 in S2:
            if e1 == e2:
                R += [e1]
                break
    return R


# (a)
def F_while(S1, S2):
    R = []
    i = 0
    while i < len(S1):
        j = 0
        while j < len(S2):
            if S1[i] == S2[j]:
                R += [S1[i]]
                break
            j += 1
        i += 1
    return R


# (b)
def F_list_comp(S1, S2):
    return [e1 for e1 in S1 for e2 in S2 if e1 == e2]


# 4
def firsts(s):
    out = ''
    for char in str(s):
        if char not in out:
            out += char
    return out
