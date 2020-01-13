# Script Name: what_is_my_name.py
# Author: Conor Fox 119322236

def what_is_my_name(question):
    '''
    Take input from user, cast to string and format to all lowercase then capitalise first letter.
    question: Question to be asked to user
    '''
    name = str(input(question))
    name = name.lower()
    name = name.capitalize()
    return name

first_name = what_is_my_name("What is your first name?")
last_name = what_is_my_name("What is your last name?")

print("Hello", first_name, last_name)
