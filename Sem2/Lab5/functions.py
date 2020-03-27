# Script Name: functions.py
# Author: Conor Fox 119322236

import random
import string


# 1
def factorialL(n):
    if n == 1:
        return 1
    else:
        return n * factorialL(n-1)


# 2
def hailStoneR(n):
    current_num = [n]
    if n == 1:
        return [1]
    elif n % 2 == 0:
        n //= 2
    else:
        n = (3 * n + 1)
    return current_num + hailStoneR(n)


# 3
def chooseLargest(a, b):
    results = []
    list_len = len(a)
    for i in range(list_len):
        results.append(max(a[i], b[i]))
    print(results)


def chooseLargest(a, b):
    return [max(a[i], b[i]) for i in range(len(a))]


def chooseLargest(a, b):
    return list(map(lambda x: max(x), zip(a, b)))


# 4
def redact():
    try:
        # Create a list of the sensitive words from the file
        sensitive = open('sensitiveWords.txt', 'r')
        words = [word.strip('\n').lower() for word in sensitive.readlines()]
        sensitive.close()
        # Create file to write redacted text to
        out = open('redacted.txt', 'w')
        to_redact = open('unredacted.txt', 'r')
        # Loop through every line in the file to redact
        for line in to_redact.readlines():
            # Create a new line to write into the new file
            current_line = ''
            # Loop through every word in the line
            for word in line.split():
                # Check to see if it's a sensitive word
                if word.lower() in words:
                    # Replace with the same amount of asterixes as the length
                    current_line += (('*' * len(word)) + ' ')
                else:
                    # Otherwise just add the word
                    current_line += (word + ' ')
            # After every line, write it to the redacted file.
            out.write(current_line + '\n')
        out.close()
        to_redact.close()
    except IOError:
        return "Error! File 'unredacted.txt' or 'sensitiveWords.txt' not found"


# 5

# x = list(map(lambda n1, n2: n1 - n2, [7, 8, 9], [3, 2, 1]))
# print(x)
"""
 -  Map is taking the two lists and passing them as parameters n1, n2 to the
    lambda function.

 -  Map will iterate over the lists passing the values at the same index in
    each list.

 -  The lambda function takes the list items passed from map and subtracts
    the item in the first list n1 from the item in the second list n2 and
    returns the answer.

 -  The output from the lambda function is saved in the map object which is
    converted into a list which is then printed.
"""


# 6
def sum_it():
    summation = []
    for n in range(17):
        if n > 10:
            summation.append(n)
    return summation


# 7
def createDeck():
    deck = []
    cards = [str(num) for num in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    for suit in ['s', 'h', 'd', 'c']:
        for card in cards:
            deck.append(card+suit)
    return deck


def shuffle(deck):
    for card in deck:
        swap_index = random.randint(1, len(deck))
        deck.pop(deck.index(card))
        deck = deck[:swap_index] + [card] + deck[swap_index:]
    return deck


# 8
def word_count():
    try:
        book = open('book.txt', 'r')
        # Dictionary to keep track of word counts
        wc = {}
        # Loop through every line in the book
        for line in book.readlines():
            # Break up each line by word
            for word in line.strip('\n').split():
                # Filter out the punctuation
                word = ''.join(l for l in word if l not in string.punctuation)
                # Make it lowercase to be consistent
                word = word.lower()
                # If the word is not already in the dictionary, initialise it
                if word not in wc:
                    wc[word] = 1
                else:
                    # Otherwise increment the counter for that word
                    wc[word] += 1
        # Counter for the most amount of occurrences
        most = 0
        # That word which appears most often
        most_word = ''
        # Loop through the counter dictionary
        for key in wc:
            # Compare that counter to the current highest value
            if wc[key] > most:
                # Assign that total to be the new highest value found
                most = wc[key]
                # Save that word with the highest total
                most_word = key
        book.close()
        return most_word
    except IOError:
        return "Error! File 'book.txt' not found."
