import datetime
import unittest
from ledger import Transaction


class TestTransaction(unittest.TestCase):
    """Test case for validating Transaction class"""

    def setUp(self):
        """Initializes new class instances for each test"""
        self.t0 = Transaction(datetime.date(2018, 10, 12), 'AAPL', 20, 4000,
                              'Buy', "Apple market buy")
        self.t1 = Transaction(datetime.date(2019, 6, 9), None, None, 500,
                              "Bank transfer", "Transfer from Chase")

    def test_init(self):
        """Tests that class attributes are stored as expected"""
        self.assertEqual(self.t0.date, datetime.date(2018, 10, 12))


if __name__ == '__main__':
    unittest.main()