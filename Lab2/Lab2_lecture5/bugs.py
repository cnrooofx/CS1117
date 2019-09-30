'''
If I leave my house at 6:52am and run 1 mile at an easy pace (8:15 minutes  [8 minutesand 15 seconds] per mile),
then 3 miles at tempo (7:12m per mile) and 1 mile at an easy pace again, what time do i get home for breakfast?
'''

departure_time_hours = 6
departure_time_minutes = 52
departure_time_seconds = (departure_time_hours * 3600) + (departure_time_minutes * 60)

easy_pace_mins = 8
easy_pace_secs = 15
easy_pace_total_sec = (easy_pace_mins * 60) + easy_pace_secs

faster_pace_mins = 7
faster_pace_secs = 12
faster_pace_total_sec = (faster_pace_mins * 60) + faster_pace_secs

# 2 miles at easy pace and 3 miles at faster pace = total time running
time_spent_running = (easy_pace_total_sec * 2) + (faster_pace_total_sec * 3)

# departure time and total time running = time back home
time_return_home_total_secs = departure_time_seconds + time_spent_running

# total seconds int divided by 3600 seconds in an hour = hours
time_return_home_hours = time_return_home_total_secs // 3600

# modulus of the hours divided by 60 = minutes
time_return_home_mins = (time_return_home_total_secs % 3600) // 60

# modulus of the hours and minutes = seconds
time_return_home_secs = (time_return_home_total_secs % 3600) % 60

print(time_return_home_hours, ":", time_return_home_mins, ":", time_return_home_secs,  "(HH:MM:SS)")

# answer: 07:30:06 (HH:MM:SS)
