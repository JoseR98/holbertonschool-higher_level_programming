#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    # dir function shows all the available attributes of the module
    for n in dir(hidden_4):
        # print only names that doesn´t start with '_'
        if n[0] != '_':
            print("{}".format(n))
