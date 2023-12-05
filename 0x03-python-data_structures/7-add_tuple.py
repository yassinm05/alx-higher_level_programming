#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a > 0):
        n1 = tuple_a[0]
    else:
        n1 = 0
    if len(tuple_a) > 1:
        n2 = tuple_a[1]
    else:
        n2 = 0
    if len(tuple_b) > 0:
        m1 = tuple_b[0]
    else:
        m1 = 0
    if len(tuple_b) > 1:
        m2 = tuple_b[1]
    else:
        m2 = 0
    new_tuple = (n1 + m1, n2 + b2)
    return new_tuple
