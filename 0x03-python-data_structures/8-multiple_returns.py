#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    number = len(sentence)
    character = sentence[0]
    tuple_a = (number, character)
    return tuple_a
