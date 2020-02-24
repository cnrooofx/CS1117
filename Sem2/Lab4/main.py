# Script Name: main.py
# Author: Conor Fox 119322236

import functions


def main():
    courierData = [[87, 83, 86, 88, 83], [99, 99, 85, 85, 81],
                   [92, 25000, 80, 84, 88], [83, 90, 93, 98, 2000],
                   [81, 98, 80, 82, 80], [95, 95, 98, 84, 80],
                   [100, 89, 86, 91, 90], [95, 89, 94, 95, 86],
                   [88, 83, 92, 81, 83], [92, 99, 96, 94, 200]]
    # l1 = [1, 2, 3, 4, 5]
    # l2 = [2, 2, 9, 0, 9]
    # print(functions.chooseLargest(l1, l2))
    # print(functions.read_draw())
    print(functions.read_draw())
    # print(functions.onek_deliveries(courierData))
    # print(functions.most_deliveries(courierData))
    # print(functions.append_list())
    print(functions.client_matcher('Alison Jones'))


if __name__ == "__main__":
    main()
