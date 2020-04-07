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
