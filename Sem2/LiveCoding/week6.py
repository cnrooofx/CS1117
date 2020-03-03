# Live Coding Class
# Mon 17/02/20

# create a function called:
#   repeat( a_list, n )
# with 2 parameters called:
#   a_list - list
#   n - number
# which takes a list of integers and a positive integer n, and returns a copy of list
# with each element replicated n times.

# repeat([2,1,3], 4) -> (False, [2,2,2,2,1,1,1,1,3,3,3,3])


# create a function called:
#   self_repeat( a_list )
# with 1 parameters called:
#   a_list - list
# which takes a list of integers, and returns a copy of list in which each
# positive element n is replicated n times, and each non-positive element is
# removed

# SelfRepeat([2,1,3]) -> (False, [2,2,1,3,3,3])
# SelfRepeat([2,-4,1,0,3]) -> (False, [2,2,1,3,3,3])
# SelfRepeat([ ]) -> (False, [ ])


# all functions return two values:
# the first is a boolean to tell if an exception occurred
# the second is output of the function, if no exception occurred, or [-1]
# if an exception occurred


def repeat(a_list, n):
    error = False
    list_copy = []
    try:
        list_copy = [val for val in a_list for _ in range(n)]
    except:
        error = True
        list_copy = [-1]
    return error, list_copy


def self_repeat(a_list):
    error = False
    new_list = []
    for number in a_list:
        error, repeated = repeat([number], number)
        if not error:
            new_list += repeated
        else:
            return error, [-1]
    return error, new_list


# def repeated(a_list):




print(self_repeat([2, 1, 3]))
# print(repeat(["a", "b", "c"], 4))
# print(repeat([1,2,3], 2))
