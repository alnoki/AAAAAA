"""Contains tests for utilities"""

import pytest
from src.utilities import check_object


class FakeClass:
    pass

fake_instance = FakeClass()
object_data = dict([('int', 75),
                    ('float', 0.1),
                    ('None', None),
                    ('str', 'GSU'),
                    ('dict', dict([('key', 'value')])),
                    ('bool', True),
                    ('tuple', ((3, ()))),
                    ('class', fake_instance)])


class TestCheckObject(object):
    """Tests the check_object function"""
    @pytest.mark.parametrize('checks', [
        # Verify no error message when correct types
        ((object_data['str'], (str,), "correct type"),
         (object_data['int'], (int,), "correct type"),
         (object_data['tuple'], (tuple,), "correct type"),
         (object_data['bool'], (bool,), "correct type")),
        # Verify error when should be None
        ((object_data['dict'], (dict, None), "correct type"),
         (object_data['float'], (None,), "is not None")),
        # Verify error when should be an actual type
        ((object_data['None'], (float,), "not float"),),
        # Verify error when should be either a number or None
        ((object_data['dict'], (float, int, None), "not num or None"),),
        # Verify no error and that a class can be checked
        ((object_data['class'], (FakeClass,), "correct type"),)],
        ids=["All correct", "Should be None", "Should be actual type",
             "No type match", "Class type"])
    def test_types_check(self, checks):
        """Verifies test on types for checklist in proper format"""
        # Check first to see if an error message should be raised
        for (obj, obj_types, error_msg) in checks:
            if error_msg != "correct type":
                with pytest.raises(TypeError, match=error_msg):
                    check_object('types', checks)
                break  # Verify the first error message only
        else:  # If an error message shouldn't be raised, verify
            check_object('types', checks)

    @pytest.mark.parametrize('checks', [
        # Verify no error message when correct value
        ((object_data['dict']['key'] != 'value', "correct value"),
         (object_data['float'] < 0.05, "correct value")),
        # Verify error when value is invalid
        ((object_data['int'] > 50, "integer too large"),),
        # Verify error when combination condition is invalid
        ((object_data['bool'] is True and object_data['str'] != "GRS",
          "value combo"),),
    ], ids=["All correct", "int too big", "combo check"])
    def test_values_check(self, checks):
        """Verifies test on values for checklist in proper format"""
        # Check first to see if an error message should be raised
        for (check, error_msg) in checks:
            if error_msg != "correct value":
                with pytest.raises(ValueError, match=error_msg):
                    check_object('values', checks)
                break  # Verify the first error message only
        else:  # If an error message shouldn't be raised, verify
            check_object('values', checks)
