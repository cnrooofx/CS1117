# Script Name: functions.py
# Author: Conor Fox 119322236
# Semester 2 - Continuous Assessment 2


def what_am_I(input_list, my_type='all'):
    """Creates a dictionary from items in a list by type

    :param input_list: list of various Python types
    :param my_type: Python type to filter by (Default value = 'all')
    :returns: dictionary with the types of the list elements as keys
    """
    try:
        out = {}
        # If the my_type is a string and isn't all, return an empty dictionary
        if my_type != 'all' and isinstance(my_type, str):
            return out
        elif len(input_list) > 0:
            if my_type == 'all':
                all = True
            else:
                # If my_type isn't all, add that type to the dictionary
                out[str(my_type.__name__)] = []
                # Set all to False, stops other types being added to dictionary
                all = False
            for val in input_list:
                # Get the type of the current item in the list
                my_type = type(val).__name__
                # If the type is already in the dictionary, add it to that list
                if my_type in out:
                    out[my_type] += [val]
                # Only add other types to the dictionary if all is set to True
                elif all:
                    out[my_type] = [val]
        return out
    except:
        return 'Oops, there was an error in what_am_I'


def who_am_I(file_input):
    """Creates a dictionary from items in a file by type

    :param file_input: name of file containing lists of various Python types
    :returns: dictionary with the types of the list elements as keys
    """
    try:
        my_file = open(file_input, 'r')
        type_list = []
        for line in my_file.readlines():
            for word in line.strip('\n').strip('[').strip(']').split(','):
                word = word.strip()
                if word == 'True':
                    type_list.append(True)
                elif word == 'False':
                    type_list.append(False)
                elif (word[0] == '\'' and word[-1] == '\'') or \
                     (word[0] == '\"' and word[-1] == '\"'):
                    type_list.append(word.strip('\'').strip('\"'))
                elif '.' in word:
                    type_list.append(float(word))
                else:
                    type_list.append(int(word))
        return what_am_I(type_list, my_type='all')
    except:
        return 'Oops, there was an error in who_am_I'


def matrices(file_input):
    """Creates a matrix taking input from a file

    :param file_input: name of file containing the matrix
    :returns: matrix (list of lists) from the file
    """
    try:
        matrix = []
        # Read the file and create the matrix from it
        with open(file_input, 'r') as my_file:
            for line in my_file.readlines():
                cur_line = []
                for num in line.strip('\n').split(','):
                    num = num.strip()
                    cur_line.append(int(num))
                matrix.append(cur_line)
        # Create an empty matrix to be the reversed version
        rev_matrix = [[] for i in range(len(matrix))]
        for row in matrix:
            # Get the index and value in each row
            for ind, val in enumerate(row):
                # Add value to the column at that index in the reversed matrix
                rev_matrix[ind].append(val)
        return rev_matrix
    except:
        return 'Oops, there was an error in matrices'


def sum_me(matrices_list):
    """Sums up rows and columns in a matrix

    :param matrices_list: matrix (list of lists)
    :returns: tuple with the sum of all the rows and the sum of all the columns
    """
    try:
        # Create lists to sum up the values
        rows = [0 for i in range(len(matrices_list[0]))]
        columns = [0 for i in range(len(matrices_list))]
        # Get the index of every row
        for row_index, row in enumerate(matrices_list):
            # Get the index of every value in each row
            for col_index, val in enumerate(row):
                # Add the value to the current row index in the sum list
                rows[row_index] += val
                # Add the value to the current column index in the sum list
                columns[col_index] += val
        return rows, columns
    except:
        return 'Oops, there was an error in sum_me'
