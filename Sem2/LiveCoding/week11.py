# this week we will use a Python dictionary to implement a regular
# language-to-language dictionary. For example, a ( very short )
# English-to-Irish dictionary could be implemented in Python as:
# { "sun":"grian", "water":"uisce", "horse":"capall", "tree":"crann" }

# create a function called:
#   read_dictionary( filename )
# with 1 parameters called:
#   filename - string name of file
# which will read the file ‘filename’, which should contain two words per line,
# and return a dictionary with the first words as keys and the corresponding
# second words as values


def read_dictionary(filename):
    filename = open('week11.txt', 'r')
    out_dict = {}
    for line in filename.readlines():
        words = line.strip('\n').split()
        out_dict[words[0]] = words[1]
    return out_dict


# print(read_dictionary('week11.txt'))
lang_dict = read_dictionary('week11.txt')

# create a function called:
#   inverse( d )
# with 1 parameters called:
#   d - dictionary
# which returns a copy of the dictionary ‘d’ but with keys and values interchanged.
# For example, calling ‘Inverse’ on the above English-to-Irish dictionary
# should produce the equivalent Irish-to-English dictionary:
# { "uisce":"water", "crann":"tree", "grian":"sun", "capall":"horse" }


def inverse(d):
    dict_copy = {}
    for key in d:
        dict_copy[d[key]] = key
    return dict_copy


print(inverse(lang_dict))

# create a function called:
#   print_dictionary( d )
# with 1 parameters called:
#   d - dictionary
# which prints the output the dictionary ‘d’, sorted alphabetically by keys,
# with one key-value pair per line, formatted as left-justified columns of width 10.

# For example, the above dictionary should be output as:
#       horse     : capall
#       sun       : grian
#       tree      : crann
#       water     : uisce
