# Script Name: functions.py
# Author: Conor Fox 119322236


# 1
def chooseLargest(a, b):
    # return list(map(max, zip(a, b)))
    return list(map(lambda x: x, map(max, zip(a, b))))


# 2
def read_draw():
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
    day_totals = [0] * len(courierData[0])
    for driver in courierData:
        for day, deliveries in enumerate(driver):
            day_totals[day] += deliveries
    return len([day for day in day_totals if day >= 1000])


def most_del(courierData):
    driver_max = 0
    driver_id = 0
    for driver, deliveries in enumerate(courierData):
        day_total = 0
        for day in deliveries:
            day_total += day
        if day_total > driver_max:
            driver_max = day_total
            driver_id = driver
    return driver_id


# 4
def append_list():
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]
    return list(map(lambda tup: tup[0]+tup[1], zip(list1, list2)))


# 5
def client_matcher(client):
    match = []
    file = open('clients.txt', 'r')
    clients = {person[0]: person[1:] for person in [
        line.strip('\n').split(',') for line in file.readlines()]}
    file.close()
    client_seek_gender = clients[client][2]
    client_gender = clients[client][0]
    client_seek_age = range(int(clients[client][3]), int(clients[client][4]))
    client_age = int(clients[client][1])
    for person in clients:
        seek_gender = clients[person][2]
        gender = clients[person][0]
        age_range = range(int(clients[person][3]), int(clients[person][4]))
        age = int(clients[person][1])
        if person == client:
            continue
        elif client_seek_gender == gender and seek_gender == client_gender:
            if age in client_seek_age and client_age in age_range:
                match += ['%s should meet %s' % (client, person)]
    return match
