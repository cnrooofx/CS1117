# Q1. # A function called dictionary_creator, which takes a list of input strings and
# splits the string into numbers and letters to return a dictionary
# # If two inputs return the same key, only the first is saved
# # Examples:
# # dictionary_creator(['15dhs', '12345zyx']                      -> {15: 'dhs', 12345: 'zyx'}
# # dictionary_creator(['415dhs', '12345zyx', '12abc', '12cde']   -> {415: 'dhs', 12345: 'zyx', 12: 'abc'}


# Q2. Write a function fibonacci_checker(l) that takes in a list l of numbers and
# checks if they are part of the fibonacci sequence.
# The output is a list of the numbers entered that are part of the fibonacci sequence.
# If the number is already in the output, it shouldn't repeat.
# # Example:
# # fibonacci_checker([1,2,3,4,5,6,7,3,4])  =  [1,2,3,5]


# Q3. Given a sentence s and a word w, create a function called inside(w, s)
# which returns True if the word w is a substring of any permutation of the individual words in s - else False.
# Note: your answer should be case-insensitive.
# # Examples:
# # 1) w = "head", s = "Racecars don't have headlights because the track is always lit." -> return True.
# # 2) w = "loud", s = "You would not believe your eyes if 10 million fireflies." -> return True
#           (swap the w and l in would - wloud).
# # 3) w = "sbeve", s = "She BElieVEd." -> return False.
# # 4) w = "/£$,)", s = "&(%&^ *,$)£!?/ (^*&) !£$%^&* #=" -> return True.


# Q4. Write a function called shuffle that takes in a playlist (parameter named playlist) and
# shuffles the songs.
# Output should be a list of strings that are all songs.
# Make sure that an error message is printed if the input is not a list of songs.
# # Example: - this is just one example, as the output will be randomly shuffled :)
# # shuffle(["Sorry", "White Invserion", "Bad Guy", "Gernade", "Mamma Mia", "Budapest", "1000 Miles", "Star Star"])
# # -> ['Gernade', 'Bad Guy', '1000 Miles', 'White Invserion', 'Mamma Mia', 'Star Star', 'Sorry', 'Budapest']
