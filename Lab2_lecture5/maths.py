#  Script Name : maths.py
#  Author: Conor Fox 119322236


def seconds_calculator(minutes, seconds):
    """
    Converts minutes and seconds into total number of minutes.
    minutes -- number of minutes
    seconds -- number of seconds

    returns value as total_seconds
    """
    total_seconds = ((int(minutes) * 60) + int(seconds))
    print("There are " + str(total_seconds) + " seconds in " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
    return total_seconds


def km_to_miles(kilometres):
    """
    Converts input in kilometres to miles
    kilometres -- distance in kilometres

    returns value as miles
    """
    miles = (kilometres / 1.6)
    print(str(kilometres) + " kilometres is " + str(miles) + " miles.")
    return miles


def average_pace(distance, time_minutes, time_seconds):
    """
    Takes distance and time and converts into average pace in
    """
    # print("Average pace for 10km race in 42m 42s")
    miles = (int(distance) / 1.6)
    # miles per second - distance/total_seconds
    # miles per minute
    total_minutes = (time_minutes) + (time_seconds / 60)

    pace = total_minutes/miles

    print("Pace is %6.6s minutes per mile." % (pace))

    return pace


def average_speed(distance, time_minutes, time_seconds):
    """
    Takes distance and time and converts into average speed in km/h.

    """
    total_seconds = total_seconds = ((int(time_minutes) * 60) + int(time_seconds))
    miles = (int(distance) / 1.6)
    # miles per second - distance/total_seconds
    # miles per minute
    total_hours = total_seconds / 3600
    speed = miles/total_hours

    print("Average speed is %6.6s miles per hour" % speed)

    return speed


def main():
    seconds_calculator(42, 42)
    km_to_miles(10)
    average_pace(10, 42, 42)
    average_speed(10, 42, 42)


if __name__ == '__main__':
    main()
