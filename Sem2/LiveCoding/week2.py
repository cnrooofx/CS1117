# Live Coding Class
# Mon 27/01/20


def peaks(numlist):
    try:
        if len(numlist) == 0:
            return False, []
        out = [numlist[0]]
        for element in numlist:
            if element > max(out):
                out.append(element)
        return False, out
    except:
        return True, [-1]


# print(peaks([2, 5, 7, "a", 9, 1]))
# print(peaks([3]))
# print(peaks([]))

print(peaks([3, 2, 5, 5, 7, 6, 1, 8, 4]))  # -> (False, [3,5,7,8])
print(peaks([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # -> (False, [1,2,3,4,5,6,7,8,9])
print(peaks([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # -> (False, [9])
print(peaks([5, 5, 5, 5, 5, 5, 5, 5, 5]))  # -> (False, [5])
print(peaks([3]))  # -> (False, [3])
print(peaks([]))  # -> (False, [])
