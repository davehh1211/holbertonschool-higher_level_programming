#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    for i in range(1, len(sys.argv)):
        num = int(sys.argv[i])
        suma = suma + num
    print(suma)
