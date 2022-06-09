#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = list(map(lambda key: key*2,a_dictionary))
    return new_dictionary
