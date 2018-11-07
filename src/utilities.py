"""Commonly-used general functions"""


def check_object(what_to_check: str, checks: tuple):
    """Checks object(s) for valid type or value

    Positional arguments:
        what_to_check -- either 'types' or 'values'
        checks -- a tuple of tuples with formats given below. In each
            case, 'str' corresponds to an error message

    The 'minimal' amount of syntax to define the checks argument:
        ((object, (type,), str),) -- when checking 'types'
        ((bool, str),) -- when checking 'values'

    Assumes that inputs are valid, rather than recursively checking
    """
    # Check each object matches allowed type(s), or if allowed, is None
    if what_to_check == 'types':
        for (obj, obj_types, error_msg) in checks:
            actual_types = tuple([  # Types that are not None
                val for val in obj_types if val is not None])
            if not ((None in obj_types and obj is None) or
                    (isinstance(obj, actual_types))):
                raise TypeError(error_msg)
    # Verify that value checks all evaluate to false
    if what_to_check == 'values':
        for check, error_msg in checks:
            if check is True:
                raise ValueError(error_msg)
