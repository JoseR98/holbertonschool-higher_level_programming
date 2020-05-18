#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    i = 0
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            div_list.append(div)
        except ZeroDivisionError:
            div = 0
            div_list.append(div)
            print("division by 0")
        except TypeError:
            div = 0
            div_list.append(div)
            print("wrong type")
        except IndexError:
            div = 0
            div_list.append(div)
            print("out of range")
        i += 1
    return div_list
