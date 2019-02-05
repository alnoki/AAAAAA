.. 5863379

.. _concepts-code:


####
Code
####


*********
Structure
*********

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`python:tut-packages`, :xref:`Directory <directory>` structuring
   :std:doc:`pytest:goodpractices`, Integrating :ref:`test code <tools-pytest>`

In accordance with :std:doc:`test code recommendations <pytest:goodpractices>`,
:term:`AAAAAA` code is structured as follows:

.. code-block:: none

   AAAAAA/
       setup.py
       src/
           AAAAAA/
               __init__.py
               ledger.py
               utilities.py
               ...
       test/
           test_ledger.py
           test_utilities.py
           ...


*****
Style
*****

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :pep:`8`, Official :xref:`Python` style guide
   :pep:`257`, :ref:`docstring <python:tut-docstrings>` conventions

#. Items of particuar emphasis:

   * Lines should be a maximum length of 79 characters, except
     :ref:`comments <python:comments>` and
     :ref:`docstrings <python:tut-docstrings>`, which should be a maximum
     of 72 characters
   * Two spaces should precede a :ref:`comment <python:comments>`

#. Per a recommended :xref:`Python-quote-convention`:

   .. code-block:: python

      symbol_like = 'begin_index'  # Symbol-like term
      natural = "Documentation optimality"  # Natural language message


.. _concepts-code-e4:

**********************************************************************
Elaborately Embellished Explanatory Enhancements (E\ :superscript:`4`)
**********************************************************************

Code is enhanced with :ref:`docstrings <python:tut-docstrings>` and
:pep:`type annotations <484>`, which enable :ref:`napoleon <tools-napoleon>` to
create pretty documentation elements that explain code:

.. autoclass:: AAAAAA.ledger.Transaction
   :members: __init__

.. attention::
   We interrupt your drooling to return to :xref:`alnoki <alnoki-repos>`
   addressing you in the second person

If you click :guilabel:`[source]`, you will be taken to the original code. Once
you are there, if you click :guilabel:`[docs]`, you will be taken back to
documentation

Conveniently, documentation elements are created with simple
:ref:`reST directives <tools-restructured-text>`. As long as you follow very
specific :ref:`formatting and syntax rules <tools-napoleon>`, all you need to
re-create the above example is:

.. code-block:: rest

   .. autoclass:: AAAAAA.ledger.Transaction
      :members: __init__
