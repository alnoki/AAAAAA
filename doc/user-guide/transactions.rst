

############
Transactions
############

.. contents::
   :local:

.. _user-fin-background:


*************************
Background financial info
*************************

A :xref:`brokerage <brokerage>` facilitates the
:xref:`buying or selling <finance-transaction>` of
:xref:`securities <finance-security>`, which are tradable forms of
:xref:`financial assets <financial-asset>`. One example of a
:xref:`security <finance-security>` is a :xref:`share <finance-share>` of
:xref:`stock <finance-stock>`, which represents fractional ownership of a
:xref:`corporation <corporation>`

Typically, a :xref:`ticker symbol <ticker-symbol>` will be used to identify the
particular :xref:`security <finance-security>` that is the subject of a
:xref:`financial transaction <finance-transaction>`

:xref:`Securities <finance-security>` are typically
:xref:`transacted <finance-transaction>` for a
:xref:`medium of exchange <medium-of-exchange>`, like :xref:`money <money>`,
and :term:`AAAAAA` measure :xref:`money <money>` using units of
:xref:`United States dollars (USD) <USD>` and :xref:`cents <finance-cent>`:

.. csv-table:: :xref:`money` notation in :term:`AAAAAA`
   :align: center
   :header: Unit, Symbol

   :xref:`USD <USD>`, $
   :xref:`Cents <finance-cent>`, ¢


*********
Mechanics
*********

:py:class:`AAAAAA.ledger.Transaction`, shortened to
:py:class:`~AAAAAA.ledger.Transaction`, is a :ref:`class <python:tut-classes>`,
which is a special type of :term:`object <python:object>`:

.. automodule:: AAAAAA.ledger
   :members: Transaction

.. tip::

   If you are viewing
   :ref:`AAAAAA documentation as a website <what-next-format>`, you can click
   :guilabel:`[source]` above to view the original
   :xref:`source code <source-code>`, then click :guilabel:`[docs]` to return

:py:class:`~AAAAAA.ledger.Transaction` has a
:ref:`namespace <python:tut-scopes>` with various
:term:`attributes <python:attribute>`, like
:py:attr:`~AAAAAA.ledger.Transaction.total_amount` or
:py:attr:`~AAAAAA.ledger.Transaction.symbol`

:py:attr:`~AAAAAA.ledger.Transaction.kinds` is a
:ref:`class variable <python:tut-class-and-instance-variables>` that describes
the possible values that can be assumed by
:py:attr:`~AAAAAA.ledger.Transaction.kind`, which is an
:ref:`instance variable <python:tut-class-and-instance-variables>`

.. csv-table:: Possible :py:attr:`~AAAAAA.ledger.Transaction.kinds`
   :align: center
   :header: Kind, :xref:`ticker-symbol` associated?, Interpretation

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
:py:class:`~AAAAAA.ledger.Transaction` you are
:ref:`calling a function <python:tut-functions>` and as such you must provide
:ref:`default argument values <python:tut-defaultargs>`, also known as
:term:`positional arguments <python:argument>`, like
:py:attr:`~AAAAAA.ledger.Transaction.total_amount`

You may optionally provide one or more
:ref:`keyword arguments <python:tut-keywordargs>`, like
:py:attr:`~AAAAAA.ledger.Transaction.num_shares`, for example, which would
enable you to access :py:attr:`~AAAAAA.ledger.Transaction.per_share_amount`,
(itself a :py:class:`python:property`)


***********************************
A word (or several) about precision
***********************************

Clearly you need to :ref:`work with numbers <python:tut-numbers>`, and it makes
sense to have an :py:obj:`integer <python:int>` amount of
:xref:`shares <finance-share>`

But does it make sense to buy something that costs exactly
``$110.1200000000000045474735088646411895751953125`` ?!?!?!?

.. admonition:: This just in

   No, it does not!

That is why :py:attr:`~AAAAAA.ledger.Transaction.total_amount` is a
:doc:`decimal <python:library/decimal>`, not a
:py:obj:`floating point number <python:float>`

Okay, alnoki is fired up
========================

You bet your bottom :xref:`dollar (USD) <USD>` that :github:`alnoki <alnoki>`
is on a :doc:`floating point precision <python:tutorial/floatingpoint>` rampage

If you don't already know how
:doc:`invoke the Python interpreter <tutorial/interpreter>`, please feel free
to to grab yourself a slippery new copy of
:doc:`Miniconda <conda:user-guide/install/download>` and
:ref:`fire up conda <conda:starting-conda>` then :wiki-pg:`type <Typing>`

.. code-block:: bash

   python

:wiki-pg:`Type <Typing>` :kbd:`return` and take several deep breaths to calm
your nerves, but don't take too many stabilitory inhalations or you may deviate
from the pressing inquisition on hand, which continues below

.. tip::

   :xref:`Copy-paste <copy-paste>` the below lines into the
   :doc:`Python interpreter <tutorial/interpreter>` then
   :wiki-pg:`type <Typing>` :kbd:`return`

.. code-block:: python

   from decimal import Decimal
   Decimal.from_float(110.12)

What's that you say, :doc:`Python interpreter <tutorial/interpreter>`?

.. code-block:: python

   >>> from decimal import Decimal
   >>> Decimal.from_float(110.12)
   Decimal('110.1200000000000045474735088646411895751953125')

.. seealso::

   The official
   :doc:`floating point precision rampage <python:tutorial/floatingpoint>`
