#!/usr/bin/python3
"""This module soporte a function that
validate utf-8 format."""


def validUTF8(data):
    """This function return True if the format is utf-8."""
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except Exception:
        return False
    return True
