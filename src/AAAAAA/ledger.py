import datetime
import decimal
from typing import Set, Optional


class Transaction:
    """An exchange of money inside of a brokerage account

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
        Associated :xref:`ticker symbol <ticker-symbol>`
    num_shares : :obj:`int` or :obj:`None`
        Number of associated :xref:`shares <finance-share>`
    description : :obj:`str` or :obj:`None`
        A description, typically provided by a
        :xref:`brokerage <brokerage>`
    kinds : :obj:`set` of :obj:`string`
        Allowed kinds of :xref:`transactions <finance-transaction>`

    """

    kinds: Set[int] = set(['Bank transfer', 'Buy', 'Dividends', 'Fees',
                           'Sell'])

    def __init__(self,
                 when: datetime.date,
                 total_amount: decimal.Decimal,
                 kind: str,
                 symbol: Optional[str] = None,
                 num_shares: Optional[int] = None,
                 description: Optional[str] = None) -> None:

        self.when = when
        self.total_amount = total_amount
        self.kind = kind
        self.symbol = symbol
        self.num_shares = num_shares
        self.description = description

    @property
    def per_share_amount(self) -> Optional[decimal.Decimal]:
        """ :obj:`decimal.Decimal` or :obj:`None`:

        The amount of :xref:`money <money>` associated with each
        :xref:`share <finance-share>`

        Only defined if
        :py:class:`~AAAAAA.ledger.Transaction.num_shares` is
        defined and is nonzero

        """
        if self.num_shares is None or self.num_shares == 0:
            return
        return self.total_amount / self.num_shares
