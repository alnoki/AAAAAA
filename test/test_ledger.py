import datetime
from ledger import Transaction
import pytest


# Could have these vars go into a fixture as a yielded value
# test_transactions.date, etc
@pytest.mark.parametrize('date',
     [datetime.date(2018, 10, 12), datetime.date(0, 0, 1)])
@pytest.mark.parametrize('symbol', ['AAPL', None, 'BRK.A'])
@pytest.mark.parametrize('num_shares', [20, None, 0])
@pytest.mark.parametrize('total_amount', [0, None, 500, 300.46])
@pytest.mark.parametrize('transact_type', ['Buy', 'Fees', None])
@pytest.mark.parametrize('description', [None, '', "Market buy"])
def test_init(date, symbol, num_shares, total_amount, transact_type,
              description):
    t = Transaction(
            date, symbol, num_shares, total_amount, transact_type, description)
    assert \
        t.date == date and \
        t.symbol == symbol and \
        t.num_shares == num_shares and \
        t.total_amount == total_amount and \
        t.transact_type == transact_type and \
        t.description == description

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