#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        n_list = sorted(a_dictionary)
        return n_list[-1]
