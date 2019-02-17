.. 0.3.0

.. _concepts-documentation:


#############
Documentation
#############

.. contents:: Contents
   :local:

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "Official
   :xref:`Python` guide to documenting"
   :xref:`RealPython guide to documenting Python <documenting-python>`, "
   General :xref:`Python` documentation practices"


******
Sphinx
******

.. note::

   The :ref:`Tools: Sphinx <tools-sphinx>` section explains how
   :ref:`Sphinx <tools-sphinx>` works, but this is an elaboration of
   specific documentation components in :term:`AAAAAA`

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
                what-next.rst
                references/
                    index.rst
                    refs.bib
                    books.rst
                    links.rst
            user-guide/
                index.rst
                fundamentals.rst
                ...
            dev-guide/
                environment/
                    index.rst
                    documenting.rst
                    ...
                concepts/
                    index.rst
                    tools.rst
                    ...
                procedures/
                    index.rst
                    conda.rst
                    ...

.. csv-table::
   :header: Name, Function
   :align: center

   ``exts/``, ":xref:`Directory <directory>` for
   :doc:`extensions <sphinx:usage/extensions/index>`"
   ``conf.py``, ":doc:`Configuration <sphinx:usage/configuration>` for
   :ref:`tools-sphinx`"
   "``Makefile`` , ``make.bat``", :ref:`sphinx-building-documentation`
   ``index.rst`` (top-level) , ":term:`AAAAAA` documentation
   :xref:`homepage <webpage>`"
   "``getting-started/`` , ``user-guide/``, etc.", "
   Documentation :xref:`directories <directory>`"
   "``quickstart.rst`` , ``what-next.rst`` , etc. ", "
   :ref:`tools-restructured-text` documents"
   ``refs.bib``, ":xref:`Citations <citation>` for
   :ref:`books <references-books>` (in :ref:`tools-bibtex` format)"

.. _concepts-documentation-style:

Style
=====

:term:`AAAAAA` adopt stylistic recommendations from common sources, with some
particular emphases:

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-restructured-text`, :term:`AAAAAA` conceptual explanation
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
#. Use :ref:`labels <sphinx:ref-role>` (``:ref:``) to reference content within
   :term:`AAAAAA` rather than specific :ref:`.rst <tools-restructured-text>`
   (``:doc:``) refrences, since the
   :ref:`toctrees <sphinx:toctree-directive>` are constantly evolving
#. :ref:`Labels <sphinx:ref-role>` should be ``lowercase-hyphenated``, and
   should use similar categorical naming when possible:

   * ``tools-anaconda``
   * ``git-view-project-log``

     .. tip::

        You can inspect all :ref:`labels <sphinx:ref-role>` in :term:`AAAAAA`
        via the :ref:`updating labels procedure <sphinx-update-labels>`

#. See the :ref:`a6 packages table <concepts-packages-table>` for some sample
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate line
   breaks

   * You should only need ``"`` in :ref:`csv-tables <sphinx:table-directives>`
     to escape line breaks for data entries, so don't use them for the
     :doc:`directive options <sphinx:usage/restructuredtext/directives>`
     listed after ``:header:`` (even if the ``:header:``
     :doc:`directive options <sphinx:usage/restructuredtext/directives>` have
     a line break)

#. There should be regular text between two different
   :ref:`links <references-links>` so that the
   :ref:`links <references-links>` can clearly be differentiated:

   .. csv-table::
      :header: Yes, NO!!!
      :align: center

      ":doc:`Extensions <sphinx:usage/extensions/index>` for
      :doc:`Sphinx <sphinx:intro>`", ":doc:`Sphinx <sphinx:intro>`
      :doc:`extensions <sphinx:usage/extensions/index>`"

#. :ref:`Link <references-links>` capitalization should be natural with regard
   to the rest of the sentence, unless the thing you are describing has special
   capitalization

   * :ref:`Links <references-links>` are here, but here are
     :ref:`links <references-links>`
   * The :doc:`NumPy package <numpy:about>` thinks it is special
   * :doc:`pytest <pytest:index>` does too
   * Not 100% sure about :ref:`napoleon <tools-napoleon>`
     (or it is :ref:`tools-napoleon`???)

     .. csv-table:: Common Conceptual Capitalizations (C\ :superscript:`3`)
        :header: Beginning of sentence, Elsewhere
        :align: center

        :doc:`NumPy <numpy:about>`, :doc:`NumPy <numpy:about>`
        :doc:`pytest <pytest:index>`, :doc:`pytest <pytest:index>`
        :ref:`Python <tools-python>`, :ref:`Python <tools-python>`
        :ref:`Anaconda <tools-anaconda>`, :ref:`Anaconda <tools-anaconda>`
        :ref:`Conda <tools-anaconda>`, :ref:`conda <tools-anaconda>`
        :ref:`tools-napoleon`, :ref:`napoleon <tools-napoleon>`
        :xref:`internet`, :xref:`internet`
        :xref:`Open-source <open-source>`, :xref:`open-source <open-source>`

Whitespace
----------

#. Use a blank line at the end of :ref:`.rst <tools-restructured-text>`
   documents
#. Indent 3 spaces (especially for
   :xref:`nested lists <reST-list-indentation>`)
#. Lines should be a maximum length of 79 characters, unless

   * :doc:`Role content <sphinx:usage/restructuredtext/roles>` can't be broken
     up
   * You are using a :rst:dir:`code-block` that itself conforms to :pep:`8` or
     similar

#. Use 2 lines of whitespace above anything that is
   :doc:`overlined <py-dev-guide:documenting>`
#. Use a single, unescaped space before
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`
#. Use a blank line after most
   :doc:`directives <sphinx:usage/restructuredtext/directives>`, like in an
   :xref:`admonition <admonition>`
#. Indent a single space after ``#.`` or after ``*``

   .. note::

      If using a
      :doc:`directive <sphinx:usage/restructuredtext/directives>` underneath
      ``#.`` or ``*``, make sure
      its ``..`` aligns with the text that is singly-spaced after ``#.`` or
      ``*``

.. _concepts-documentation-example:

Simple example
==============

Per the :ref:`proofreading procedures <writing-proofread>`, there should be
a :doc:`reST comment <usage/restructuredtext/basics>` with a
:ref:`version number <version-list>` tag (in the form of a
:doc:`reST comment <usage/restructuredtext/basics>`)  at the top of
:ref:`.rst <tools-restructured-text>` documents

.. literalinclude:: sample-doc.rst
   :language: rest
   :lines: 5-

.. tip::

   The :ref:`.rst <tools-restructured-text>` documents in :term:`AAAAAA` should
   clearly portray other relevant stylistic components. Look around in them for
   more examples


*****************
Jupyter Notebooks
*****************

.. note::

   The :ref:`Tools: Jupyter <tools-jupyter>` section explains how
   :ref:`Jupyter <tools-Jupyter>` works, but this is an elaboration of
   specific components in :term:`AAAAAA`

.. _concepts-jupyter-nbs-structure:

.. code-block:: none

   AAAAAA/
       nbs/
           dev/
               ledger.ipynb
           src/
               ledger.ipynb
               utilities.ipynb

.. csv-table::
   :header: Name, Function
   :align: center

   ``dev/``, Created during development
   ``src/``, Complements :ref:`source code <guide-intro>`
   "``ledger.ipynb``, ``utilities.ipynb``, etc.", "
   :ref:`Jupyter Notebooks <tools-jupyter>`"

.. tip::
   This :xref:`AAAAAA-nbs` opens at the ``nbs/`` :xref:`directory <directory>`
   and can render any :ref:`Jupyter Notebook <tools-jupyter>` in the
   :xref:`AAAAAA-repo`
