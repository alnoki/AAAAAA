"""Includes classes and functions related to ledger-style data."""

import datetime
from typing import Union
from src.utilities import check_object

transact_types = set(['Bank transfer', 'Buy', 'Dividends', 'Fees', 'Sell'])


class Transaction:
    """Represents a bank transfer, buy, dividends, fee, or sell"""

    def _check_instance_args(self, date, total_amount, transact_type, symbol,
                             num_shares, description):
        """Checks positional & keyword arg types/values for __init__"""
        check_object('types', dict([  # Positional arg types
            (date, ((datetime.date,), 'date')),
            (total_amount, ((float, int), 'total_amount')),
            (transact_type, ((str,), 'transact_type'))]))
        check_object('values', [  # Positional arg values
            (total_amount < 0, "total_amount negative"),
            (transact_type not in transact_types, "transact_type type")])
        check_object('types', dict([  # Keyword arg types
            (symbol, ((str, None), 'symbol')),
            (num_shares, ((int, None), 'num_shares')),
            (description, ((str, None), 'description'))]))
        check_object('values', [  # Keyword arg values
            (symbol is not None and (len(symbol) == 0 or symbol.isspace()),
                "blank symbol"),
            (transact_type == 'Bank transfer' and symbol is not None,
                "bank transfer has symbol"),
            (transact_type != 'Bank transfer' and symbol is None,
                "symbol missing"),
            (symbol is None and num_shares is not None,
                "num_shares should be None"),
            (symbol is not None and num_shares is None, "num_shares missing"),
            (num_shares is not None and num_shares <= 0,
                "non-positive num_shares")])

    def __init__(self, date: datetime.date, total_amount: Union[float, int],
                 transact_type: str, symbol: str=None,
                 num_shares: int=None, description: str=None):
        """Creates object if valid parameters, else raises error"""
        try:  # Check input validity before assignment
            self._check_instance_args(date, total_amount, transact_type,
                                      symbol, num_shares, description)
        except (TypeError, ValueError) as e:
            raise e
        else:  # Create an object if data is valid
            self.date = date
            self.total_amount = float(total_amount)
            self.transact_type = transact_type
            self.symbol = symbol
            self.num_shares = num_shares
            self.description = description

# @property
# def per_share_amount(self):
#     # Can't compute if data is missing and don't want divide by 0
#     if self.num_shares is None or self.total_amount is None \
#             or self.num_shares == 0:
#         return None
#     return self.total_amount / self.num_shares

# def __str__(self):
#     return f"{self.date}, {self.symbol}, {self.num_shares}, " \
#            f"{self.per_share_amount}, {self.total_amount}, " \
#            f"{self.transact_type}, {self.description}"

# def __repr__(self):
#     # Per share amount is not needed to reproduce object
#     return f"{self.__class__.__name__}({self.date}, {self.symbol}, " \
#            f"{self.num_shares}, " \
#            f"{self.total_amount}, {self.transact_type}, {self.description})"

# @classmethod
# def from_string(cls, string):
#     """
#     Sanitizes and re-casts arguments from a string defining a
#     transaction. Strips off class definition and associated ()
#     :param string: Of form:
#     "Transaction(2018-10-12, AAPL, 25, 4000, Buy, Apple buy)"
#     :return: A Transaction object
#     """
#     import re
#     # Regex looks for class name, then left paren, then any number
#     # of non new-line chars, then right parent before end of string
#     pattern = re.compile(f"{cls.__name__}\((.+)\)$")
#     match = pattern.findall(string)  # Could probably be different
#     if match is None:
#         return None
#     date, symbol, num_shares, total_amount, transact_type, description = \
#         match[0].split(', ') # This could probably be cleaner
#     # Recast relevant attributes
#     date = None if date == 'None' else \
#         datetime.datetime.strptime(date, '%Y-%m-%d').date()
#     symbol = None if symbol == 'None' else symbol
#     num_shares = None if num_shares == 'None' else int(num_shares)
#     total_amount = None if total_amount == 'None' else float(total_amount)
#     transact_type = None if transact_type == 'None' else transact_type
#     description = None if description == 'None' else description
#     return(cls, date, symbol, num_shares, total_amount, transact_type,
#            description)


# def test_section(description):
#     """
#     Prints a header-style message to terminal that denotes a new test
#     :param description: Description of the test being run
#     """
#     print(f"\n--- Test: {description} ---\n")
#
#
# test_section("Per share amount attribute")
# transaction = Transaction(datetime.date(2018, 10, 12), 'AAPL', 20, 4000,
#                           'Buy', "Apple market buy")
# bank_transaction = Transaction(datetime.date(2019, 6, 9), None, 500,
#                                "Bank transfer", "Transfer to brokerage\
# account")
# print(transaction.per_share_amount)  # Nominal case
# transaction.num_shares = None
# print(transaction.per_share_amount)  # num_shares is None
# transaction.num_shares = 20
# transaction.total_amount = None
# print(transaction.per_share_amount)  # total_amount is None
# transaction.total_amount = 4000
# transaction.num_shares = 0
# print(transaction.per_share_amount)  # divide by zero case
#
# test_section(" __str__ function")
# print(str(transaction))
# transaction.date, transaction.num_shares = None, None
# print(str(transaction))
# print(type(transaction.total_amount))
#
# test_section(" __repr__ function")
# transaction.date, transaction.num_shares = datetime.date(2018, 10, 12), 25
# print(repr(transaction))
# transaction.num_shares = None
# print(repr(transaction))
#
# test_section(" from_string function")
# string = repr(transaction)  # Using data from above test
# transaction = Transaction.from_string(string)
# print(str(transaction))
