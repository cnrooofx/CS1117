# Script Name: functions.py
# Author: Conor Fox 119322236


def to_english(n):
    answer = ""
    units_dictionary = {1: "one", 2: "two", 3: "three", 4: "four",
                        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens_dictionary = {11: "eleven", 12: "twelve", 13: "thirteen",
                        14: "fourteen", 15: "fifteen", 16: "sixteen",
                        17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens_dictionary = {1: "ten", 2: "twenty", 3: "thirty",
                       4: "forty", 5: "fifty", 6: "sixty", 7: "seventy",
                       8: "eighty", 9: "ninety"}
    if n == 0:
        return "Zero"
    elif n < 0:
        n *= -1
        answer = "Minus "
    if n // 100 != 0:
        hundreds = n // 100
        if n % 100 < 10 and n % 100 != 0:
            return (answer + units_dictionary[hundreds] + " hundred and "
                    + units_dictionary[n % 100]).capitalize()
        elif n % 100 == 0:
            return (answer + units_dictionary[hundreds]
                    + " hundred").capitalize()
        answer += units_dictionary[hundreds]+" hundred and "
    if (n % 100) > 10 and (n % 100) < 20:
        if answer == "":
            return (answer + teens_dictionary[n % 100]).capitalize()
        elif answer == "Minus ":
            return (answer + teens_dictionary[n % 100]).capitalize()
        return (answer + teens_dictionary[n % 100]).capitalize()
    if n % 100 < 10 and n not in units_dictionary:
        return (answer + " and " + units_dictionary[n % 10]).capitalize()
    elif n // 10 != 0:
        tens = (n % 100) // 10
        answer += tens_dictionary[tens]
    if n % 10 == 0:
        return answer.capitalize()
    if answer == "Minus ":
        return answer + units_dictionary[n % 10]
    elif answer != "":
        answer += " "
    answer += units_dictionary[n % 10]
    return answer.capitalize()


def sort_a_list(s):
    """
    Takes a list s and sorts it from smallest value to biggest value.
    s -- Input list
    return -- The sorted list
    """
    new_list = []
    for i in range(len(s)):
        smallest_val = min(s)
        if smallest_val not in new_list:
            smallest_val = min(s)
            new_list.append(smallest_val)
        s.remove(smallest_val)
    return new_list


def ascii_difference(m, n=[0]):
    ascii_table = {"!":33, "\"":34, "#":35, "$":36, "%":37, "&":38, "\'":39,
                   "(":40, ")":41, "*":42, "+":43, ",":44, "-":45, ".":46,
                   "/":47, "0":48, "1":49, "2":50, "3":51, "4":52, "5":53,
                   "6":54, "7":55, "8":56, "9":57, ":":58, ";":59, "<":60,
                   "=":61, ">":62, "?":63, 
                   }
    i = 0
    m_out = []
    n_out = []
    while i < len(m):
        print(m[i])
        i += 1
    return m_out, n_out
