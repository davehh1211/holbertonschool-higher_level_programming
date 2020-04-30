#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    m = len(sys.argv)
    if m == 1:
        print("{} arguments.".format(m - 1))
    elif m >= 3:
        print("{} arguments:".format(m - 1))
    elif m == 2:
        print("{} argument:".format(m - 1))
    for i in range(1, len(sys.argv)):
        args = sys.argv[i]
        print("{}: {}".format(i, args))
