"""Includes classes and functions related to ledger-style data."""

import datetime
import decimal
from typing import Union

from .utilities import check_object


class Transaction:
    """A :xref:`transaction <finance-transaction>`

    Attributes
    ----------
    when : :obj:`datetime.date`
        Day of occurence
    total_amount : :obj:`decimal.Decimal`
        The amount of :xref:`money <money>` involved, in units of
        :xref:`$ <USD>` and :xref:`¢ <finance-cent>`
    kind : :obj:`str`
        What kind of :xref:`transaction <finance-transaction>`
    symbol : :obj:`str` or :obj:`None`
        Associated :xref:`ticker-symbol`
    num_shares : :obj:`int` or :obj:`None`
        Number of associated :xref:`shares <finance-share>`
    description : :obj:`str` or :obj:`None`
        A description, typically provided by a :xref:`brokerage <brokerage>`

    """

    kinds = set(['Bank transfer', 'Buy', 'Dividends', 'Fees', 'Sell'])

    def _check_instance_args(self, when, total_amount, kind, symbol,
                             num_shares, description):
        """Checks positional & keyword arg types/values for __init__"""

        # use when.__name__ instead of 'when'?

        check_object('types', (  # Positional arg types
            (when, (datetime.date,), 'when'),
            (total_amount, (decimal.Decimal, int), 'total_amount'),
            (kind, (str,), 'kind'),))
        check_object('values', (  # Positional arg values
            (total_amount < 0, "total_amount negative"),
            (kind not in kinds, "kind"),))
        check_object('types', (  # Keyword arg types
            (symbol, (str, None), 'symbol'),
            (num_shares, (int, None), 'num_shares'),
            (description, (str, None), 'description'),))
        check_object('values', (  # Keyword arg values
            (symbol is not None and (len(symbol) == 0 or symbol.isspace()),
                "blank symbol"),
            (kind == 'Bank transfer' and symbol is not None,
                "bank transfer has symbol"),
            (kind != 'Bank transfer' and symbol is None,
                "symbol missing"),
            (symbol is None and num_shares is not None,
                "num_shares should be None"),
            (symbol is not None and num_shares is None, "num_shares missing"),
            (num_shares is not None and num_shares <= 0,
                "non-positive num_shares"),))

    def __init__(self,
                 when: datetime.date,
                 total_amount: Union[decimal.Decimal, int],
                 kind: str,
                 symbol: str = None,
                 num_shares: int = None,
                 description: str = None) -> None:

        try:  # Check input validity before assignment
            self._check_instance_args(when, total_amount, kind, symbol,
                                      num_shares, description)
        except (TypeError, ValueError) as e:
            raise e
        else:  # Create an object if data is valid
            self.when = when
            self.total_amount = decimal.Decimal(total_amount)
            self.kind = kind
            self.symbol = symbol
            self.num_shares = num_shares
            self.description = description
