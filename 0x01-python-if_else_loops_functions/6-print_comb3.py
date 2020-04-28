#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first != second and first == 0:
            print("{:d}{:d}".format(first, second), end=", ")
        elif first != 0 and second > first and first != 8:
            print("{:d}{:d}".format(first, second), end=", ")
        elif second > first:
            print("{:d}{:d}".format(first, second))
