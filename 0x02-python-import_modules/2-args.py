#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    lenght = len(arg) - 1

    if lenght > 1:
        print("{} arguments: ".format(lenght))
        for a in range(1, lenght + 1):
            print("{}: {}".format(a, arg[a]))

    elif lenght == 0:
        print("{} arguments: ".format(lenght))

    else:
        print("{} argument: ".format(lenght))
        print("{}: {}".format(lenght, arg[1]))
