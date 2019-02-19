.. 0.3.0


########
Welcome!
########


********************************************************************
Alnoki's Algorithmic Analysis Asset Allocation Applications (AAAAAA)
********************************************************************

*Brought to you by alnoki*

.. glossary::

   AAAAAA
      :xref:`Alnoki <alnoki-repos>`'s Algorithmic Analysis Asset Allocation
      Applications (AAAAAA), colloquially referred to as *alnoki's apps*, are a
      growing collection of :ref:`financial analysis <user-fin-background>`
      tools. :xref:`source-code` is written in the
      :xref:`Python computer language <Python>`, using additional
      :ref:`packages <python:tut-packages>` developed by the
      :xref:`open-source` community


*******
Python?
*******

A bit of :xref:`Python` can be executed on most :xref:`computers <computer>`
with minimal effort, using :py:func:`python:print`:

#. Open the :xref:`command line <command-line>` on your
   :xref:`computer <computer>`:

.. csv-table::
   :header: :xref:`OS` , Command line
   :align: center

   :xref:`Linux`, :program:`Terminal`
   :xref:`Mac`, :program:`Terminal`
   :xref:`Windows`, :program:`Command Prompt`

#. Type :command:`python` and hit :kbd:`return`

   #. If this doesn't work then you probably don't have :xref:`Python`, but you
      can get it for :xref:`free <money`!

      #. Download
         :doc:`Miniconda <conda:user-guide/install/download>`
      #. :ref:`Start up Conda <conda:starting-conda>`
      #. Type :command:`python` and hit :kbd:`return`

         * Rejoice, for you have just started the
           :doc:`Python interpreter <tutorial/interpreter>`

#. :xref:`Copy and paste <copy-paste>` the below contents to the
   :xref:`command line <command-line>` then hit :kbd:`return`:

   .. code-block:: python

      print("I am a computer programmer!")

#. If you are feeling fancy:

   .. code-block:: python

      for i in range(5):
          print("Please be aware of the number", i)

   * This :xref:`Python` input ends with an indented line, so hit
     :kbd:`return` twice after :xref:`copy-pasting <copy-paste>` the above
     contents

#. How about some :xref:`factorials <factorial-definition>`?  The
   ":xref:`factorial <factorial-definition>` of x" is represented by:

   .. math::

      x! = \begin{cases}
               1 & x = 0 \\
               \displaystyle \prod_{ k = 1 } ^ { x } k & x > 0 \\
            \end{cases}

   .. code-block:: python

      factorial = 1  # Initialize factorial
      for x in range(10):
          if x > 0:
              factorial = x * factorial  # Update factorial
              print("Please be aware of the number", x,
                     "with factorial", factorial)

   .. admonition:: Don't forget

      This :xref:`Python` input ends with an indented line, so hit
      :kbd:`return` twice

Congratulations!!!

.. tip::

   Hit the :guilabel:`Next` button at the top or the bottom of this
   :xref:`webpage <webpage` to continue


******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`search`

.. * :ref:`modindex` goes in between the two above

.. toctree::
   :caption: Getting started
   :maxdepth: 1
   :numbered:

   getting-started/quickstart
   getting-started/examples
   getting-started/what-next
   getting-started/references/index

.. toctree::
   :caption: User guide
   :maxdepth: 1
   :numbered:

   user-guide/index
   user-guide/fundamentals
   user-guide/version-list

.. toctree::
   :caption: Developer guide
   :maxdepth: 1
   :numbered:

   dev-guide/index
   dev-guide/environment/index
   dev-guide/concepts/index
   dev-guide/testing/index
   dev-guide/distributing/index
   dev-guide/procedures/index
