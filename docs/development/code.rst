####
Code
####


*****
Style
*****

#. :pep:`8` for :xref:`Python` code, with emphasis on:

   * Lines should be a maximum length of 79 characters, except comments or
     docstrings, which should be a maximum of 72 characters
   * Two spaces before a comment

#. Per :xref:`Python-quote-convention`::

       symbol_like = 'begin_index'  # Symbol-like term
       natural = "Documentation optimality"  # Natural language message



******
Access
******

AAAAAA source code is available at the :xref:`AAAAAA-repo`, and
:xref:`alnoki-repos` contain some additional content from relevant tutorials


*********
Structure
*********

#. ``src``: Source code
#. ``test``: :std:doc:`pytest <pytest:index>` modules for testing source code
#. ``docs``: Documentation created via
   :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
#. ``nbs``: :xref:`Jupyter Notebook <Jupyter>` documentation of ``src`` and
   ``dev`` (nbs = ``notebooks``)

   * ``dev`` includes walkthroughs done during experimental code creation
   * ``src`` includes some documentation created before the adoption of using
     :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`