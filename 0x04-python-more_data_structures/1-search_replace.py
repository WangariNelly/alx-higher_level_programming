#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = ' '
    for name in range(0, len(my_list)):
        if(my_list[name] == "search"):
            new_list += "replace"
        else:
            new_list += my_list[name]
    print("New string :  ")
