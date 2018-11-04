"""Commonly-used general functions"""


def check_object(what_to_check, checks):
    """Checks object(s) for valid type or value"""
    if what_to_check == 'types':
        # checks is a dictionary, with objects as keys. The values are
        # tuples with the expected type(s) of the object, and an error
        # message to be raised if the object is of the wrong type
        for obj, (obj_types, error_msg) in checks.items():
            actual_types = tuple([  # Types that are not None
                val for val in obj_types if val is not None])
            if not ((None in obj_types and obj is None) or
                    (isinstance(obj, actual_types))):
                raise TypeError(error_msg)
    if what_to_check == 'values':
        # checks is a list of tuples. Each tuple is a boolean condition
        # and a message to be raised if the condition is true
        for check, error_message in checks:
            if check is True:
                raise ValueError(error_message)
