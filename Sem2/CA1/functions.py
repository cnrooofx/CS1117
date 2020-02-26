# Script Name: functions.py
# Author: Conor Fox 119322236
# Semester 2 - Continuous Assessment 1


# 1
def fractions(DNA):
    if isinstance(DNA, str):
        c = 0.0
        g = 0.0
        t = 0.0
        a = 0.0
        dna_string = ''
        for char in DNA:
            if char in ('C', 'G', 'T', 'A'):
                dna_string += char
        if dna_string != '':
            length = len(dna_string)
            for char in dna_string:
                if char == 'C':
                    c += 1
                elif char == 'G':
                    g += 1
                elif char == 'T':
                    t += 1
                else:
                    a += 1
            c /= length
            g /= length
            t /= length
            a /= length
        return c, g, t, a
    return 'input must be a string character'


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


# 3
def frequencies(s):
    out_dict = {}
    if isinstance(s, (str, list)):
        s = list(s)
        s.sort()
        for val in s:
            if val not in out_dict:
                out_dict[val] = 1
            else:
                out_dict[val] += 1
        return out_dict
    return "input is incorrect"


# 4
def firsts(s):
    if type(s) == list:
        s = ''.join([str(item) for item in s])
    out = ''
    for char in str(s):
        if char not in out:
            out += char
    return out


# 5
def extract(text, n, m):
    hidden = ''
    text = text.split()
    i = int(m)
    while i < len(text):
        word = text[i-1]
        for to_strip in ('.', ',', '!', '?'):
            word.strip(to_strip)
        if (n-1) not in range(len(word)):
            return 'There is no character %s in the word - %s' % (n, word)
        hidden += word[n-1]
        i += m
    return hidden
