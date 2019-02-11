.. 5863379

.. _concepts-code:


####
Code
####

.. note::

   The :ref:`Tools: Anaconda <tools-anaconda>` section explains how
   :ref:`Python and it associated packages <tools-anaconda>` work and the
   :ref:`user guide <guide-intro>` is a walkthrough of software features, but
   this is an elaboration of the specific components in :term:`AAAAAA` from a
   developer's perspective


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

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :pep:`257`, :ref:`Docstring <python:tut-docstrings>` conventions
   :pep:`484`, Syntax to annotate :std:doc:`types <python:library/stdtypes>`
   :std:ref:`NumPy docstrings <numpy:format>`, "
   :ref:`Docstring <python:tut-docstrings>` style"

Code is enhanced with :ref:`docstrings <python:tut-docstrings>` and
:pep:`type annotations <484>`, which enable :ref:`napoleon <tools-napoleon>` to
create pretty documentation elements that explain code:

.. py:function:: explanation(what, who, how, where, when, how_many)

   Explain something to somebody in a certain way at a certain place on a
   certain day, a certain number of timey times

   :param object what: are you trying to explain?
   :param str who: even cares?
   :param str how: you gon' do that?
   :param str where: are you 'splaining it?
   :param datetime.date when: do we receive the coupons you promised?
   :param int how_many: times you gon' do dis befo' I smack-a-you?
   :return: with newfound knowledge
   :rtype: str
   :raises ValueError: if the explanaion is not understood
   :raises TypeError: if the explanation is in the wrong language

.. attention::
   We interrupt your drooling to return to :xref:`alnoki <alnoki-repos>`
   addressing you in the second person

If you click :guilabel:`[source]`, you will be taken to the original code. Once
you are there, if you click :guilabel:`[docs]`, you will be taken back to
documentation

Conveniently, documentation elements can be created with simple
:ref:`reST directives <tools-restructured-text>` like:

.. code-block:: rest

   .. autoclass:: AAAAAA.ledger.Transaction