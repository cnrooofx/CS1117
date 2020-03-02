# Live Coding Class
# Mon 20/01/20


def all_pairs(s1=[], s2=[]):
    out = [-1]
    error = False
    try:
        out = [str(item1)+str(item2) for item1 in s1 for item2 in s2]
    except:
        error = True
    return error, out


def all_pairs(s1, s2):
    try:
        return False, [str(i) + str(x) for i in list(s1) for x in list(s2)]
    except:
        return True, [-1]


# print(all_pairs("abc", [1, 2, 3]))
# print(all_pairs("abcdef", [1, 2]))
# print(all_pairs([1, 2], "abc"))
# print(all_pairs([], ""))
# print(all_pairs(["a", "b"], 123))


def while_pairs(s1, s2):
    out = []
    error = False
    try:
        i = 0
        while i < len(s1):
            j = 0
            while j < len(s2):
                out.append(str(s1[i])+str(s2[j]))
                j += 1
            i += 1
    except:
        error = True
        out = [-1]
    return error, out


print(while_pairs("abc", [1, 2, 3]))
print(while_pairs("abcdef", [1, 2]))
print(while_pairs([1, 2], "abc"))
print(while_pairs([], ""))
print(while_pairs(["a", "b"], 123))
