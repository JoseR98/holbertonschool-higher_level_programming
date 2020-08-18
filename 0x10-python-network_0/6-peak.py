#!/usr/bin/python3
"""Contains function to find a peak inside a list"""


def find_peak(list_of_integers):
    """Find peak inside a list of integers"""
    if list_of_integers == []:
        return None
    peak = list_of_integers[0]
    max_p = 0
    left_val = peak
    right_val = 0
    item = 0
    peaks = []
    while item < len(list_of_integers) - 1:
        peak = list_of_integers[item]
        try:
            if left_val < peak and list_of_integers[item + 1] < peak:
                if max_p < peak:
                    max_p = peak
            elif left_val == peak and item != 0:
                max_p = peak
        except Exception as out_range:
            pass
        left_val = peak
        item += 1
    return max_p
