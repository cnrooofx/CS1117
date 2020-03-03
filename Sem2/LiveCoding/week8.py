# Live Coding Class
# Mon 24/02/20

# create a function called:
#   are_rotations(s1, s2)
# with 2 parameters called:
#   s1 - string
#   s2 - string
# which takes two string parameters and returns a Boolean stating whether or
# not one is a rotation of the other


def rotate(s, n):
    try:
        if n >= 0:
            return False, s[n:] + s[:n]
        else:
            return True, [-1]
    except:
        return True, [-1]


# def are_rotations(s1, s2):
#     try:
#         if len(s1) != len(s2):
#             return False, False
#         for i in range(len(s1)):
#             for j in range(len(s2)):
#                 if (s1[i:] + s2[:i]) == (s2[j:] + s2[:j]):
#                     return False, True
#         return False, False
#     except:
#         return True, [-1]


def are_rotations(s1, s2):
    try:
        if len(s1) != len(s2):
            return False, False
        for i in range(len(s1)):
            err, rotated_s2 = rotate(s2, i)
            if err:
                return True, [-1]
            elif s1 == rotated_s2:
                return False, True
        return False, False
    except:
        return True, [-1]


print(are_rotations("abcde", "cdeab"))  # -> (False, True)
print(are_rotations("abcde", "edcba"))  # -> (False, False)
print(are_rotations("abcde", "abc"))  # -> (False, False)
print(are_rotations("abaab", "aabab"))  # -> (False, True)

print()

print(are_rotations("abcde", "cdeab"))
print(are_rotations("abcde", "edcba"))
print(are_rotations("abcde", "abc"))
print(are_rotations("abaab", "aabab"))
print(are_rotations("abaab", "babaa"))
print(are_rotations("", ""))
print(are_rotations("ab", "ab"))
print(are_rotations("a", "ab"))


# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred
