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
    start = [n]
    if n == 1:
        return [1]
    elif n % 2 == 0:
        n //= 2
    else:
        n = (3 * n + 1)
    return start + hailStoneR(n)


# 3
def chooseLargest(a, b):
    results = []
    list_len = len(a)
    for i in range(list_len):
        results.append(max(a[i], b[i]))
    print(results)


def chooseLargest_comp(a, b):
    return [max(a[i], b[i]) for i in range(len(a))]


def chooseLargest_lambda(a, b):
    return list(map(lambda x: max(x), zip(a, b)))


# 4
def redact():
    sensitive_words = open('sensitiveWords.txt', 'r')
    words = [word.strip('\n').lower() for word in sensitive_words.readlines()]
    sensitive_words.close()
    out = open('redacted.txt', 'w')
    to_redact = open('unredacted.txt', 'r')
    for line in to_redact.readlines():
        current_line = ''
        for word in line.split():
            if word.lower() in words:
                current_line += (('*' * len(word)) + ' ')
            else:
                current_line += (word + ' ')
        out.write(current_line + '\n')
    print(words)
    out.close()
    to_redact.close()


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
    book = open('book.txt', 'r')
    wc = {}
    for line in book.readlines():
        for word in line.strip('\n').split():
            word = ''.join(l for l in word if l not in string.punctuation)
            word = word.lower()
            if word not in wc:
                wc[word] = 1
            else:
                wc[word] += 1
    most = 0
    most_word = ''
    for key in wc:
        if wc[key] > most:
            most = wc[key]
            most_word = key
    return most_word, most
