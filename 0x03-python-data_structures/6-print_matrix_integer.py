#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(matrix) == 0:
            print()
        for j in i:
            print("{:d} ".format(j))
        print()
