#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{}{:d}".format("0" if number < 10 else "", number), end=", ")
    else:
        print("{:d}".format(number))
