#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    Addition = 0
    i = 1 
    while i < len(argv):
        Addition += int(argv[i])
        i += 1
    print("{:d}".format(Addition))
