#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    MAX = my_list[0]
    for i in my_list:
        if i > MAX:
            MAX = i
    return MAX
