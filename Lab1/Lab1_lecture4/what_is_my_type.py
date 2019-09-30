# Script Name: what_is_my_type.py
# Author: Conor Fox 119322236


def what_is_my_type(inputValue):
    '''
    Takes an input, finds both type and id and returns them
    :param inputValue: Takes a value to find the id and type
    :return: Returns the type and id of the inputted value

    '''
    what_type = type(inputValue)
    what_id = id(inputValue)
    return inputValue, what_type, what_id

# This is the value to find the type and id
input_Value = "7"

# Assign the 3 outputs from the function to variables
inputValue, what_type, what_id = what_is_my_type(input_Value)

# Print the
print("The value", "\"", inputValue, "\"", "is type", what_type, "and has the id", what_id)

'''
what_is_my_type = 2019
what_type = type(what_is_my_type)
whatID = id(what_is_my_type)
print("Variable", "\"", what_is_my_type, "\"", "is", what_type)

what_is_my_type = 29.99
what_type = type(what_is_my_type)
print("Variable", "\"", what_is_my_type, "\"", "is", what_type)

what_is_my_type = "Hello my name is Conor"
what_type = type(what_is_my_type)
print("Variable", "\"", what_is_my_type, "\"", "is", what_type)

what_is_my_type = ("alpha", "beta", "gamma")
what_type = type(what_is_my_type)
print("Variable", "\"", what_is_my_type, "\"", "is", what_type)
'''
