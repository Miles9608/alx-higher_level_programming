#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: v * 2 for k, v in a_dictionary.items()}#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary
