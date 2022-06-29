#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        keep = number * -1
    else:
        keep = number

    lastDigit = keep % 10
    print("{}".format(lastDigit))
    return lastDigit
