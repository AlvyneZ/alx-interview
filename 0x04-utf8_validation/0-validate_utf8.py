#!/usr/bin/python3
"""
0-validate_utf8.py - Provides a function for UTF-8 encoding
 validation of a byte sequence
"""


def validUTF8(data):
    """validates UTF-8 encoding in a byte sequence

    Args:
        data (List[int]): byte sequence to be checked

    Returns:
        bool: True if valid, False otherwise
    """
    byte_count = 0

    for byte in data:
        if byte_count == 0:
            if byte >> 5 == 0b110:
                byte_count = 1
            elif byte >> 4 == 0b1110:
                byte_count = 2
            elif byte >> 3 == 0b11110:
                byte_count = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
