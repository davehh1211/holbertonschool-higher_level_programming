#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        point = fct(*args)
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as den:
        print("Exception:", den, file=sys.stderr)
        return None
    return point
