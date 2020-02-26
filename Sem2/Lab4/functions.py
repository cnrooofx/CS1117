# Script Name: functions.py
# Author: Conor Fox 119322236


# 1
def chooseLargest(a, b):
    return list(map(lambda x: max(x), zip(a, b)))


# 2
def read_draw():
    """Reads lottery numbers from a file and creates a list for every draw.

    return -- List of lottery draw lists
    """
    file = open('lotteryNumbers.txt', 'r')
    lottery_list = [[int(number) for number in line.strip(
        '\n').split(' ')] for line in file.readlines()]
    # for line in file.readlines():
    #     line = line.strip('\n').split(' ')
    #     current_draw = []
    #     for number in line:
    #         current_draw.append(int(number))
    #     lottery_list.append(current_draw)
    file.close()
    return lottery_list


# 3
def del_1000(courierData):
    """Calculates total number of days with at least 1000 deliveries

    courierData -- Table of delivery data, drivers as rows and days as columns
    return -- Number of days with at least 1000 deliveries
    """
    # Create a list with a counter for each day in the table
    day_totals = [0] * len(courierData[0])
    for driver in courierData:
        # Loop through each row, adding the deliveries to that days counter
        for day, deliveries in enumerate(driver):
            day_totals[day] += deliveries
    # Make a list of days with at least 1k deliveries, the length is the total
    return len([day for day in day_totals if day >= 1000])


def most_del(courierData):
    """Finds the number of the driver with the most deliveries in the week

    courierData -- Table of delivery data, drivers as rows and days as columns
    return -- Driver id number with most deliveries for the week
    """
    # The driver with the highest total deliveries for comparison
    driver_max = 0
    # The id number of that driver
    driver_id = 0
    for driver, deliveries in enumerate(courierData):
        # Loop through each driver adding up the deliveries for the week
        day_total = 0
        for day in deliveries:
            day_total += day
        # If that driver has more than the previous highest total
        if day_total > driver_max:
            # Reassign that total as the new highest value
            driver_max = day_total
            # Save the id number of the driver
            driver_id = driver
    return driver_id


# 4
def append_list():
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]
    return list(map(lambda tup: tup[0]+tup[1], zip(list1, list2)))


# 5
def client_matcher(client):
    """Reads client data from a file and finds matches for the selected client

    client -- String, Client name for find matches for
    return -- List of mutual matches for the client
    """
    match = []
    file = open('clients.txt', 'r')
    # Create a dictionary from the input file with client names as keys
    clients = {person[0]: person[1:] for person in [
        line.strip('\n').split(',') for line in file.readlines()]}
    file.close()
    # The gender that the client is looking for
    client_seek_gender = clients[client][2]
    # The clients gender
    client_gender = clients[client][0]
    # The age range that the client is looking for
    client_seek_age = range(int(clients[client][3]), int(clients[client][4]))
    # The clients age
    client_age = int(clients[client][1])
    for person in clients:
        if person != client:
            # The gender that the current person is looking for
            seek_gender = clients[person][2]
            # The gender of the current person
            gender = clients[person][0]
            # The age range that the current person is looking for
            age_range = range(int(clients[person][3]), int(clients[person][4]))
            # The age of the current person
            age = int(clients[person][1])
            # Check if the required genders of both people match
            if client_seek_gender == gender and seek_gender == client_gender:
                # Check if both people are in each others age ranges
                if age in client_seek_age and client_age in age_range:
                    # If they match, add an entry to the list
                    match += ['%s should meet %s' % (client, person)]
    return match
