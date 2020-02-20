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
    for person in clients:
        gender = clients[person][0]
        seek_gender = clients[client][2]
        age = range(int(clients[person][3]), int(clients[person][4]))
        seek_age = range(int(clients[client][3]), int(clients[client][4]))
        if person == client:
            continue
        elif gender == seek_gender and age in seek_age:
            match += person
            print(person, clients[person][0], client, clients[client][2])
    return match
