###########
Basic setup
###########

If you just want to try out some basic :term:`AAAAAA` functionality, then
follow the below steps. Afterwards, if you want to re-create the development
environment that :xref:`alnoki <alnoki-repos>` uses, there are some additional
steps for you on the following pages

#. Download the :std:doc:`Miniconda variant <conda:user-guide/install/index>`
   of :xref:`Anaconda`, which will give you quick access to :xref:`Python` if
   your machine did not come pre-loaded with it
#. Download the :xref:`AAAAAA-zip-archive` and open the command line from
   inside the root directory of the project
#. Type :command:`python` and hit :kbd:`return`
#. Copy-paste the following and hit :kbd:`return`::

       import datetime  # Lets you work with dates and times
       from src.ledger import Transaction  # From AAAAAA codebase
       my_transaction = Transaction(
           date=datetime.date(1994, 6, 19), total_amount=50, transact_type='Buy',
           symbol='ALNOKI', num_shares=1)

#. Play around with some commands like::

       my_transaction.symbol  # What was that symbol again?

Congratulations!!!
