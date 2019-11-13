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
            return (answer + units_dictionary[hundreds] + " hundred and " + units_dictionary[n % 100]).capitalize()
        elif n % 100 == 0:
            return (answer + units_dictionary[hundreds] + " hundred").capitalize()
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
