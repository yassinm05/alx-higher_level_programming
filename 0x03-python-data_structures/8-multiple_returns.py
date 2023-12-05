#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return_val = (len(sentence), None)
        return (return_val)
    else:
        return_val = (len(sentence), sentence[0])
        return (return_val)
