#!/usr/bin/python3
import numpy


def new_in_list(my_list, idx, element):
    if ((idx < 0) or idx > (len(my_list) - 1)):
        return(my_list)
    else:
        new = [num for num in my_list]
        new[idx] = element
        return(new)
    