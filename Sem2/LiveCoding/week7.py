# Live Coding Class
# Mon 24/02/20

# create a function called:
#   rotate(s, n)
# with 2 parameters called:
#   s - string
#   n - integer
# which takes a string s and an integer n, with 0 ≤ n < len(s), and returns a
# copy of s rotated by n places


def rotate(s, n):
    try:
        if n >= 0:
            return False, s[n:] + s[:n]
        else:
            return True, [-1]
    except:
        return True, [-1]


print(rotate("abcde", 1))  # -> (False, "bcdea")
print(rotate("abcde", 2))  # -> (False, "cdeab")
print(rotate("abcde", 0))  # -> (False, "abcde")
# print(rotate("Conor", 4))

# create a function called:
#   are_rotations(s1, s2)
# with 2 parameters called:
#   s1 - string
#   s2 - string
# which takes two string parameters and returns a Boolean stating whether or
# not one is a rotation of the other

# are_rotations("abcde", "cdeab") -> (False, True)
# are_rotations("abcde", "edcba") -> (False, False)
# are_rotations("abcde", "abc") -> (False, False)
# are_rotations("abaab", "aabab") -> (False, True)


# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred
