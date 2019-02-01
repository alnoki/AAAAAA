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


********
Napoleon
********

Example
=======

If you participated in the :ref:`quick start <setup-quickstart>`, then you
initialized (link_needed) an instance (link_needed) of
:py:class:`~AAAAAA.ledger.Transaction`, which is itself a class (link_needed)

The code for :py:class:`~AAAAAA.ledger.Transaction` is enhanced with
:ref:`docstrings <python:tut-docstrings>` and :PEP:`type annotations <484>`,
which enable the Sphinx Napoleon extension (link_needed) to create an
autoclass (link_needed) documentation element:

.. autoclass:: AAAAAA.ledger.Transaction
   :members: __init__

.. attention::
   We interrupt your drooling to return to :xref:`alnoki <alnoki-repos>`
   addressing you in the second person

If you click :guilabel:`[source]`, you will be taken to the original code. Once
you are there, if you click :guilabel:`[docs]`, you will be taken back to the
autoclass (link_needed) documentation element

Specifics
=========

Conveniently, the autoclass (link_needed) documentation element is
created with a simple :ref:`reST directive <tools-restructured-text>` specified
in the autodoc extension (link_needed):

.. code-block:: rest

   .. autoclass:: AAAAAA.ledger.Transaction
      :members: __init__

Code uses NumPy style docstrings (link_needed) instead of traditional autodoc
style docstrings (link_needed), so :term:`AAAAAA` use the Napolen extension
(link_needed) to convert :ref:`docstrings <python:tut-docstrings>` in a way
that enables the use of autodoc directives (link_needed)


.. Configuring
.. ===========

.. Should talk about how conf.py got set up and use the package links to
   explain

