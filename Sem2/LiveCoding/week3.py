# Live Coding Class
# Mon 03/02/20

def num_digits(s1):
    try:
        number = str(s1)
        negative = False
        if number[0:1] == "-":
            negative = True
            number = number[1:]
        if number[:2] == "0.":
            number = number[1:]
        length = len(number)
        if negative:
            length *= -1
        return False, length
    except:
        return True, [-1]


# create a function called:
#   num_digits(s1)
# with 1 parameters called:
#   s1 - integer/float number
# which determines how many digits are in the input number (including decimal place)
# adding a minus before the output if a negative number is passed in

print(num_digits(0))  # -> (False, 1)
print(num_digits(12345))  # -> (False, 5)
print(num_digits(12.3465))  # -> (False, 7)
print(num_digits(.012))  # -> (False, 4)
print(num_digits(-12.3454))  # -> (False, -7)
print(num_digits(-.012))  # -> (False, -4)
