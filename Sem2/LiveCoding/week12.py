# create a function called:
#   twenty_twenty(list1, list2)
# with 2 parameters called:
#   list1 (defaults to [1,2,7,5,6])
#   list2 (defaults to [1,2,5,6,7])
# which determines how similar these lists are (which I call the blurry-ness of the inputs)
# the function is not concerned with the order of the lists, or repetition in the list
# only how close the list are to each other (based on the uniqueness of the elements)
# returning the int 2020, if the lists are identical (20 for list1 and 20 for list2)


#
# twenty_twenty( ) -> 2020
# twenty_twenty( [1,2,7,5,6,'a'], ['a',1,2,5,6,7] ) -> 2020
#
# if not identical, for each list:
#   return the sum of the elements in the lists divided by the number of elements modulus 20
# again returning as an int
# twenty_twenty( [1,2,7,5,6], [1,3,5,8,7] ) -> 1212
