import datetime
import decimal
from typing import Set, Optional


class Transaction:
    """A :wiki-pg:`financial transaction <Financial_transaction>`

    Attributes
    ----------
    when : :obj:`datetime.date`
        :wiki-pg:`Time` of occurence
    amount : :obj:`decimal.Decimal`
        The amount of :xref:`money <money>` involved, in units of
        :xref:`$ <USD>` and :xref:`¢ <finance-cent>`
    kind : :obj:`str`
        What kind of :xref:`transaction <finance-transaction>`
    symbol : :obj:`str` or :obj:`None`
        Associated :xref:`ticker symbol <ticker-symbol>`
    shares : :obj:`int` or :obj:`None`
        Number of associated :xref:`shares <finance-share>`
    comment : :obj:`str` or :obj:`None`
        A description, typically provided by a
        :xref:`brokerage <brokerage>`

    """

    def __init__(self,
                 when: datetime.date,
                 amount: decimal.Decimal,
                 kind: str,
                 symbol: Optional[str] = None,
                 shares: Optional[int] = None,
                 comment: Optional[str] = None) -> None:
        """Create a :py:class:`~AAAAAA.ledger.Transaction`"""
        self.when = when
        self.amount = amount
        self.kind = kind
        self.symbol = symbol
        self.shares = shares
        self.comment = comment

    kinds: Set[str] = set(['Bank transfer', 'Buy', 'Dividends', 'Fees',
                           'Sell'])
    """:obj:`set` of :obj:`string`:

    Allowed values for :py:attr:`kind`

    """

    @property
    def per_share_amount(self) -> Optional[decimal.Decimal]:
        """:obj:`decimal.Decimal` or :obj:`None`:

        The amount of :xref:`money <money>` associated with each
        :xref:`share <finance-share>`

        Only defined if
        :py:class:`~AAAAAA.ledger.Transaction.num_shares` is
        defined and is nonzero

        """
        if self.num_shares is None or self.num_shares == 0:
            return
        return self.total_amount / self.num_shares
