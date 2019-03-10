.. 0.3.0


########
Welcome!
########


********************************************************************
Alnoki's Algorithmic Analysis Asset Allocation Applications (AAAAAA)
********************************************************************

*Brought to you by alnoki*

What are they?
==============

.. glossary::

   AAAAAA
      :github:`Alnoki <alnoki>`'s :wiki-pg:`Algorithmic <Algorithm>`
      Analysis :wiki-pg:`Asset Allocation <Financial_asset>` Applications
      (AAAAAA or :wiki-pg:`double-triple Alfa <NATO_phonetic_alphabet>`),
      colloquially referred to as *alnoki's apps*, are a growing collection of
      :wiki-pg:`financial <Finance>` analysis
      :wiki-pg:`software <Software>` tools.
      :wiki-pg:`Source code <Source_code>` is written in the
      :xref:`Python computer language <Python>`, and uses
      :ref:`packages <python:tut-packages>` that have been
      :wiki-pg:`developed <Software_development>` by the
      :wiki-pg:`open-source <Open-source_software>` community

Python?
=======

You can use a bit of :xref:`Python` on most :xref:`computers <computer>` with
minimal effort, using :py:func:`python:print`:

#. Open the :xref:`command line <command-line>` on your
   :xref:`computer <computer>`:

.. csv-table::
   :align: center
   :header: :xref:`OS` , :wiki-pg:`Command line <Command_line>`

   :wiki-pg:`Linux`, :program:`Terminal`
   :wiki-pg:`Mac <Macintosh_operating_systems>`, :program:`Terminal`
   :wiki-pg:`Windows <Microsoft_Windows>`, :program:`Command Prompt`

#. :wiki-pg:`Type <Typing>` :command:`python` then :wiki-pg:`type <Typing>`
   :kbd:`return`

   #. If this doesn't work then you probably don't have :xref:`Python`, but you
      can get it for :xref:`free <money`!

      #. :doc:`Download Miniconda <conda:user-guide/install/download>`
      #. :ref:`Start up Conda <conda:starting-conda>`
      #. :wiki-pg:`Type <Typing>` :command:`python` then
         :wiki-pg:`type <Typing>` :kbd:`return`

         * Rejoice, for you have just started the
           :doc:`Python interpreter <tutorial/interpreter>`

#. :xref:`Copy and paste <copy-paste>` the below contents to the
   :xref:`command line <command-line>` then :wiki-pg:`type <Typing>`
   :kbd:`return`:

   .. code-block:: python

      print("I am a computer programmer!")

#. If you are feeling fancy:

   .. code-block:: python

      for i in range(5):
          print("Please be aware of the number", i)

   * This :xref:`Python` input ends with an indented
     :wiki-pg:`line of code <Source_lines_of_code>`, so
     :wiki-pg:`type <Typing>`
     :kbd:`return` twice after :xref:`copy-pasting <copy-paste>` the above
     contents

#. How about some :wiki-pg:`factorials <Factorial>`?  The
   ":wiki-pg:`factorial <Factorial>` of :math:`x`" is given by:

   .. math::

      x! = x(x-1)(x-2)\ldots

   More eloquently:

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

      This :xref:`Python` input ends with an indented
      :wiki-pg:`line of code <Source_lines_of_code>`, so
      :wiki-pg:`type <Typing>`
      :kbd:`return` twice

Congratulations!!!

.. tip::

   :wiki-pg:`Click <Point_and_click>` the :guilabel:`Next` button at the top
   or the bottom of this :xref:`webpage <webpage` to begin your journey


***************
Getting started
***************

:ref:`Here <quickstart>` is where the :term:`AAAAAA` journey begins!

.. toctree::
   :caption: Getting started
   :hidden:
   :numbered:

   getting-started/quickstart
   getting-started/examples
   getting-started/what-next


**********
User guide
**********

:ref:`Here <user-intro>` you can learn to use :term:`AAAAAA`!

.. toctree::
   :caption: User guide
   :hidden:
   :numbered:

   user-guide/index
   user-guide/transactions


***************
Developer guide
***************

:ref:`Here <dev-intro>` you can learn to create :term:`AAAAAA`!

.. toctree::
   :caption: Developer guide
   :hidden:
   :numbered:

   dev-guide/index
   dev-guide/environment/index
   dev-guide/concepts/index
   dev-guide/distributing/index
   dev-guide/testing/index
   dev-guide/procedures/index

.. _indices-and-tables:


******************
Indices and tables
******************

:ref:`Here <indices-intro>` you can review contents of :term:`AAAAAA`!

.. toctree::
   :caption: Indices
   :hidden:
   :numbered:

   indices/index
   indices/acronyms
   indices/versions
   indices/references/index
