# Is there a bug here (Y/N):
# hat is the output?
# add the code here


def separated_input(string1, string2, my_sep, my_end):
    print(str(string1)+" ", str(string2)+" ", sep=str(my_sep)+" ", end=str(my_end))


separated_input("A", "B", my_sep=" and", my_end="and C\n")
separated_input("A", "B", my_end="and C\n", my_sep=" and")
separated_input("A", "B", my_end="and C\n", my_sep=" and")
separated_input("A", "B", my_sep=" and", my_end="and C\n")
separated_input("A", "B", my_end="and C\n", my_sep=" and")
separated_input("A", "B", my_sep=" and", my_end="and C\n")
separated_input("8", "7", my_sep=" +", my_end="= 15\n")
separated_input(8, 7, my_sep="+", my_end="= 15\n")
separated_input(8, 7, my_sep=" +", my_end="= 15\n")
separated_input(8, 7, my_sep=" +", my_end="= 15"+"\n")

'''

#Is there a bug here (Y/N):Y
#What is the output?

# add the code here
seperated_input("A", "B", my_sep=" and ", my_end="and C\n")
seperated_input("A", "B", my_end="and C\n", my_sep=" and ")
seperated_input("A", my_end="and C\n", my_sep=" and ", "B")
seperated_input("A", "B", my_sep=" and ")
seperated_input("A", "B", my_end=" and C\n")
seperated_input("A", "B", "C", my_sep=" and ", my_end=" and C\n")
seperated_input("8", "7", my_sep=" + ", my_end=" = 15\n")
seperated_input(8, 7, my_sep= +, my_end=" = 15\n")
seperated_input(8, 7, my_sep=" + ", my_end=15)
seperated_input(8, 7, my_sep=" + ", my_end=" = 15"+"\n")

'''
