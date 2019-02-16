.. db615a5

.. _concepts-documentation:


#############
Documentation
#############

.. contents:: Contents
   :local:

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide <py-dev-guide:documenting>`, "Official
   :xref:`Python` guide to documenting"
   :xref:`RealPython guide to documenting Python <documenting-python>`, "
   General :xref:`Python` documentation practices"


******
Sphinx
******

.. note::

   The :ref:`Tools: Sphinx <tools-sphinx>` section explains how
   :ref:`Sphinx <tools-sphinx>` works, but this is an elaboration of the
   specific components in :term:`AAAAAA`

.. _concepts-documentation-structure:

Documentation structure
=======================

.. code-block:: none

    AAAAAA/
        doc/
            exts/
                xref.py
            conf.py
            Makefile
            make.bat
            index.rst
            getting-started/
                quickstart.rst
                ...
                references/
                    index.rst
                    refs.bib
                    books.rst
                    links.rst
            user-guide/
                index.rst
                fundamentals.rst
            dev-guide/
                concepts/
                    index.rst
                    tools.rst
                    ...
                environment/
                    index.rst
                    documenting.rst
                    ...
                procedures/
                    writing.rst
                    ...

.. csv-table::
   :header: Name, Function
   :align: center

   ``exts/``, ":xref:`Directory <directory>` for
   :std:doc:`extensions <sphinx:usage/extensions/index>`"
   ``conf.py``, :std:doc:`Configuration <sphinx:usage/configuration>`
   "``Makefile`` , ``make.bat``", :ref:`sphinx-building-documentation`
   ``index.rst`` (top-level) , :term:`AAAAAA` documentation homepage
   "``getting-started/`` , ``user-guide/``, etc.", "
   Documentation :xref:`directories <directory>`"
   "``quickstart.rst`` , ``fundamentals.rst`` , etc. ", "
   :ref:`tools-restructured-text` files"
   ``refs.bib``, :ref:`tools-bibtex` citations

.. _concepts-documentation-style:

General style
=============

:term:`AAAAAA` adopt stylistic recommendations from common sources, with some
particular emphases:

.. csv-table:: Style references
   :header: "Reference", "Topic"
   :align: center

   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "General
   :ref:`reST <tools-restructured-text>` style guide"
   :xref:`Doc8`, ":ref:`Conda package <tools-anaconda>` to check
   :ref:`reST <tools-restructured-text>` style [#]_"

.. rubric:: Footnotes

.. [#] Automatically runs via the :xref:`RST-preview-ext` for
   :ref:`tools-vs-code`

Specific syntax
---------------

#. Nothing should be prefixed with ``:std:`` because components of the
   :doc:`standard domain <sphinx:usage/restructuredtext/domains>` do not
   require it
#. :ref:`Labels <ref-role>` should be lowercase hyphenated, and should use
   similar categorical naming when possible:

   * ``tools-anaconda``
   * ``git-view-project-log``

#. See :ref:`the packages table <concepts-packages-table>` for some sample
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate line
   breaks

   * You should only need ``"`` in :ref:`csv-tables <sphinx:table-directives>`
     to escape line breaks, so don't use them for the
     :doc:`directive options <sphinx:usage/restructuredtext/directives>`
     listed after ``:header:``

#. :ref:`Link <references-links>` capitalization should be natural with regard
   to the rest of the sentence, unless the thing you are describing has special
   capitalization

   * :ref:`Links <references-links>` are here
   * Here are some :ref:`links <references-links>`
   * The :doc:`NumPy package <numpy:about>` thinks it is special
   * :doc:`pytest <pytest:index>` does too

#. There should be regular text between two different
   :ref:`links <references-links>` so that the
   :ref:`links <references-links>` can clearly be differentiated:

   .. csv-table::
      :header: Yes, NO!!!
      :align: center

      ":doc:`Extensions <sphinx:usage/extensions/index>` for
      :doc:`Sphinx <sphinx:intro>`", ":std:doc:`Sphinx <sphinx:intro>`
      :doc:`extensions <sphinx:usage/extensions/index>`"

Whitespace
----------

#. Indent 3 spaces (especially for
   :xref:`nested lists <reST-list-indentation>`)
#. Lines should be a maximum length of 79 characters, unless

   * :doc:`role content <sphinx:usage/restructuredtext/roles>` can't be broken up
   * You are using a :rst:dir:`code-block` that itself conforms to :pep:`8`

#. Use 2 lines of whitespace above anything that is
   :doc:`overlined <py-dev-guide:documenting>`
#. Use a single, unescaped space before
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`
#. Use a blank line after the
   :doc:`directive <sphinx:usage/restructuredtext/directives>` in an
   :xref:`admonition <admonition>`
#. Indent a single space after ``#.`` or after ``*``

.. _concepts-documentation-example:

Simple example
==============

.. note::

   Per the :ref:`proofreading procedures <writing-proofread>`, there should be
   a :doc:`reST comment <usage/restructuredtext/basics>` with a
   :ref:`version number <version-list>` tag at the top of
   :ref:`.rst <tools-restructured-text>` files

.. literalinclude:: sample-doc.rst
   :language: rest
   :lines: 5-

.. tip::

   The :ref:`.rst <tools-restructured-text>` files in :term:`AAAAAA` should
   clearly portray other relevant stylistic components. Look around in them for
   more examples


*****************
Jupyter Notebooks
*****************

.. note::

   The :ref:`Tools: Jupyter <tools-jupyter>` section explains how
   :ref:`Jupyter <tools-Jupyter>` works, but this is an elaboration of the
   specific components in :term:`AAAAAA`

.. _concepts-jupyter-nbs-structure:

.. code-block:: none

   AAAAAA/
       nbs/
           dev/
               ledger.ipynb
               ...
           src/
               ledger.ipynb
               utilities.ipynb
               ...

.. csv-table::
   :header: "Name", "Style"
   :align: center

   ``dev/``, Created during development
   ``src/``, Complements source code


.. tip::
   This :xref:`AAAAAA-nbs` opens at the ``nbs/`` directory and can render any
   :ref:`Jupyter Notebook <tools-jupyter>` in the :xref:`AAAAAA-repo`
