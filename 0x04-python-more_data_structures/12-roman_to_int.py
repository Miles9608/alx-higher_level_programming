#!/usr/bin/python3
def roman_to_int(roman_string):
    arra = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    miles = 0
    p = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if arra[roman_string[c]] >= p:
                miles += arra[roman_string[c]]
            else:
                miles -= arra[roman_string[c]]
            p = arra[roman_string[c]]
    return miles
