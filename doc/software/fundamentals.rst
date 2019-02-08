############
Fundamentals
############

**********************
Brokerage transactions
**********************

Introduction
============

A :xref:`brokerage <brokerage>` facilitates the buying or selling of
:xref:`securities <finance-security>`, which are tradable forms of
:xref:`financial assets <financial-asset>`. One example of a
:xref:`security <finance-security>` is a :xref:`share <finance-share>` of
:xref:`stock <finance-stock>`, which
represents fractional ownership of a :xref:`corporation <corporation>`

Typically, a :xref:`ticker symbol <ticker-symbol>` will be used to identify the
particular :xref:`security <finance-security>` that is the subject of a
:xref:`financial transaction <finance-transaction>`

:xref:`Securities <finance-security>` are typically
:xref:`transacted <finance-transaction>` for a
:xref:`medium of exchange <medium-of-exchange>`, like :xref:`money <money>`,
and :term:`AAAAAA` measure :xref:`money <money>` using units of
:xref:`United States dollars (USD) <USD>` and :xref:`cents <finance-cent>`:

.. csv-table:: :xref:`money` notation
   :header: "Unit", "Symbol"
   :align: center

   :xref:`USD <USD>`, $
   :xref:`Cents <finance-cent>`, ¢

.. autoclass:: AAAAAA.ledger.Transaction

Mechanics
=========

:py:class:`AAAAAA.ledger.Transaction` (:py:class:`~AAAAAA.ledger.Transaction`)
is a :ref:`class <python:tut-classes>`
with various :ref:`attributes <python:tut-scopes>` like
:py:attr:`~AAAAAA.ledger.Transaction.total_amount` or
:py:attr:`~AAAAAA.ledger.Transaction.symbol`

:py:attr:`~AAAAAA.ledger.Transaction.kinds` is a
:ref:`class variable <python:tut-class-and-instance-variables>` that describes
the possible values that can be assumed by
:py:attr:`~AAAAAA.ledger.Transaction.kind`, which is an
:ref:`instance variable <python:tut-class-and-instance-variables>`

.. csv-table:: Possible :py:attr:`~AAAAAA.ledger.Transaction.kinds`
   :header: "Kind", ":xref:`ticker-symbol` associated?", "Interpretation"
   :align: center

   ``'Bank transfer'``, No, Add :xref:`money <money>` from a :xref:`bank`
   ``'Buy'``, Yes, "Pay :xref:`money <money>` for a
   :xref:`security <finance-security>`"
   ``'Dividends'``, Yes, "Receive :xref:`money <money>` from a
   :xref:`security <finance-security>`"
   ``'Fees'``, Yes, "Pay a :xref:`fee <fee>` when selling a
   :xref:`security <finance-security>`"
   ``'Sell'``, Yes, "Sell a :xref:`security <finance-security>` for
   :xref:`money <money>`"

When you :ref:`initialize an instance<python:tut-classobjects>` of
:py:class:`~AAAAAA.ledger.Transaction`
