#!/usr/bin/python3
"""101-locked_class

This module contains a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass():
    """LockedClass with single attribute first_name"""
    __slots__ = "first_name"
