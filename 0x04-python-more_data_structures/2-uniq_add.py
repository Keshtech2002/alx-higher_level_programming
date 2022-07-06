#!/usr/bin/python3

def uniq_add(my_list=[]):
    store = []
    for i in range(0, len(my_list)):
        if my_list[i] not in store:
            store.append(my_list[i])
    return sum(store)
