#!/usr/bin/python3
"""This module soporte a function that
validate utf-8 format."""


def validUTF8(data):
    """This function return True if the format is utf-8."""
    successive_10 = 0
    for b in data:
        b = bin(b).replace('0b', '').rjust(8, '0')
        if successive_10 != 0:
            successive_10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
            successive_10 = len(b.split('0')[0]) - 1
    return True
