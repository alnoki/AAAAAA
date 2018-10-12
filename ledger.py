"""
This module includes classes and functions related to ledger-style
data.
"""
import datetime


class Transaction:
    """
    Represents a buy, sell, etc, that is associated with a form of
    financial transfer
    """
    def __init__(self, date=None, symbol=None, num_shares=None,
                 total_amount=None, transact_type=None, description=None):
        self.date = date  # Should be datetime.date class
        self.symbol = symbol  # Should be string
        self.num_shares = num_shares  # Should be integer
        self.total_amount = total_amount  # Should be float
        self.transact_type = transact_type  # Should be string
        self.description = description  # Should be string

    @property
    def per_share_amount(self):
        # Can't compute if data is missing and don't want divide by 0
        if self.num_shares is None or self.total_amount is None \
                or self.num_shares == 0:
            return None
        return self.total_amount / self.num_shares

    def __str__(self):
        return f"{self.date}, {self.symbol}, {self.num_shares}, " \
               f"{self.per_share_amount}, {self.total_amount}, " \
               f"{self.transact_type}, {self.description}"


# Testing

print("\nTesting per share amount attribute:\n")
transaction = Transaction(datetime.date(2018, 10, 12), 'AAPL', 20, 4000,
                          'Buy', "Apple market buy")
print(transaction.per_share_amount)  # Nominal case
transaction.num_shares = None
print(transaction.per_share_amount)  # num_shares is None
transaction.num_shares = 20
transaction.total_amount = None
print(transaction.per_share_amount)  # total_amount is None
transaction.total_amount = 4000
transaction.num_shares = 0
print(transaction.per_share_amount)  # divide by zero case

print("\nTesting __str__:\n")
print(transaction)

# Print(int(None))
