#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        n_list = max(a_dictionary, key=a_dictionary.get)
        return n_list
