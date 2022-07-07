#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete = []
    for k, v in my_dict.items():
        if v == value:
            delete.append(k)
    for x in delete:
        del my_dict[x]
    return(my_dict)
