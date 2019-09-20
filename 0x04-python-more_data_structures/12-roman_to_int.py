#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return 0
    elif not isinstance(roman_string, str):
        return 0
    elif roman_string in romans:
        return romans.get(roman_string)
    else:
        num = romans[roman_string[0]]
        for count in range(len(roman_string) - 1):
            future = romans[roman_string[count + 1]]
            present = romans[roman_string[count]]
            num += future if future <= present else +future - 2 * present
        return num
