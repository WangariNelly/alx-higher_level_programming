def uniq_add(my_list=[]):
    unique_list = []
    for number in my_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list
