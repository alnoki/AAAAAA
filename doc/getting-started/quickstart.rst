.. 5333f1a

.. _quickstart:


###########
Quick start
###########

If you want to try out some basic :term:`AAAAAA` functionality, then
follow the below steps:

#. :std:doc:`Download Miniconda <conda:user-guide/install/download>` (a variant
   of :xref:`Anaconda`), which will give you quick access to :xref:`Python` if
   your :xref:`operating system <OS>` did not come pre-loaded with it
#. Download the :xref:`AAAAAA-zip-archive`
#. :ref:`Start up Conda <conda:starting-conda>` and navigate to the root
   :xref:`directory <directory>` of the
   :xref:`archive you just downloaded <AAAAAA-zip-archive>`
#. Type :command:`python` and hit :kbd:`return`
#. Copy-paste the following and hit :kbd:`return`

   .. code-block:: python

      import datetime  # Lets you work with dates and times
      import decimal  # Lets you work with $$.¢¢
      from src.AAAAAA.ledger import Transaction  # From AAAAAA codebase
      my_transaction = Transaction(
          when=datetime.date(1994, 6, 19), total_amount=decimal.Decimal('24.48'),
          kind='Buy', symbol='ALNOKI', num_shares=12)

#. You just paid $24.48 for 12 :xref:`shares <finance-share>`

   .. code-block:: python

      my_transaction.per_share_amount  # How much does each one cost?

.. Example code here should not require any packages beyond base miniconda

Congratulations!!!

.. tip::

   Hit the :guilabel:`Next` button at the top or the bottom of the page to
   continue
