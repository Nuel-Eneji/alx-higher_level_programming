#!/usr/bin/python3
"""Square with size"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
