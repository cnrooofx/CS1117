# Script Name: functions.py
# Author: Conor Fox 119322236

# 1


def chooseLargest(a, b):
    return list(map(lambda x: x, map(max, zip(a, b))))

