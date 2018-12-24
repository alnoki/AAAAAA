# @property
# def per_share_amount(self):
#     # Can't compute if data is missing and don't want divide by 0
#     if self.num_shares is None or self.total_amount is None \
#             or self.num_shares == 0:
#         return None
#     return self.total_amount / self.num_shares

# def __str__(self):
#     return f"{self.date}, {self.symbol}, {self.num_shares}, " \
#            f"{self.per_share_amount}, {self.total_amount}, " \
#            f"{self.transact_type}, {self.description}"

# def __repr__(self):
#     # Per share amount is not needed to reproduce object
#     return f"{self.__class__.__name__}({self.date}, {self.symbol}, " \
#            f"{self.num_shares}, " \
#            f"{self.total_amount}, {self.transact_type}, {self.description})"

# @classmethod
# def from_string(cls, string):
#     """
#     Sanitizes and re-casts arguments from a string defining a
#     transaction. Strips off class definition and associated ()
#     :param string: Of form:
#     "Transaction(2018-10-12, AAPL, 25, 4000, Buy, Apple buy)"
#     :return: A Transaction object
#     """
#     import re
#     # Regex looks for class name, then left paren, then any number
#     # of non new-line chars, then right parent before end of string
#     pattern = re.compile(f"{cls.__name__}\((.+)\)$")
#     match = pattern.findall(string)  # Could probably be different
#     if match is None:
#         return None
#     date, symbol, num_shares, total_amount, transact_type, description = \
#         match[0].split(', ') # This could probably be cleaner
#     # Recast relevant attributes
#     date = None if date == 'None' else \
#         datetime.datetime.strptime(date, '%Y-%m-%d').date()
#     symbol = None if symbol == 'None' else symbol
#     num_shares = None if num_shares == 'None' else int(num_shares)
#     total_amount = None if total_amount == 'None' else float(total_amount)
#     transact_type = None if transact_type == 'None' else transact_type
#     description = None if description == 'None' else description
#     return(cls, date, symbol, num_shares, total_amount, transact_type,
#            description)