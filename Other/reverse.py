def slice_reverse(input_value):
    list(input_value)
    i = 0
    length = len(input_value)
    while i < len(input_value):
        if input_value[i] == input_value[len-i]:
            i += 1
        else:
