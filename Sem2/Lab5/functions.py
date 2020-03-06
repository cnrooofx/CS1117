# Script Name: functions.py
# Author: Conor Fox 119322236


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

