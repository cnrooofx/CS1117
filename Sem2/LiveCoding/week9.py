# Live Coding Class
# Mon 09/03/20

# create a function called:
#   recursive_N(n)
# with 1 parameters called:
#   n - integer
#
# which sums the numbers from n to 0 recursively


def recursive_N(n):
    if n == 0:
        return n
    elif n < 1:
        return n + recursive_N(n+1)
    return n + recursive_N(n-1)


print(recursive_N(0))  # -> (False, 0)
print(recursive_N(-2))  # -> (False, -3)
print(recursive_N(200))  # -> (False, 3)


# create a function called:
#   sub_range(lo, hi)
# with 2 parameters called:
#   lo - integer
#   hi - integer
# which creates a list of integers from the integer ‘lo’ (inclusive) up to
# the integer ‘hi’ (exclusive). Write this function recursively.

# sub_range(3, 7) -> (False, [3, 4, 5, 6])
# sub_range(3, 4) -> (False, [3])
# sub_range(3, 3) -> (False, [])
# sub_range(3, 1) ->s (False, [])

# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred
