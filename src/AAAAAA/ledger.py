"""Includes classes and functions related to ledger-style data."""

import datetime
import decimal
from typing import Union

from .utilities import check_object

transact_types = set(['Bank transfer', 'Buy', 'Dividends', 'Fees', 'Sell'])


class Transaction:
    """Represents a transaction in a brokerage account

    Parameters
    ----------
    date : :obj:`datetime.date`
        The day on which a :obj:`Transaction` occured
    total_amount : :obj:`decimal.Decimal` or :obj:`int`
        The total amount transacted. Use a :obj:`decimal.Decimal` if
        cents are specified, and an :obj:`int` if only dollars are
        specified
    transact_type : :obj:`str`
        What type of :obj:`Transaction` occured. Should be a member of
        transact_types
    symbol : :obj:`str`
        Ticker symbol associated with a :obj:`Transaction`
    num_shares : :obj:`int` or :obj:`None`
        The number of shares associated with a :obj:`Transaction` that
        involves a symbol
    description : :obj:`str` or :obj:`None`
        A description of the :obj:`Transaction`, like one provided by
        a broker

    """

    def _check_instance_args(self, date, total_amount, transact_type, symbol,
                             num_shares, description):
        """Checks positional & keyword arg types/values for __init__"""

        # use date.__name__ instead of 'date'?

        check_object('types', (  # Positional arg types
            (date, (datetime.date,), 'date'),
            (total_amount, (decimal.Decimal, int), 'total_amount'),
            (transact_type, (str,), 'transact_type'),))
        check_object('values', (  # Positional arg values
            (total_amount < 0, "total_amount negative"),
            (transact_type not in transact_types, "transact_type type"),))
        check_object('types', (  # Keyword arg types
            (symbol, (str, None), 'symbol'),
            (num_shares, (int, None), 'num_shares'),
            (description, (str, None), 'description'),))
        check_object('values', (  # Keyword arg values
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
                "non-positive num_shares"),))

    def __init__(self,
                 date: datetime.date,
                 total_amount: Union[decimal.Decimal, int],
                 transact_type: str,
                 symbol: str = None,
                 num_shares: int = None,
                 description: str = None) -> None:
        """ Sanitize inputs

        Raises
        ------
        TypeError
            if a parameter is of the invalid type
        ValueError
            if a parameter contains invalid data
        """

        try:  # Check input validity before assignment
            self._check_instance_args(date, total_amount, transact_type,
                                      symbol, num_shares, description)
        except (TypeError, ValueError) as e:
            raise e
        else:  # Create an object if data is valid
            self.date = date
            self.total_amount = decimal.Decimal(total_amount)
            self.transact_type = transact_type
            self.symbol = symbol
            self.num_shares = num_shares
            self.description = description
