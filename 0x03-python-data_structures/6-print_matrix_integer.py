#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat_ints in matrix:
        print(" ".join("{:d}".format(m) for m in mat_ints))
    