#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    a = len(my_list) - 1
    if idx < 0 and idx > a:
            return my_list
    else:
        my_list = my_list[0:idx] + my_list[idx:]
    return my_list
