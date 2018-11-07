import datetime
import pytest
from src.ledger import Transaction, transact_types


class TestTransactionInit(object):
    """Tests the initialization functions of the Transaction class"""

    # Default values for positional arguments
    d_date = datetime.date.today()
    d_total_amount = 0
    d_transact_type = 'Bank transfer'
    d_symbol = 'AAPL'
    d_num_shares = 1
    d_args = (d_date, d_total_amount, d_transact_type)

    @pytest.mark.parametrize(
        "i_date",
        [None, 1, 'abc', datetime.date(2018, 10, 12), datetime.date(1, 1, 1)],
        ids=['None', None, 'abc', '20181012', '00010101'])
    def test_date(self, i_date):
        """Verifies date is correctly initialized"""
        # Type error should be raised if date isn't correct type
        if not isinstance(i_date, datetime.date):
            with pytest.raises(TypeError, match="date"):
                Transaction(date=i_date, total_amount=self.d_total_amount,
                            transact_type=self.d_transact_type)
        else:  # Check date has been assigned correctly
            t = Transaction(date=i_date, total_amount=self.d_total_amount,
                            transact_type=self.d_transact_type)
            assert t.date == i_date

    @pytest.mark.parametrize('i_total_amount', [None, -2, 'abc', 45, 45.0])
    def test_total_amount(self, i_total_amount):
        """Verifies total_amount is correctly initialized"""
        # Type error should be raised if not a float or an int
        if not isinstance(i_total_amount, (float, int)):
            with pytest.raises(TypeError, match="total_amount"):
                Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
        # Value error should be raised if amount is negative
        elif i_total_amount < 0:
            with pytest.raises(ValueError, match="total_amount negative"):
                Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
        else:  # Verify value has been cast as float and assigned
            t = Transaction(date=self.d_date, total_amount=i_total_amount,
                            transact_type=self.d_transact_type)
            assert (t.total_amount == i_total_amount and
                    isinstance(t.total_amount, float))

    @pytest.mark.parametrize(
        'i_transact_type', [None, 3, '', ' ', 'buy', 'Sell'],
        ids=[None, None, "empty str", "whitespace str", "lowercase buy",
             "correct Sell"])
    def test_transact_type(self, i_transact_type):
        """Verifies transact_type is correctly initialized"""
        # Type error should be raised if type is not string
        if not isinstance(i_transact_type, str):
            with pytest.raises(TypeError, match="transact_type"):
                Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type)
        # Value error should be raised if isn't 'Buy', 'Sell', etc.
        # Case sensitive: 'buy' should fail, but 'Buy' would pass
        elif i_transact_type not in transact_types:
            with pytest.raises(ValueError, match="transact_type type"):
                Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type)
        else:  # Verify value has been assigned correctly
            # Should only apply to 'Sell' test, so need num_shares
            t = Transaction(date=self.d_date, total_amount=self.d_total_amount,
                            transact_type=i_transact_type,
                            symbol=self.d_symbol, num_shares=self.d_num_shares)
            assert t.transact_type == i_transact_type

    @pytest.mark.parametrize(
        'i_symbol', [None, 3, '', '   ', 'BRK.A', 'AAPL'],
        ids=["None symbol", "int symbol", "Empty symbol", "Whitespace symbol",
             None, None])
    @pytest.mark.parametrize(
        'i_transact_type', ['Bank transfer', 'Sell'])
    def test_symbol(self, i_symbol, i_transact_type):
        """Verifies symbol is correctly initialized"""
        # Type error should be raised if type is not None or str
        if i_symbol is not None and not isinstance(i_symbol, str):
            with pytest.raises(TypeError, match="symbol"):
                Transaction(*self.d_args, symbol=i_symbol)
        # Symbol must have some actual text if is not None
        elif ((i_symbol is not None) and
              (len(i_symbol) == 0 or i_symbol.isspace())):
            with pytest.raises(ValueError, match="blank symbol"):
                Transaction(
                    self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol)
        # Bank transfers can not have associated symbols
        elif i_transact_type == 'Bank transfer' and i_symbol is not None:
            with pytest.raises(ValueError, match="bank transfer has symbol"):
                Transaction(
                    self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol)
        # Must have symbol if not bank transfer
        elif i_transact_type != 'Bank transfer' and i_symbol is None:
            with pytest.raises(ValueError, match="symbol missing"):
                Transaction(
                    self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol)
        else:  # Verify value has been assigned correctly
            if i_transact_type == 'Bank transfer':
                i_num_shares = None
            else:
                i_num_shares = self.d_num_shares
            t = Transaction(
                    self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol,
                    num_shares=i_num_shares)
            assert t.symbol == i_symbol

    @pytest.mark.parametrize(
        'i_num_shares', [None, 'abc', 0, 2, 3.5, -1, 0.0],
        ids=["None num_shares", "str num_shares", "0 shares", "2 shares",
             "3.5 shares", "-1 shares", "0.0 shares"])
    @pytest.mark.parametrize('i_symbol', [None, 'AAPL'],
        ids=["None symbol", None])
    def test_num_shares(self, i_num_shares, i_symbol):
        """Verifies num_shares is correctly initialized"""
        i_transact_type = 'Sell'
        # Type error should be raised if type is not None or int
        if i_num_shares is not None and not isinstance(i_num_shares, int):
            with pytest.raises(TypeError, match="num_shares"):
                Transaction(
                    date=self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, num_shares=i_num_shares)
        # Can not have num_shares if symbol is undefined
        elif i_symbol is None and i_num_shares is not None:
            with pytest.raises(ValueError, match="num_shares should be None"):
                Transaction(
                    *self.d_args, symbol=i_symbol, num_shares=i_num_shares)
        # Need num_shares if symbol is defined
        elif i_symbol is not None and i_num_shares is None:
            with pytest.raises(ValueError, match="num_shares missing"):
                Transaction(
                    date=self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol,
                    num_shares=i_num_shares)
        # Value error if num_shares is not None but is < or = to 0
        elif i_num_shares is not None and i_num_shares <= 0:
            with pytest.raises(ValueError, match="non-positive num_shares"):
                Transaction(
                    date=self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol,
                    num_shares=i_num_shares)
        else:  # Verify value has been assigned correctly
            if i_symbol is None:
                i_transact_type = self.d_transact_type
            t = Transaction(
                    date=self.d_date, total_amount=self.d_total_amount,
                    transact_type=i_transact_type, symbol=i_symbol,
                    num_shares=i_num_shares)
            assert t.num_shares == i_num_shares

    @pytest.mark.parametrize('i_description', [None, 3, '', 'Comment'],
        ids=[None, "int description", "empty description",
             "correct description"])
    def test_description(self, i_description):
        # Check that description is either None or string
        if i_description is not None and not isinstance(i_description, str):
            with pytest.raises(TypeError, match="description"):
                Transaction(*self.d_args, description=i_description)
        else:
            t = Transaction(*self.d_args, description=i_description)
            assert i_description == t.description
