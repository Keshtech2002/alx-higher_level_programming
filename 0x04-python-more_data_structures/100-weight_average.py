#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    add = 0
    freq = 0
    for a, b in my_list:
        add += a * b
        freq += b
    return (add / freq)
