import datetime
from src.ledger import Transaction
import pytest


class TestInit(object):
    """Tests the initialization functions of the Transaction class"""

    @pytest.mark.parametrize(
        "in_var", [None, datetime.date(2018, 10, 12), datetime.date(1, 1, 1)])
    def test_date(self, in_var):
        """Verifies the date is correctly initialized"""
        t = Transaction(date=in_var)
        assert t.date == in_var

    @pytest.mark.parametrize(
        "in_var", [None, '', ' ', 'AAPL', 'BRK.A', 'AAPL', '^CRSPTMT'])
    def test_symbol(self, in_var):
        """Verifies the symbol is correctly initialized"""
        t = Transaction(symbol=in_var)
        assert t.symbol == in_var

    @pytest.mark.parametrize(
        "in_var", [None, 0, 1.2, 3, -1])
    def test_num_shares(self, in_var):
        """Verifies the number of shares is correctly initialized"""
        t = Transaction(num_shares=in_var)
        assert t.num_shares == in_var



# class TestTransaction(unittest.TestCase):
#     """Test case for validating Transaction class"""
#
#     def setUp(self):
#         """Initializes new class instances for each test"""
#         self.t0 = Transaction(datetime.date(2018, 10, 12), 'AAPL', 20, 4000,
#                               'Buy', "Apple market buy")
#         self.t1 = Transaction(datetime.date(2019, 6, 9), None, None, 500,
#                               "Bank transfer", "Transfer from Chase")
#
#     def test_init(self):
#         """Tests that class attributes are stored as expected"""
#         self.assertEqual(self.t0.date, datetime.date(2018, 10, 12))
#
#
# if __name__ == '__main__':
#     unittest.main()