def slice_reverse(input_value):
    input_value = str(input_value)
    i = 0
    length = len(input_value)
    while i < len(input_value):
        if input_value[i] == input_value[(length-1)-i]:
            i += 1


slice_reverse(123454321)
