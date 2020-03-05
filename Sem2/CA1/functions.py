# Script Name: functions.py
# Author: Conor Fox 119322236
# Semester 2 - Continuous Assessment 1


# 1
def fractions(DNA):
    """gives fraction of DNA in the overall string

    :param DNA: input string or list to check
    :returns: fraction of C, G, T, A in the input
    """
    # Checks that DNA is a non-empty string
    if isinstance(DNA, (str, list)) and DNA:
        c = 0.0
        g = 0.0
        t = 0.0
        a = 0.0
        dna_string = ''
        # Create a new string with only the correct letters
        for char in DNA:
            if char in ['C', 'G', 'T', 'A']:
                dna_string += char
        if dna_string != '':
            # Length is the total number of correct letters
            length = len(dna_string)
            # Loop through the new string counting occurrences of the letters
            for char in dna_string:
                if char == 'C':
                    c += 1
                elif char == 'G':
                    g += 1
                elif char == 'T':
                    t += 1
                else:
                    a += 1
            # Divide the number of characters by length to get the fraction
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
    return [e for e in S1 if e in S2]


# (c)
def F_lambda(S1, S2):
    return list(filter(lambda e: e in S2, S1))


# (d)
def F_error(S1, S2):
    if isinstance(S1, list) and isinstance(S2, list):
        R = []
        for e1 in S1:
            for e2 in S2:
                if e1 == e2:
                    R += [e1]
                    break
        return R
    return 'Error - input must be a list'


# 3
def frequencies(s):
    """creates a dictionary with the count of each distinct item in a sequence

    :param s: string or list to check
    :returns: sorted dictionary
    """
    # Check to make sure that the input is a list or a string
    if isinstance(s, (str, list)):
        s = list(s)
        # Sort the list so that the dictionary will be sorted
        s.sort()
        # Initialize a dictionary with a key for unique characters in the list
        out_dict = {val: 0 for val in s}
        # For each character, increment the dictionary value
        for val in s:
            out_dict[val] += 1
        return out_dict
    return 'input is incorrect'


# 4
def firsts(s):
    """returns the string formed from the first occurrence of each item in s

    :param s: item to check (can be str, int, list or tuple)
    :returns: string of the first occurrence of each item in s
    """
    # Convert lists and tuples to strings
    if isinstance(s, (list, tuple)):
        s = ''.join([str(item) for item in s])
    out = ''
    # Loop through the input
    for char in str(s):
        # Add the character to the output if it isn't already there
        if char not in out:
            out += char
    return out


# 5
def extract(text, n, m):
    """extracts a hidden message from a passage of text

    :param text: string of text containing a hidden message
    :param n: checks the 'n'th letter of the words
    :param m: checks every 'm'th word
    :returns: the hidden message
    """
    hidden = ''
    text = text.split()
    i = int(m)
    while i < len(text):
        word = text[i-1]
        # Strip multiple times to remove different punctuation marks
        for to_strip in ('.', ',', '!', '?'):
            word.strip(to_strip)
        # Error if the index is greater than the length of the current word
        if (n-1) not in range(len(word)):
            return 'There is no character %s in the word - %s' % (n, word)
        # Add the required letter of the current word to the output
        hidden += word[n-1]
        # Increment the counter by m to check the next word
        i += m
    return hidden
