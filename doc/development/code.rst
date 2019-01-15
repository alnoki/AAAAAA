####
Code
####


*****
Style
*****

#. :xref:`Python` code is written according to :pep:`8`, with emphasis on:

   * Lines should be a maximum length of 79 characters, except
     :ref:`comments <python:comments>` and
     :ref:`docstrings <python:tut-docstrings>` [#]_ , which should be a maximum
     of 72 characters
   * Two spaces should precede a comment

   .. docstrings

#. Per a recommended :xref:`Python-quote-convention`::

       symbol_like = 'begin_index'  # Symbol-like term
       natural = "Documentation optimality"  # Natural language message


******
Access
******

:term:`AAAAAA` source code is available at the :xref:`AAAAAA-repo`, and
:xref:`alnoki-repos` contain some additional content from relevant tutorials


*********
Structure
*********

The :xref:`AAAAAA-repo` has several top-level directories of particular
importance:

#. ``src``: Source code
#. ``test``: :std:doc:`pytest <pytest:index>` modules for testing source code
#. ``doc``: Documentation created via
   :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
#. ``nbs``: :xref:`Jupyter Notebook <Jupyter>` documentation of ``src`` and
   ``dev`` (nbs = ``notebooks``)

   * ``dev`` includes walkthroughs done during experimental code creation
   * ``src`` includes some documentation created before the use of
     :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
     was adopted

Additional contents of the :xref:`AAAAAA-repo`, which can be manipulated in
:xref:`VS-Code` [#]_:

#. ``.vscode`` directory contains development
   :xref:`settings <VS-Code-settings>`
#. ``.gitignore`` is used for :xref:`version control <git-manual>`
#. ``README.md`` contains references to :term:`AAAAAA` documentation
#. ``TODO.md`` contains planned development tasks

.. rubric:: Footnotes

.. [#] See :pep:`257` for :ref:`docstrings <python:tut-docstrings>` conventions
.. [#] See :ref:`tools` and :ref:`references` for more :xref:`VS-Code` info