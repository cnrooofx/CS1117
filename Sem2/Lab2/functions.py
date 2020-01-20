# Script Name: functions.py
# Author: Conor Fox 119322236


# 1
def power():
    return [i*i for i in range(1, 6) if i % 2 == 0]


# 2
def F(s1, s2):
    r = []
    i = 0
    while i < len(s1):
        j = 0
        while j < len(s2):
            if s1[i] == s2[j]:
                r += [s1[i]]
                break
            j += 1
        i += 1
    return r


# 3 (a)
def reducedFeeEntitlement(d):
    return [student for student in d if len(d[student]) < 2]


# 3 (b)
def commonModules(d, s1, s2):
    return [module1 for module1 in d[s1] for module2 in d[s2] if module1 == module2]


# 4
def iter_factorial(n):
    i = n
    ans = 1
    while i > 0:
        ans *= i
        i -= 1
    return ans


# 5
def fizz_buzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
