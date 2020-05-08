#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0.0
    if my_list:
        sum_average = list(i * j for i, j in my_list)
        sum_total = 0
        for i, j in my_list:
            sum_total += j
        for i in sum_average:
            average += i
        average /= sum_total
    return average
