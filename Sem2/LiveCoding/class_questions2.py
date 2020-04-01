import random

# Q1. A function called swaps() which takes 1 parameter - a_list.
# a_list contains two types of Python types
#
# The function returns a list such that for all values of the second type
# move to the index at which the next value of the same type appears.
# Finally, the last element of that type in the list takes the place of the first element of that type
#
# e.g.
# swaps([1,2,3,'a',4,5,'b',6,',c',7]) -> [1,2,3,'c',4,5,'a',6,'b',7]
# swaps([1,2.0,3,4.0,5,6.0]) -> [1,6.0,3,2.0,5,4.0]


def swaps(a_list):
    first_type = type(a_list[0])
    i = 0
    while type(a_list[i]) == first_type:
        i += 1
    else:
        second_type = type(a_list[i])
    for val, index in enumerate(a_list):
        print(val, index)
    print('first_type: ')
    print(first_type)
    print('second_type: ')
    print(second_type)
    return


print(swaps([1, 2, 3, 'a', 4, 5, 'b', 6, ',c', 7]))  # -> [1,2,3,'c',4,5,'a',6,'b',7]
print(swaps([1, 2.0, 3, 4.0, 5, 6.0]))  # -> [1,6.0,3,2.0,5,4.0]

# Q2. Given a list of 4096 unique numbers that occupy the 12-bit unsigned number space,
# return the largest number in the list in decimal. Fastest code wins.
# use this to generate your list of numbers


def randomList4096():
    out = [0]
    for i in range(1, 4095):
        out.insert(random.randint(0, i), i)
    return out


def unique_num(num_list):
    num_list.sort()
    return


num_list = randomList4096()
print(num_list)
# print(unique_num(num_list))

# Q3. Create a function called substrings(s) which returns all possible contiguous substrings of
# a string s.
# Note: Output is a list of strings.
#
# EXAMPLES:
# 1) "the" -> ["", "t", "h", "e", "th", "he", "the"]
# 2) "four" -> ["", "f", "o", "u", "r", "fo", "ou", "ur", "fou", "our", "four"]


def substrings(s):
    return

# Q4. The fibonacci sequence is one of the most well known sequences in mathematics.
# The sequence is defined such that the n-th term is equal to the sum of the two terms
# directly preceding it. The classic example uses the numbers 0 and 1 as its first and
# second terms to create the following infinite sequence 0,1,1,2,3,5,8,13,21,...
# but any two numbers denoted a and b can be used to begin the sequence.
# You are given a shuffled contiguous subsequence of a sequence which is
# defined in the same way as the classic fibonacci sequence - but has different
# starting numbers a and b.
# Find the smallest a + b which can start the given shuffled subsequence.
# Call your function findstart(lst).
#
# Notes: a, b > 0, return a, b.
#
# EXAMPLES:
# [13,5,8,21] -> (1,1)
# [1974, 466, 754, 288, 1220, 178] -> (2,2)
# [343, 2351, 1453, 555, 212, 898, 6155, 3804] -> (3, 2)
# [10569, 1542, 6532, 27670, 17101, 4037, 953, 2495] -> (5,1)


def findstart(lst):
    return
