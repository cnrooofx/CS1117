# Script Name: functions.py
# Author: Conor Fox 119322236
# Semester 2 - Continuous Assessment 2


def what_am_I(input_list, my_type='all'):
    try:
        out = {}
        if my_type != 'all' and isinstance(my_type, str):
            return out
        elif len(input_list) > 0:
            if my_type != 'all':
                my_type = str(my_type.__name__)
                for val in input_list:
                    if type(val).__name__ == my_type:
                        if my_type not in out:
                            out[my_type] = [val]
                        else:
                            out[my_type] += [val]
            else:
                for val in input_list:
                    my_type = type(val).__name__
                    if my_type not in out:
                        out[my_type] = [val]
                    else:
                        out[my_type] += [val]
        return out
    except:
        return 'Error'


def who_am_I(file_input):
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
        return 'Error'


def matrices(file_input):
    matrix = []
    with open(file_input, 'r') as my_file:
        for line in my_file.readlines():
            cur_line = []
            for num in line.strip('\n').split(','):
                num = num.strip()
                cur_line.append(int(num))
            matrix.append(cur_line)
    rev_matrix = []
    for i in range(len(matrix)):
        rev_matrix.append([])
    for row in matrix:
        for ind, val in enumerate(row):
            rev_matrix[ind].append(val)
    return rev_matrix


def sum_me(matrices_list):
    rows = [0 for i in range(len(matrices_list))]
    columns = [0 for i in range(len(matrices_list[0]))]
    for row_ind, row in enumerate(matrices_list):
        for col_ind, val in enumerate(row):
            rows[row_ind] += val
            columns[col_ind] += val
    return rows, columns
