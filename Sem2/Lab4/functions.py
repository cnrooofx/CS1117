# Script Name: functions.py
# Author: Conor Fox 119322236

# 1
def chooseLargest(a, b):
    # return list(map(max, zip(a, b)))
    return list(map(lambda x: x, map(max, zip(a, b))))


# 2
def lottery():
    file = open('lotteryNumbers.txt', 'r')
    lottery_list = []
    for line in file.readlines():
        line = line.strip('\n').split(' ')
        current_draw = []
        for number in line:
            current_draw.append(int(number))
        lottery_list.append(current_draw)
    file.close()
    return lottery_list


# 3
def onek_deliveries(courierData):
    day_totals = []
    for driver in courierData:
        for day, deliveries in enumerate(driver):
            if day not in range(len(day_totals)):
                day_totals.append(0)
            day_totals[day] += deliveries
    onek_days = 0
    for day in day_totals:
        if day >= 1000:
            onek_days += 1
    return onek_days


def most_deliveries(courierData):
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


#4
def totals(list1, list2):
    return list(map(lambda tup: tup[0]+tup[1], zip(list1, list2)))
