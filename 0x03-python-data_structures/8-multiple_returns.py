#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        tuple_a = (a, None)
        return tuple_a
    else:
        tuple_a = (a, sentence[0])
        return tuple_a
