#!/usr/bin/python3

def no_c(my_string):
    no_of_chars = len(my_string)
    new_string = ""
    i = 0
    for i in range(0, no_of_chars):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        new_string = new_string + my_string[i]
    return new_string
