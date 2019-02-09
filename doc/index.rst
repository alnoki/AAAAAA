.. 14a4fa4


########
Welcome!
########


********************************************************************
Alnoki's Algorithmic Analysis Asset Allocation Applications (AAAAAA)
********************************************************************

*Brought to you by alnoki*

.. glossary::

   AAAAAA
      Alnoki's Algorithmic Analysis Asset Allocation Applications (AAAAAA) are
      a growing collection of financial analysis tools. Development is
      performed in the :xref:`Python` computer language, using additional
      :ref:`packages <conda:concept-conda-package>` developed by the
      :xref:`open-source` community


*******
Python?
*******

A bit of :xref:`Python` can be executed on most computers with minimal effort,
using :py:func:`python:print`:

#. Open the command line on your specific machine:

.. csv-table::
   :header: :xref:`OS` , "Command line"
   :align: center

   :xref:`Mac`, Terminal
   :xref:`Windows`, Command Prompt
   :xref:`Linux`, Terminal

#. Type :command:`python` and hit :kbd:`return`

   #. If this doesn't work then you probably don't have :xref:`Python`, but you
      can get it for free!

      #. Download
         :std:doc:`Miniconda <conda:user-guide/install/download>`
      #. :ref:`Start up conda <conda:starting-conda>`
      #. Type :command:`python` and hit :kbd:`return`

#. Copy and paste the below contents to the command line then hit
   :kbd:`return`:

   .. code-block:: python

      print("I am a computer programmer!")

#. If you are feeling fancy:

   .. code-block:: python

      for i in range(5):
          print("Please be aware of the number", i)

   .. tip::
      This :xref:`Python` input ends with an indented line, so hit
      :kbd:`return` twice after copy-pasting the above contents

#. How about some :xref:`factorials <factorial-definition>`?  The "factorial of
   x" is represented by:

   .. math::
      x! = \begin{cases}
               1 & x = 0 \\
               \displaystyle \prod_{k=1}^{x} k & x > 0 \\
            \end{cases}

   .. code-block:: python

      factorial = 1  # Initialize factorial
      for x in range(10):
          if x > 0:
              factorial = x * factorial  # Update factorial
              print("Please be aware of the number", x,
                     "with factorial", factorial)

   .. note::
      This :xref:`Python` input ends with an indented line, so don't forget to
      hit :kbd:`return` twice

Congratulations!!!

.. tip::
   Hit the :guilabel:`Next` button at the top or the bottom of the page to
   continue


******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :caption: Getting started
   :maxdepth: 2
   :numbered:

   getting-started/quickstart
   getting-started/what-next
   getting-started/references/index


.. toctree::
   :caption: User guide
   :maxdepth: 2
   :numbered:

   user-guide/index
   user-guide/fundamentals
   user-guide/versions

.. toctree::
   :caption: Developer guide
   :maxdepth: 2
   :numbered:

   dev-guide/environment/index
   dev-guide/concepts/index
   dev-guide/procedures/index



