.. _concepts-code:


####
Code
####

.. note::

   The :ref:`concepts-tools` section explains general :ref:`tools-python` and
   :ref:`tools-pytest` concepts, the :ref:`user guide <user-intro>` is a
   walkthrough of :xref:`software <software>` features in :term:`AAAAAA`,
   and the :ref:`testing <testing-intro>` section is a walkthrough of
   :ref:`pytest code <tools-pytest>`, but this is an elaboration of
   specific components in :term:`AAAAAA` from a
   :wiki-pg:`developer <Programmer>`'s perspective

.. contents::
   :local:

.. _concepts-code-tree:


*********
Structure
*********

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-python`, Conceptual explanation
   :ref:`tools-pytest`, Conceptual explanation
   :ref:`User guide <user-intro>`, Walkthrough
   :ref:`testing-intro`, Walkthrough

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :ref:`python:tut-packages`, :xref:`Directory <directory>` structuring
   :doc:`pytest:goodpractices`, Integrating :ref:`test code <tools-pytest>`

In accordance with :ref:`pytest configuration specifications <configs-pytest>`,
:term:`AAAAAA` are structured as follows:

.. code-block:: none

   AAAAAA/
       src/
           AAAAAA/
               __init__.py
               ledger.py
       test/
           test_ledger.py
           test_utilities.py
       setup.py

.. csv-table::
   :align: center
   :header: Name, Function

   ``src/AAAAAA/``, :ref:`Python source code <tools-python>`
   ``test/``, :ref:`pytest test code <tools-pytest>`
   ``setup.py``, :ref:`pytest configuration <configs-pytest>`

.. _concepts-code-style:


*****
Style
*****

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :pep:`8`, Official :ref:`tools-python` style guide
   :pep:`257`, :ref:`Docstring <python:tut-docstrings>` conventions

#. Items of particular emphasis:

   * :wiki-pg:`Lines <Line_(text_file)>` should be a maximum length of 79
     :wiki-pg:`characters <Character_(computing)>`, except
     :ref:`comments <python:comments>` and
     :ref:`docstrings <python:tut-docstrings>`, which should be a maximum
     of 72 :wiki-pg:`characters <Character_(computing)>`

     * The :ref:`VS Code ruler settings <configs-vs-code>` help with this

   * Two :wiki-pg:`spaces <Whitespace_character>` should precede a
     :ref:`comment <python:comments>`

#. Per a recommended
   :stack-q:`Python quote convention
   <56011/single-quotes-vs-double-quotes-in-python>`:

   .. code-block:: python

      symbol_like = 'begin_index'  # Symbol-like term
      natural = "Documentation optimality"  # Natural language message

.. _concepts-code-e4:


**********************************************************************
Elaborately Embellished Explanatory Enhancements (E\ :superscript:`4`)
**********************************************************************

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-napoleon`, Conceptual explanation
   :ref:`Napoleon procedures <procedures-napoleon>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :pep:`257`, :ref:`Docstring <python:tut-docstrings>` conventions
   :pep:`484`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>` to indicate
   :doc:`types <python:library/stdtypes>`"
   :ref:`NumPy docstrings <numpy:format>`, "
   :ref:`Docstring <python:tut-docstrings>` style"
   :ref:`Python domain <sphinx:python-roles>`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` guide"

:ref:`Source code <tools-Python>` is enhanced with
:pep:`type annotations <484>` and :ref:`docstrings <python:tut-docstrings>`
containing :ref:`Python domain <sphinx:python-roles>` components for
:ref:`reST <tools-restructured-text>`, so that
:ref:`napoleon <tools-napoleon>` can create pretty
:wiki-pg:`documentation <Software_documentation>` elements that explain
:xref:`source code <source-code>`, like this
:ref:`info field list <sphinx:info-field-lists>`:

.. py:function:: explanation(what, who, how, where, when, how_many)

   Explain something to somebody in a certain way at a certain place on a
   certain :wiki-pg:`day <ISO_8601>`, a certain number of
   :wiki-pg:`timey times <Time>`

   :param object what: are you trying to explain?
   :param str who: even cares?
   :param str how: you gon' do that?
   :param str where: are you 'splaining it?
   :param datetime.date when: do we receive the coupons you promised?
   :param int how_many: parcels of knowledge?
   :return: with newfound knowledge
   :rtype: object
   :raises ValueError: if the explanation is not understood
   :raises TypeError: if the explanation is in the wrong language

.. attention::

   We interrupt your drooling to return to :github:`alnoki`

Conveniently, :wiki-pg:`documentation <Software_documentation>` elements can
be created with simple :ref:`reST directives <tools-restructured-text>` like:

.. code-block:: rest

   .. autoclass:: AAAAAA.ledger.Transaction

After a :wiki-pg:`documentation <Software_documentation>` element has been
created, it can be referenced using the
:ref:`Python domain <sphinx:python-roles>`:

.. code-block:: rest
   :caption: Let's talk about :py:class:`AAAAAA.ledger.Transaction`

   Let's talk about :py:class:`AAAAAA.ledger.Transaction`

Real :ref:`concepts-code-e4`, like the example below, also have a
:guilabel:`[source]` feature that :xref:`links <URL>` directly to
:xref:`source code <source-code>`, except when viewing
:wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA` in
:ref:`PDF format <dist-doc-pdf>`

.. admonition:: Example

   :py:class:`AAAAAA.ledger.Transaction` (<- yes, that's a :xref:`link <URL>`)
