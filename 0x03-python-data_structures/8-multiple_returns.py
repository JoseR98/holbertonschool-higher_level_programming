#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
        tuple_1 = length, first,
    else:
        length = len(sentence)
        first = None
        tuple_1 = length, first,
    return tuple_1
