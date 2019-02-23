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
   :xref:`Python` guide to :wiki-pg:`documenting <Software_documentation>`"
   :xref:`RealPython guide to documenting Python <documenting-python>`, "
   General :wiki-pg:`documentation <Software_documentation>` practices for
   :xref:`Python`"


******
Sphinx
******

.. note::

   The :ref:`Tools: Sphinx <tools-sphinx>` section explains how
   :ref:`Sphinx <tools-sphinx>` works, but this is an elaboration of
   specific :wiki-pg:`documentation <Software_documentation>` components in
   :term:`AAAAAA`

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
            requirements.txt
            getting-started/
                quickstart.rst
                examples.rst
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
                index.rst
                environment/
                    index.rst
                    documenting.rst
                    ...
                concepts/
                    index.rst
                    tools.rst
                    ...
                testing/
                    index.rst
                distributing/
                    index.rst
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
   ``index.rst`` (top-level) , ":xref:`homepage <webpage>` of
   :wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA`"
   "``getting-started/`` , ``user-guide/``, etc.", "
   :xref:`Directories <directory>` for
   :wiki-pg:`documentation <Software_documentation>`"
   "``quickstart.rst`` , ``what-next.rst`` , etc. ", "
   :wiki-pg:`Files <Computer_file>` with :ref:`tools-restructured-text`"
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
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate
   :wiki-pg:`line breaks <Newline>`

   * You should only need ``"`` in :ref:`csv-tables <sphinx:table-directives>`
     for :wiki-pg:`line breaks <Newline>` in data entries, so don't use them
     for the
     :doc:`directive options <sphinx:usage/restructuredtext/directives>`
     listed after ``:header:`` (even if the ``:header:``
     :doc:`directive options <sphinx:usage/restructuredtext/directives>` have
     a line break)

#. If a :doc:`directive option <sphinx:usage/restructuredtext/directives>` has
   a :wiki-pg:`line break <Newline>`, make sure to
   :wiki-pg:`indent <Indentation_(typesetting)>` the following
   :wiki-pg:`line <Source_lines_of_code>` if it starts with a
   :doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest

      .. literalinclude:: sample-doc.rst
         :caption: What the :ref:`reST <tools-restructured-text>` for
            :ref:`sample-doc.rst <sample-doc>` looks like:

   * Otherwise, simply :wiki-pg:`line break <Newline>` without
     :wiki-pg:`indenting <Indentation_(typesetting)>`

#. There should be regular :wiki-pg:`text <Character_(computing)>` between two
   different :ref:`links <references-links>` so that the
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
        :ref:`Intersphinx <tools-intersphinx>`, "
        :ref:`Intersphinx <tools-intersphinx>`"
        :xref:`Git <git-manual>`, :xref:`Git <git-manual>`
        :ref:`Miniconda <tools-anaconda>`, :ref:`Miniconda <tools-anaconda>`

Whitespace and line breaking
----------------------------

#. Use a :wiki-pg:`blank line <Newline>` at the end of
   :ref:`.rst files <tools-restructured-text>`
#. :wiki-pg:`Indent <Indentation_(typesetting)>` 3
   :wiki-pg:`spaces <Whitespace_character>` (especially for
   :xref:`nested lists <reST-list-indentation>`)
#. :wiki-pg:`Lines <Line_(text_file)>` should be a maximum length of 79
   :wiki-pg:`characters <Character_(computing)>`, unless you are using a
   :rst:dir:`code-block` that itself conforms to :pep:`8` or an appropriate
   standard

      * When you use a :wiki-pg:`line break <Newline>` for a
        :doc:`role <sphinx:usage/restructuredtext/roles>`, do it between the
        :doc:`title <sphinx:usage/restructuredtext/roles>` and the
        :doc:`target <sphinx:usage/restructuredtext/roles>`

#. Use 2 :wiki-pg:`lines <Line_(text_file)>` of
   :wiki-pg:`whitespace <Whitespace_character>` above any
   :doc:`overlined headings <py-dev-guide:documenting>`
#. Use a single :wiki-pg:`space <Whitespace_character>` before
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`
#. Use a :wiki-pg:`blank line <Line_(text_file)>` after most
   :doc:`directives <sphinx:usage/restructuredtext/directives>`, like in an
   :xref:`admonition <admonition>`
#. :wiki-pg:`Indent <Indentation_(typesetting)>` a single
   :wiki-pg:`space <Whitespace_character>` after ``#.`` or
   after ``*``

   .. note::

      If using a
      :doc:`directive <sphinx:usage/restructuredtext/directives>` underneath
      ``#.`` or ``*``, make sure
      its ``..`` :wiki-pg:`aligns <Indentation_(typesetting)>` with the
      :wiki-pg:`text <Character_(computing)>`
      that is singly-:wiki-pg:`spaced <Whitespace_character>` after ``#.``
      or ``*``

.. _concepts-documentation-example:

Simple example
==============


Per the :ref:`proofreading procedures <writing-proofread>`, there should be
a :doc:`reST comment <usage/restructuredtext/basics>` with a
:ref:`version number <version-list>` tag (in the form of a
:doc:`reST comment <usage/restructuredtext/basics>`)  at the top of
:ref:`.rst files <tools-restructured-text>`

Though it is not included in a :ref:`toctree <sphinx:toctree-directive>`, check
out :ref:`sample-doc.rst <sample-doc>`!

.. literalinclude:: sample-doc.rst
   :caption: What the :ref:`reST <tools-restructured-text>` for
      :ref:`sample-doc.rst <sample-doc>` looks like:
   :language: rest
   :lines: 3-

.. tip::

   The :ref:`.rst files <tools-restructured-text>` in :term:`AAAAAA` should
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

   ``dev/``, Created during :wiki-pg:`development <Software_development>`
   ``src/``, Complements :ref:`source code <user-intro>`
   "``ledger.ipynb``, ``utilities.ipynb``, etc.", "
   :ref:`Jupyter Notebooks <tools-jupyter>`"

.. tip::

   This :xref:`AAAAAA-nbs` opens at the ``nbs/`` :xref:`directory <directory>`
   and can render any any :xref:`Jupyter Notebook<Jupyter>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>` inside of a
   :xref:`web browser <web-browser>`, even if you don't have
   :xref:`Jupyter <Jupyter>`
