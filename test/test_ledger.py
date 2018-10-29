import datetime
from src.ledger import Transaction, transact_types
import pytest


class TestTransactionInit(object):
    """Tests the initialization functions of the Transaction class"""

    # Default values for positional arguments
    d_date = datetime.date.today()
    d_total_amount = 0
    d_transact_type = 'Buy'
    d_args = (d_date, d_total_amount, d_transact_type)

    @pytest.mark.parametrize(
        "i_date", [None, 1, 'abc', datetime.date(2018, 10, 12),
                   datetime.date(1, 1, 1)])
    def test_date(self, i_date):
        """Verifies date is correctly initialized"""
        # Attribute error should be raised if date isn't correct type
        if not isinstance(i_date, datetime.date):
            with pytest.raises(AttributeError):
                Transaction(date=i_date, total_amount=self.d_total_amount,
                            transact_type=self.d_transact_type)
        else:  # Check date has been assigned correctly
            t = Transaction(date=i_date, total_amount=self.d_total_amount,
                            transact_type=self.d_transact_type)
            assert t.date == i_date

    @pytest.mark.parametrize('i_total_amount', [None, -2, 'abc', 45, 45.0])
    def test_total_amount(self, i_total_amount):
        """Verifies total_amount is correctly initialized"""
        # Attribute error should be raised if not a float or an int
        if not isinstance(i_total_amount, (float, int)):
            with pytest.raises(AttributeError):
                Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
        # Value error should be raised if amount is negative
        elif i_total_amount < 0:
            with pytest.raises(ValueError):
                Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
        else:  # Verify value has been cast as float and assigned
            t = Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
            assert (t.total_amount == i_total_amount and
                    type(t.total_amount) is float)

    @pytest.mark.parametrize('i_transact_type',
                             [None, 3, '', ' ', 'buy', 'Sell'])
    def test_transact_type(self, i_transact_type):
        """Verifies transact_type is correctly initialized"""
        # Attribute error should be raised if type is not string
        if not isinstance(i_transact_type, str):
            with pytest.raises(AttributeError):
                Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type)
        # Value error should be raised if isn't 'Buy', 'Sell', etc.
        # Case sensitive: 'buy' should fail, but 'Buy' would pass
        elif i_transact_type not in transact_types:
            with pytest.raises(ValueError):
                Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type)
        else:  # Verify value has been assigned correctly
            t = Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type)
            assert t.transact_type == i_transact_type

    @pytest.mark.parametrize('i_symbol', [None, 3, '', '   ', 'BRK.A', 'AAPL'])
    @pytest.mark.parametrize(
        'i_transact_type', [None, 'Bank transfer', 'Sell'])
    def test_symbol(self, i_symbol, i_transact_type):
        """Verifies symbol is correctly initialized"""
        # Attribute error should be raised if type is not string or None
        if not isinstance(i_symbol, str) or i_symbol is not None:
            with pytest.raises(AttributeError):
                Transaction(*self.d_args, symbol=i_symbol)
        # No symbol if bank transfer, no bank transfer if symbol
        elif ((i_transact_type == 'Bank transfer' and i_symbol is not None) or
              (i_transact_type != 'Bank transfer' and i_symbol is None)):
            with pytest.raises(ValueError):
                Transaction(
                    self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol)
        # Symbol must have some actual text if is not None
        elif ((i_symbol is not None) and
              (len(i_symbol) == 0 or i_symbol.isspace())):
            with pytest.raises(ValueError):
                Transaction(*self.d_args, symbol=i_symbol)
        else:  # Verify value has been assigned correctly
            t = Transaction(*self.d_args, symbol=i_symbol)
            assert t.symbol == i_symbol


# Can't have num_shares if symbol is None....