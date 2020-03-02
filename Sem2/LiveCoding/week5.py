# Live Coding Class
# Mon 10/02/20

# create a function called:
#   is_subsequence( s1, s2 )
# with 2 parameters called:
#   s1 - string
#   s2 - string
# which takes two sequence parameters and returns a Boolean stating whether or
# not all the elements of S1 also occur in S2, in the same order but not
# necessarily side-by-side

# is_subsequence( "abc", "abcde" ) -> (False, True)
# is_subsequence( "bce", "abcde" ) -> (False, True)
# IsSubsequence( "bec", "abcde" ) -> (False, False)
# IsSubsequence( "bfe", "abcde" ) -> (False, False)
# IsSubsequence( "b", "abcde" ) -> (False, True)
# IsSubsequence( "", "abcde" ) -> (False, True)

# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred


def is_subsequence(s1, s2):
    out = False
    error = False
    indexes = []
    sorted_list = []
    try:
        if s1 in s2:
            out = True
        else:
            for letter in s1:
                if letter not in s2:
                    break
                indexes.append(s2.index(letter))
                sorted_list.append(s2.index(letter))
            else:
                sorted_list.sort()
                if indexes == sorted_list:
                    out = True

    except:
        error = True
    return error, out, indexes


# print(is_subsequence('', 'abcde'))

print(is_subsequence("abc", "abcde"))  # -> (False, True)
print(is_subsequence("bce", "abcde"))  # -> (False, True)
print(is_subsequence("bec", "abcde"))  # -> (False, False)
print(is_subsequence("bfe", "abcde"))  # -> (False, False)
print(is_subsequence("b", "abcde"))  # -> (False, True)
print(is_subsequence("", "abcde"))  # -> (False, True)
