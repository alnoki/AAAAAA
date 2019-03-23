import datetime
import decimal
from typing import Set, Optional


class Transaction:
    """A :wiki-pg:`financial transaction <Financial_transaction>`

    Attributes
    ----------
    when : :obj:`datetime.datetime`
        :wiki-pg:`Time` of occurence, in
        :wiki-pg:`UTC <Coordinated_Universal_Time>`
    amount : :obj:`decimal.Decimal`
        The nonnegative amount of :wiki-pg:`money <Money>` involved, in
        units of :wiki-pg:`$ <United_States_dollar>` and
        :wiki-pg:`¢ <Cent_(currency)>`
    kind : :obj:`str`
        What kind of :wiki-pg:`transaction <Financial_transaction>`,
        from :py:attr:`kinds`
    symbol : :obj:`str` or :obj:`None`
        Associated :wiki-pg:`ticker symbol <Ticker_symbol>`
    shares : :obj:`int` or :obj:`None`
        Number of associated :wiki-pg:`shares <Share_(finance)>`
    comment : :obj:`str` or :obj:`None`
        A description, typically provided by a
        :wiki-pg:`brokerage <Broker>`

    """

    def __init__(self,
                 when: datetime.datetime,
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

    kinds = {
        'Buy': (False, True, True),
        'Deposit': (True, False, None),
        'Pay': (False, True, None),
        'Receive': (True, True, None),
        'Sell': (True, True, False),
        'Withdraw': (False, False, None),
    }
    """

    :obj:`dict` from :obj:`str` to :obj:`tuple` of :obj:`bool` and \
    :obj:`None` :

    Allowed values for :py:attr:`kind`

    .. csv-table::
       :align: center
       :header: :obj:`Key <dict>`, Meaning

       ``Buy``, ":wiki-pg:`Buy <Financial_transaction>` a
       :wiki-pg:`security <Security_(finance)>`"
       ``Deposit``, ":wiki-pg:`Deposit <Deposit_(finance)>` into a
       :wiki-pg:`brokerage account <Securities_account>`"
       ``Pay``, ":wiki-pg:`Pay <Financial_transaction>` a
       :wiki-pg:`fee <Fee>`"
       ``Receive``, Receive :wiki-pg:`dividends <Dividend>`
       ``Sell``, ":wiki-pg:`Sell <Financial_transaction>` a
       :wiki-pg:`security <Security_(finance)>`"
       ``Withdraw``, ":wiki-pg:`Withdraw <Deposit_(finance)>` from a
       :wiki-pg:`brokerage account <Securities_account>`"

    Each :obj:`key <dict>` corresponds to a :obj:`value <dict>` which is
    a :obj:`tuple` that provides more information about the nature of
    each possible :attr:`kind`. Each :term:`python:object` in the
    :obj:`tuple` describes the relationship between a :attr:`kind` and
    another :term:`python:attribute` of
    :py:class:`~AAAAAA.ledger.Transaction`. In order of occurence within
    the :obj:`tuple`, interpretations for each :term:`python:object` are
    as follows:

    .. csv-table::
       :align: center
       :header: :obj:`True` if, :obj:`False` if, :obj:`None` if

       :attr:`amount` received, :attr:`amount` surrendered, \-
       :attr:`symbol` is not :obj:`None`, ":attr:`symbol` is
       :obj:`None`", \-
       :attr:`shares` received, :attr:`shares` surrendered, "No exchange
       of :attr:`shares`"

    These effects are described from the perspective of a
    :wiki-pg:`brokerage account <Securities_account>`. This means that
    :attr:`amount` is received for ``Deposit``, and :attr:`shares` are
    received but :attr:`amount` is surrendered for ``Buy``

    """

    @property
    def per_share_amount(self) -> Optional[decimal.Decimal]:
        """:obj:`decimal.Decimal` or :obj:`None`:

        The amount of :xref:`money <money>` associated with each
        :xref:`share <finance-share>`

        Only defined if
        :py:class:`~AAAAAA.ledger.Transaction.shares` is not :obj:`None`
        and is nonzero

        """
        if self.num_shares is None or self.num_shares == 0:
            return
        return self.total_amount / self.num_shares
