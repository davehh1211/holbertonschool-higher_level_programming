#!/usr/bin/python3
"""pascal traignel
"""


def pascal_triangle(n):
    """
    Args:
        n (int): the depth of pascal's
    """
    # creamos una lista que contendra los dos primeras lineas
    if n <= 0:
        return

    triang = []
    for i in range(n):
        space = []
        for sq in range(i + 1):
            if sq is 0 or sq is i:
                space.append(1)
            else:
                space.append(triang[i - 1][sq - 1] + triang[i - 1][sq])
        triang.append(space)
    return triang
