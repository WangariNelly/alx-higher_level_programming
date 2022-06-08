#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [name if name != search else replace for name in my_list]
    return(new_list)
    