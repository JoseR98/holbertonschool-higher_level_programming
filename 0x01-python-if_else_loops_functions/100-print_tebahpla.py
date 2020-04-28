#!/usr/bin/python3
range_1 = range(97, 123)
range_r = reversed(range_1)
for letter in range_r:
    print("{}\
".format(chr(letter) if letter % 2 == 0 else chr(letter - 32)), end="")
