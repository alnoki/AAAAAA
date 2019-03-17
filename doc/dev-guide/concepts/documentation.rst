.. _concepts-doc:


#############
Documentation
#############

.. contents:: Contents
   :local:

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "Official
   :xref:`Python` guide to :wiki-pg:`documenting <Software_documentation>`"
   ":real-py:`RealPython guide to documenting Python
   <documenting-python-code>`", "
   General :wiki-pg:`documentation <Software_documentation>` practices for
   :xref:`Python`"


******
Sphinx
******

.. note::

   The :ref:`Tools: Sphinx <tools-sphinx>` section explains how
   :ref:`Sphinx <tools-sphinx>` works, but this is an elaboration of specific
   :wiki-pg:`documentation <Software_documentation>` components in
   :term:`AAAAAA`

.. _concepts-doc-tree:

Structure
=========

.. code-block:: none

    AAAAAA/
        doc/
            conf.py
            requirements.txt
            exts/
                xref.py
            Makefile
            make.bat
            index.rst
            getting-started/
                quickstart.rst
                examples.rst
                what-next.rst
            user-guide/
                index.rst
                transactions.rst
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
            indices/
                index.rst
                references/
                    ...
                    refs.bib
                    books.rst


.. csv-table::
   :align: center
   :header: Name, Function

   ``conf.py``, :ref:`Sphinx configuration <configs-conf-py>`
   ``requirements.txt``, "
   :ref:`Read the Docs configuration <configs-read-the-docs>`"
   ``exts/xref.py``, :ref:`xref Sphinx extension <tools-xref>`
   "``Makefile`` , ``make.bat``", ":ref:`sphinx-building-doc`, from
   :ref:`sphinx-quickstart <dist-doc>`"
   ``doc/index.rst`` , ":xref:`Homepage <webpage>` of
   :wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA`"
   "``getting-started/`` , ``user-guide/``, etc.", "
   :xref:`Directories <directory>` for
   :wiki-pg:`documentation <Software_documentation>` sections"
   "``quickstart.rst`` , ``what-next.rst`` , etc. ", "
   :ref:`reStructuredText files <tools-restructured-text>`"
   ``refs.bib``, ":xref:`Citations <citation>` for
   :ref:`books <references-books>` (in :ref:`tools-bibtex` format)"

.. _concepts-doc-style:

Style
=====

.. contents::
   :local:

:term:`AAAAAA` adopt stylistic recommendations from common sources, with some
particular emphases

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-restructured-text`, Conceptual explanation
   :ref:`tools-napoleon`, Conceptual explanation
   :ref:`Napoleon example <concepts-code-e4>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "General
   :ref:`reST <tools-restructured-text>` style guide"
   :conda-forge:`Doc8 reST linter <doc8>`, ":wiki-pg:`Linter <Lint_(software)>`
   for :ref:`reST <tools-restructured-text>` [#]_"

.. tip::

   The :ref:`.rst files <tools-restructured-text>` in :term:`AAAAAA` should
   clearly portray stylistic components. Look around in them for more examples
   after reviewing the below considerations

.. rubric:: Footnotes

.. [#] Automatically :wiki-pg:`runs <Execution_(computing)>` via the
   :vs-code-ext:`reStructuredText extension <lextudio.restructuredtext>` for
   :ref:`tools-vs-code`

Specific syntax
---------------

#. Nothing should be prefixed with ``:std:`` because components of the
   :doc:`standard domain <sphinx:usage/restructuredtext/domains>` do not
   require it
#. Use :ref:`labels <sphinx:ref-role>` (``:ref:``) to reference content within
   :term:`AAAAAA` rather than specific :ref:`.rst <tools-restructured-text>`
   (``:doc:``) references, in case
   :ref:`toctrees <sphinx:toctree-directive>` change
#. :ref:`Labels <sphinx:ref-role>` should be ``lowercase-hyphenated``, and
   should use similar categorical naming when possible:

   * ``tools-anaconda``
   * ``git-view-project-log``

     .. tip::

        You can inspect all :ref:`labels <sphinx:ref-role>` in :term:`AAAAAA`
        via the :ref:`updating labels procedure <sphinx-update-labels>`

#. There should be regular :wiki-pg:`text <Character_(computing)>` between two
   different :ref:`links <references-links>` so that the
   :ref:`links <references-links>` can be clearly differentiated:

   .. csv-table::
      :align: center
      :header: Yes, NO!!!

      ":doc:`Extensions <sphinx:usage/extensions/index>` for
      :doc:`Sphinx <sphinx:intro>`", ":doc:`Sphinx <sphinx:intro>`
      :doc:`extensions <sphinx:usage/extensions/index>`"

.. _concepts-doc-ccc:

Common Conceptual Capitalizations (C\ :superscript:`3`)
-------------------------------------------------------

#. :ref:`Link <references-links>` capitalization should be natural with regard
   to the rest of the sentence, unless the thing you are describing has special
   capitalization

   * :ref:`Links <references-links>` are here, but here are
     :ref:`links <references-links>`
   * The :doc:`NumPy package <numpy:about>` thinks it is special
   * :doc:`pytest <pytest:index>` does too

     .. csv-table:: Common Conceptual Capitalizations (C\ :superscript:`3`)
        :align: center
        :header: Beginning of sentence, Elsewhere

        :ref:`Anaconda <tools-anaconda>`, :ref:`Anaconda <tools-anaconda>`
        ":vs-code-doc:`Command Palette
        <getstarted/userinterface#_command-palette>`","
        :vs-code-doc:`Command Palette
        <getstarted/userinterface#_command-palette>`"
        :ref:`Conda <tools-anaconda>`, :ref:`conda <tools-anaconda>`
        :ref:`Docstrings <python:tut-docstrings>`, "
        :ref:`docstrings <python:tut-docstrings>`"
        :git-doc:`Git <user-manual>`, :git-doc:`Git <user-manual>`
        :wiki-pg:`Internet`, :wiki-pg:`Internet`
        :vs-code-doc:`Integrated terminal <editor/integrated-terminal>`, "
        :vs-code-doc:`integrated terminal <editor/integrated-terminal>`"
        :ref:`Intersphinx <tools-intersphinx>`, "
        :ref:`Intersphinx <tools-intersphinx>`"
        :github-help:`Markdown <basic-writing-and-formatting-syntax>`, "
        :github-help:`Markdown <basic-writing-and-formatting-syntax>`"
        :ref:`Miniconda <tools-anaconda>`, :ref:`Miniconda <tools-anaconda>`
        :ref:`tools-napoleon`, :ref:`napoleon <tools-napoleon>`
        :doc:`NumPy <numpy:about>`, :doc:`NumPy <numpy:about>`
        :wiki-pg:`Open-source <Open-source_software>`, "
        :wiki-pg:`open-source <Open-source_software>`"
        :doc:`pytest <pytest:index>`, :doc:`pytest <pytest:index>`
        :ref:`Python <tools-python>`, :ref:`Python <tools-python>`

.. _concepts-doc-whitespace:

Whitespace and line breaking
----------------------------

Many of these are exemplified below in the
:ref:`documentation example <concepts-doc-example>`

#. Use a :wiki-pg:`blank line <Newline>` at the end of
   :ref:`.rst files <tools-restructured-text>`
#. :wiki-pg:`Indent <Indentation_(typesetting)>` 3
   :wiki-pg:`spaces <Whitespace_character>` (especially for
   :stack-q:`nested lists
   <5550089/how-to-create-a-nested-list-in-restructuredtext>`)
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

#. Use 2 :wiki-pg:`lines <Line_(text_file)>` of
   :wiki-pg:`whitespace <Whitespace_character>` above any
   :doc:`overlined section headings <sphinx:usage/restructuredtext/basics>`
#. :wiki-pg:`Lines <Line_(text_file)>` should be a maximum length of 79
   :wiki-pg:`characters <Character_(computing)>`, unless you are using a
   :rst:dir:`code-block` that itself conforms to :pep:`8` or an appropriate
   standard. If you are using a
   :doc:`role <sphinx:usage/restructuredtext/roles>` and you need to
   :wiki-pg:`line break <Newline>`:

      #. Place the :doc:`role <sphinx:usage/restructuredtext/roles>` on its own
         :wiki-pg:`line <Line_(text_file)>`:

         .. code-block:: rest

            Use 2 :wiki-pg:`lines <Line_(text_file)>` of
            :wiki-pg:`whitespace <Whitespace_character>` above any
            :doc:`overlined section headings <sphinx:usage/restructuredtext/basics>`

      #. If the :wiki-pg:`line <Line_(text_file)>` is still too long, then
         :wiki-pg:`line break <Newline>` between
         the :doc:`title <sphinx:usage/restructuredtext/roles>` and the
         :doc:`target <sphinx:usage/restructuredtext/roles>`, with the ``<`` at
         the beginning of a :wiki-pg:`new line <Newline>`:

         .. code-block:: rest

            .. [#] Recommeded in
               :yt-vid:`Carol Willing's Practical Sphinx talk from PyCon 2018
               <0ROZRNZkPS8>`

      #. If the :wiki-pg:`line <Line_(text_file)>` is still too long, then use
         a ``\`` to :wiki-pg:`escape <Delimiter>` a
         :wiki-pg:`new line <Newline>` inside the
         :doc:`target <sphinx:usage/restructuredtext/roles>` and/or
         :doc:`title <sphinx:usage/restructuredtext/roles>`:

         .. code-block:: rest

            :stack-q:`https://stackoverflow.com/questions/1441010/the-shortest-possible\
            -output-from-git-log-containing-author-and-date
            <1441010/the-shortest-possible-output-from-git-log-containing-author-and-\
            date>`:

         * Note that this works, but there may not be
           :wiki-pg:`syntax highlighting <Syntax_highlighting>` in the
           above :rst:dir:`code-block` because of the
           ``\``-:wiki-pg:`escapes <Delimiter>` for
           :wiki-pg:`new lines <Newline>`

#. Use a :wiki-pg:`blank line <Line_(text_file)>` before
   :doc:`directive content <sphinx:usage/restructuredtext/directives>`, but
   not before
   :doc:`directive options <sphinx:usage/restructuredtext/basics>`:

   .. code-block:: rest

      .. csv-table:: Select references
         :align: center
         :header: Reference, Topic

         :xref:`Python.org <Python>`, Official information
         :doc:`python:tutorial/index`, Official tutorial

#. If a :doc:`directive option <sphinx:usage/restructuredtext/basics>`
   requires a :wiki-pg:`line break <Newline>`, make sure to
   :wiki-pg:`indent <Indentation_(typesetting)>` the following
   :wiki-pg:`line <Source_lines_of_code>` if it starts with a
   :doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest

      .. literalinclude:: sample-doc.rst
         :language: rest
         :caption: What the :ref:`reST <tools-restructured-text>` for
            :ref:`sample-doc.rst <sample-doc>` looks like:

   * Otherwise, simply :wiki-pg:`line break <Newline>` without
     :wiki-pg:`indenting <Indentation_(typesetting)>`
   * Note that this does not apply to
     :doc:`directive arguments <sphinx:usage/restructuredtext/basics>`:

     .. code-block:: rest

        .. csv-table:: :ref:`conda:concept-conda-package` required for
           :term:`AAAAAA`
           :align: center

#. See the :ref:`a6 packages table <concepts-packages-table>` for some sample
   :ref:`csv-table syntax<sphinx:table-directives>` with appropriate
   :wiki-pg:`line breaks <Newline>`

   * You should only need ``"`` in :ref:`csv-tables <sphinx:table-directives>`
     for :wiki-pg:`line breaks <Newline>` that are necessary when ``,`` is also
     needed
   * For consistency, ``:align:`` should come before ``:header:``

     .. code-block:: rest

        .. csv-table:: :ref:`conda:concept-conda-package` required for
           :term:`AAAAAA`
           :align: center
           :header: :ref:`Package <conda:concept-conda-package>`, Function, "
              :ref:`Setup Phase <dev-env-intro>`", "
              :ref:`Channel <conda:channels-glossary>`"

#. Use a single :wiki-pg:`space <Whitespace_character>` before
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`

.. _concepts-doc-example:

Simple example
==============

Though it is an :ref:`orphan page <sphinx:metadata>`, check
out the :wiki-pg:`HTML` form of :ref:`sample-doc.rst <sample-doc>`!

.. literalinclude:: sample-doc.rst
   :caption: What the :ref:`reST <tools-restructured-text>` for
      :ref:`sample-doc.rst <sample-doc>` looks like
   :language: rest


*****************
Jupyter Notebooks
*****************

.. note::

   The :ref:`Tools: Jupyter <tools-jupyter>` section explains how
   :ref:`Jupyter <tools-Jupyter>` works, but this is an elaboration of
   specific components in :term:`AAAAAA`

.. _concepts-nbs-tree:

.. code-block:: none

   AAAAAA/
       nbs/
           dev/
               ledger.ipynb
           src/
               ledger.ipynb
               utilities.ipynb
           doc/
               version-stats.ipynb
               version-stats.csv


.. csv-table::
   :align: center
   :header: Name, Function

   ``dev/``, Created during :wiki-pg:`development <Software_development>`
   ``src/``, Complements :ref:`source code <user-intro>`
   ``doc/``, For measuring :ref:`version statistics <dist-doc-versions>`
   "``ledger.ipynb``, ``version-stats.ipynb``, etc.", "
   :ref:`Jupyter Notebooks <tools-jupyter>`"
   ``version-stats.csv``, ":ref:`csv-table <sphinx:table-directives>`
   integration for :ref:`version statistics <versions-stats>`"

.. tip::

   The :xref:`AAAAAA-nbs` opens at the ``nbs/`` :xref:`directory <directory>`
   and can :wiki-pg:`render <Rendering_(computer_graphics)>` any
   :ref:`Jupyter Notebook <tools-jupyter>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>` inside of a
   :xref:`web browser <web-browser>`, even if you don't have
   :ref:`Jupyter <tools-jupyter>`
