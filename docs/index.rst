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
:py:func:`python:print`:

#. Open the command line on your specific machine

   * :program:`Terminal` on a :xref:`Mac`
   * :program:`Command Prompt` on :xref:`Windows`
   * If using :xref:`Linux`, you probably already know where to look...

#. Type :command:`python` and hit :kbd:`return`
#. Copy and paste the below contents to the command line then hit
   :kbd:`return`::

    print("I am a computer programmer!")

#. If you are feeling fancy::

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

   ::

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

.. toctree::
   :caption: Development
   :maxdepth: -1
   :numbered:

   development/zen
   development/tools
   development/code
   development/documentation
   development/tasks/index
   references

..  Indices and tables
    ==================

..  * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
