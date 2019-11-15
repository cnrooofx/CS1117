# Continuous Assessment / Labs 9 & 10

# Script Name: functions.py
# Author: Conor Fox 119322236


def to_english(n=0):
    """
    Takes an integer between -999 and 999 inclusive, returns that number
    in english
    n -- Integer, -999 <= n <= 999
    return -- English translation of the number
    """
    answer = ""
    units_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                  5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens_dict = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                  14: "fourteen", 15: "fifteen", 16: "sixteen",
                  17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens_dict = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    if n < 0:  # If the number is negative
        answer = "Minus "  # Add minus to front of answer
        n *= -1  # Make number positive for rest of calulation
    if n in units_dict:  # If number already in a dictionary, use that
        answer += units_dict[n]
    elif n in teens_dict:
        answer += teens_dict[n]
    elif n // 100 != 0:  # Check for hundreds
        answer += units_dict[n // 100] + " hundred"  # First digit
        if n % 100 // 10 != 0:  # Check for tens
            if n % 100 in teens_dict:  # Check for teens
                answer += " and " + teens_dict[n % 100]
            else:
                answer += " and " + tens_dict[n % 100 // 10]
        # Check for units, excluding the teens
        if n % 10 != 0 and n % 100 not in teens_dict:
            # If there is just units, no tens, add 'and'
            if n % 100 // 10 == 0:
                answer += " and"
            # Otherwise add on the units
            answer += " " + units_dict[n % 10]
    elif n // 10 != 0:  # Check for tens
        answer += tens_dict[n // 10]  # Add tens
        if n % 10 != 0:  # If there is units, add those
            answer += " " + units_dict[n % 10]
    else:
        answer += units_dict[n]
    return answer.capitalize()  # Capitalise the first letter of output


def sort_a_list(s):
    """
    Takes a list s and sorts it from smallest value to biggest value.
    s -- Input list
    return -- The sorted list
    """
    new_list = []
    for i in range(len(s)):  # Goes through evert index in the list
        smallest_value = min(s)
        if smallest_value not in new_list:
            # Add the smallest value to the new list
            new_list.append(smallest_value)
        # Remove that value to find next smallest value
        s.remove(smallest_value)
    return new_list


def ascii_difference(m, n):
    """
    Returns two lists, the first with the combined ascii value of the elements
    at the same index number, the second list with the absolute ascii
    difference between each element at the same index number
    m -- First list
    n -- Second list
    return -- List with total combined ascii value and list with
              absolute ascii difference
    """
    ascii_table = {"!": 33, "\"": 34, "#": 35, "$": 36, "%": 37, "&": 38,
                   "\'": 39, "(": 40, ")": 41, "*": 42, "+": 43, ",": 44,
                   "-": 45, ".": 46, "/": 47, "0": 48, "1": 49, "2": 50,
                   "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56,
                   "9": 57, ":": 58, ";": 59, "<": 60, "=": 61, ">": 62,
                   "?": 63, "@": 64, "A": 65, "B": 66,  "C": 67, "D": 68,
                   "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
                   "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80,
                   "Q": 81, "R": 82, "S": 83, "T": 84, "U": 85, "V": 86,
                   "W": 87, "X": 88, "Y": 89, "Z": 90, "[": 91, "\\": 92,
                   "]": 93, "^": 94, "_": 95, "`": 96, "a": 97, "b": 98,
                   "c": 99, "d": 100, "e": 101, "f": 102, "g": 103, "h": 104,
                   "i": 105, "j": 106, "k": 107, "l": 108, "m": 109, "n": 110,
                   "o": 111, "p": 112, "q": 113, "r": 114, "s": 115, "t": 116,
                   "u": 117, "v": 118, "w": 119, "x": 120, "y": 121, "z": 122,
                   "{": 123, "|": 124, "}": 125, "~": 126, "": 0}
    ascii_total = []
    ascii_diff = []
    if len(n) < len(m):  # If the second list n is shorter than the first m:
        i = len(n)
        while i < len(m):
            n.append("")  # Add empty strings as blank values upto length of m
            i += 1
    for i in range(len(m)):
        # Get the ASCII values of the characters, add together and append to
        # the ascii_total output list
        ascii_total.append(ascii_table[str(m[i])] + ascii_table[str(n[i])])
        # Get the ASCII values of the characters, take them from each together,
        # get the positive value and append to the ascii_diff output list
        ascii_diff.append(abs(ascii_table[str(m[i])] - ascii_table[str(n[i])]))
    return ascii_total, ascii_diff
