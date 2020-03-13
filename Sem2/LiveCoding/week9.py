# Live Coding Class
# Mon 09/03/20

# create a function called:
#   recursive_N(n)
# with 1 parameters called:
#   n - integer
#
# which sums the numbers from n to 0 recursively


def recursive_N(n, extra=0):
    try:
        if n == 0:
            return False, n
        if n < extra:
            error, ans = recursive_N(n+1)
        else:
            error, ans = recursive_N(n-1)
        if error:
            return True, [-1]
        return False, n + ans
    except:
        return True, [-1]


print(recursive_N(0))  # -> (False, 0)
print(recursive_N(-2))  # -> (False, -3)
print(recursive_N(200))  # -> (False, 3)

print(recursive_N(1, 5))  # -> (False, 0)
print(recursive_N(5, 1))  # -> (False, -3)


# create a function called:
#   sub_range(lo, hi)
# with 2 parameters called:
#   lo - integer
#   hi - integer
# which creates a list of integers from the integer ‘lo’ (inclusive) up to
# the integer ‘hi’ (exclusive). Write this function recursively.


def sub_range(lo, hi):
    try:
        if lo >= hi:
            return False, []
        error, ans = sub_range(lo+1, hi)
        if error:
            return True, [-1]
        return False, [lo] + ans
    except:
        return True, [-1]


# print(sub_range(3, 7))  # -> (False, [3, 4, 5, 6])
# print(sub_range(3, 4))  # -> (False, [3])
# print(sub_range(3, 3))  # -> (False, [])
# print(sub_range(3, 1))  # -> (False, [])

# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred

###### EXTRA QUESTIONS ######
# change sub_range(lo, hi) to take hi,lo and lo,hi...
# easiest way possible, 2 lines of code...

# change recursive_N(n) to sum a range, without changing the strcuture of the function...
