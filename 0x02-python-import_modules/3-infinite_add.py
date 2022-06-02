#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addition = 0
    for add in argv[1:]:
        addition += int(add)
    print("{:d}".format(addition))
