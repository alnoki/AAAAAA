########
Welcome!
########

********************************************************************
Alnoki's Algorithmic Analysis Asset Allocation Applications (AAAAAA)
********************************************************************

*Brought to you by alnoki*

AAAAAA are a growing collection of financial analysis tools. Development is
performed in the :xref:`Python` computer language, using additional packages
developed by the open source community

*******
Python?
*******
A bit of Python can be executed on most computers with minimal effort, using
:py:func:`print`:

#. Open the command line on your specific machine

   * ``Terminal`` on a Mac
   * ``Command Prompt`` on Windows
   * If using Linux, you probably already know where to look...

#. Type :command:`python` and hit ``enter``
#. Copy and paste the below contents to the command line then hit ``enter``::

    print("I am a computer programmer!")

#. If you are feeling fancy::

    for i in range(5):
       print("Please be aware of the number", i)

   .. tip::
      Hit ``enter`` twice after copy-pasting the above contents

#. How about some :xref:`factorials <factorial-definition>`? The "factorial of
   x" is represented by:

   .. math::
      x! = \begin{cases}
               1 & x = 0 \\
               \displaystyle \prod_{k=1}^{x} & x > 0 \\
            \end{cases}

   ::

       factorial = 1  # Initialize factorial
       for x in range(10):
          if x > 0:
             factorial = x * factorial  # Update factorial
          print("Please be aware of the number", x,
                "with factorial", factorial)

   .. note::
      Don't forget to hit ``enter`` twice

Congratulations!!!

.. toctree::
   :caption: Development
   :maxdepth: -1

   development/zen
   development/tools
   development/code
   development/documentation
   development/tasks/index
   references

.. tip::
   AAAAAA ``README`` file, at the bottom of the :xref:`AAAAAA-repo`, contains
   some additional links that are commonly referenced during development as
   well as some philosophies and directory structure notes


..  Indices and tables
    ==================

..  * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
