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

Documentation structure
=======================

.. code-block:: none

   AAAAAA/
       doc/
           exts/
               xref.py
               ...
           conf.py
           Makefile
           make.bat
           index.rst
           procedures/
           setup/
               quickstart.rst
               developer.rst
               ...
               concepts/
                   project-structure.rst
                   tools.rst
                   ...
           ...

.. csv-table::
   :header: "Name", "Function"
   :align: center

   ``exts/``, ":xref:`Directory <directory>` for
   :std:doc:`extensions <sphinx:usage/extensions/index>`"
   ``conf.py``, :std:doc:`Configuration <sphinx:usage/configuration>`
   "``Makefile`` , ``make.bat``", :ref:`sphinx-building-documentation`
   ``index.rst`` , :term:`AAAAAA` documentation homepage
   "``procedures/`` , ``setup/``, etc.", "
   Documentation :xref:`directories <directory>`"
   "``quickstart.rst`` , ``developer.rst`` , etc. ", "
   :ref:`tools-restructured-text` files"

.. _concepts-documentation-style:

Style
=====

:term:`AAAAAA` adopt stylistic recommendations from common sources, with some
particular emphases:

.. csv-table:: Style references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   General :ref:`reST <tools-restructured-text>` style guide"
   :xref:`Doc8`, ":ref:`Conda package <tools-anaconda>` to check
   :ref:`reST <tools-restructured-text>` style [#]_"

.. rubric:: Footnotes

.. [#] Automatically runs via the :xref:`RST-preview-ext` for
   :ref:`tools-vs-code`

General syntax
--------------

#. :ref:`Labels <ref-role>` should be lowercase hyphenated, and should use
   similar categorical naming when possible:

   * ``tools-anaconda``
   * ``git-view-project-log``

#. See :ref:`the packages table <concepts-packages-table>` for some sample
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate line
   breaks
#. :ref:`Link <references-links>` capitalization should be natural with regard
   to the rest of the sentence

   * :ref:`Links <references-links>` are here
   * Here are some :ref:`links <references-links>`

#. There should be non-link text between two different links so that the links
   can clearly be differentiated:

   .. csv-table::
      :header: Yes, NO!!!
      :align: center

      ":std:doc:`Extensions <sphinx:usage/extensions/index>` for
      :std:doc:`Sphinx <sphinx:intro>`", ":std:doc:`Sphinx <sphinx:intro>`
      :std:doc:`extensions <sphinx:usage/extensions/index>`"

Whitespace
----------

#. Indent 3 spaces (especially for
   :xref:`nested lists <reST-list-indentation>`)
#. Lines should be a maximum length of 79 characters, unless
   :std:doc:`role content <sphinx:usage/restructuredtext/roles>` can't be
   broken up (this is okay)
#. Use 2 lines of whitespace above anything that is
   :std:doc:`overlined <py-dev-guide:documenting>`
#. Use a single, unescaped space before
   :std:doc:`footnotes <sphinx:usage/restructuredtext/basics>`

.. _concepts-documentation-example:

Simple example
==============

.. note::
   Per the :ref:`proofreading procedures <writing-proofread>`, there should be
   a :std:doc:`reST comment <usage/restructuredtext/basics>` with
   a :ref:`SHA-1 <tools-git>` tag at the top of
   :ref:`.rst <tools-restructured-text>` files that have been proofread

.. code-block:: rest

   .. f00cafe

   .. _my-label:


   ##########
   Part title
   ##########

   Welcome to this document! Don't forget the double overline!

   #. Item 1
   #. Item 2 (no vertical whitespace)

      #. Item 3 (needs vertical whitespace)


   *************
   Chapter title
   *************

   Welcome to this section! Don't forget the double overline! [#]_

   Section title
   =============

   Welcome to this section. No double overline needed here!

   Subsection title
   ----------------
   Welcome to this subsection. No double overline needed here!

   .. rubric:: Footnotes

   .. [#] Footnote from the above section

.. tip::
   The :ref:`.rst <tools-restructured-text>` files in :term:`AAAAAA` should
   clearly portray other relevant stylistic components. Look around in them for
   more examples


*****************
Jupyter Notebooks
*****************

.. note::

   The :ref:`Tools: Jupyter <tools-jupyter>` section explains how
   :ref:`Jupyter <tools-Jupyter>` works, but is an elaboration of the specific
   components in :term:`AAAAAA`

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
