.. 0.4.0

.. _quickstart:


##########
Quickstart
##########

If you want to try out some basic :term:`AAAAAA` functionality, then
follow the below steps:

#. :doc:`Download Miniconda <conda:user-guide/install/download>` (a variant
   of :xref:`Anaconda`), which will give you quick access to :xref:`Python` if
   your :xref:`operating system <OS>` did not come with :xref:`Python`
#. :wiki-pg:`Download` the :xref:`AAAAAA-zip-archive`
#. :ref:`Start up conda <conda:starting-conda>` in the
   :xref:`root directory <directory>` of the
   :xref:`archive you just downloaded <AAAAAA-zip-archive>`
#. :wiki-pg:`Type <Typing>` :command:`python` then :wiki-pg:`type <Typing>`
   :kbd:`return`

   * Rejoice, for you have just started the
     :doc:`Python interpreter <tutorial/interpreter>`

#. :xref:`Copy and paste <copy-paste>` the following then
   :wiki-pg:`type <Typing>` :kbd:`return`

   .. code-block:: python

      import datetime  # Lets you work with dates and times
      import decimal  # Lets you work with $$.¢¢
      from src.AAAAAA.ledger import Transaction  # From AAAAAA codebase
      my_transaction = Transaction(
          when=datetime.date(1994, 6, 19), total_amount=decimal.Decimal('24.48'),
          kind='Buy', symbol='ALNOKI', num_shares=12)

#. You just :xref:`paid <finance-transaction>` 24 :xref:`dollars <USD>` and 48
   :xref:`cents <finance-cent>` for 12 :xref:`shares <finance-share>`

   .. code-block:: python

      my_transaction.per_share_amount  # How much does each one cost?

.. Example code here should not require any packages beyond base miniconda

Congratulations!!!

.. tip::

   :wiki-pg:`Click <Point_and_click>` the :guilabel:`Next` button at the top or
   the bottom of the :xref:`webpage <webpage>` to continue
