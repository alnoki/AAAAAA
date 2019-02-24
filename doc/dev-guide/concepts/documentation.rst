.. 0.3.0

.. _concepts-doc:


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

.. _concepts-doc-tree:

Structure
=========

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
   "``Makefile`` , ``make.bat``", :ref:`sphinx-building-doc`
   ``index.rst`` (top-level) , ":xref:`homepage <webpage>` of
   :wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA`"
   "``getting-started/`` , ``user-guide/``, etc.", "
   :xref:`Directories <directory>` for
   :wiki-pg:`documentation <Software_documentation>`"
   "``quickstart.rst`` , ``what-next.rst`` , etc. ", "
   :wiki-pg:`Files <Computer_file>` with :ref:`tools-restructured-text`"
   ``refs.bib``, ":xref:`Citations <citation>` for
   :ref:`books <references-books>` (in :ref:`tools-bibtex` format)"

.. _concepts-doc-style:

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

.. _concepts-doc-whitespace:

Whitespace and line breaking
----------------------------

#. Use a :wiki-pg:`blank line <Newline>` at the end of
   :ref:`.rst files <tools-restructured-text>`
#. :wiki-pg:`Indent <Indentation_(typesetting)>` 3
   :wiki-pg:`spaces <Whitespace_character>` (especially for
   :xref:`nested lists <reST-list-indentation>`)
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

         * Note that this works, it just doesn't
           :wiki-pg:`render <Rendering_(computer_graphics)>` with
           :wiki-pg:`colors <Web_colors>` in the above :rst:dir:`code-block`
           because of the ``\``-:wiki-pg:`escapes <Delimiter>` for
           :wiki-pg:`new lines <Newline>`

#. Use a :wiki-pg:`blank line <Line_(text_file)>` before
   :doc:`directive content <sphinx:usage/restructuredtext/directives>`, but
   not before
   :doc:`directive options <sphinx:usage/restructuredtext/directives>`:

   .. code-block:: rest

      .. csv-table:: Select references
         :header: Reference, Topic
         :align: center

         :xref:`Python.org <Python>`, Official information
         :doc:`python:tutorial/index`, Official tutorial

#. If a :doc:`directive option <sphinx:usage/restructuredtext/directives>`
   requires a :wiki-pg:`line break <Newline>`, make sure to
   :wiki-pg:`indent <Indentation_(typesetting)>` the following
   :wiki-pg:`line <Source_lines_of_code>` if it starts with a
   :doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest

      .. literalinclude:: sample-doc.rst
         :caption: What the :ref:`reST <tools-restructured-text>` for
            :ref:`sample-doc.rst <sample-doc>` looks like:

   * Otherwise, simply :wiki-pg:`line break <Newline>` without
     :wiki-pg:`indenting <Indentation_(typesetting)>`

#. See the :ref:`a6 packages table <concepts-packages-table>` for some sample
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate
   :wiki-pg:`line breaks <Newline>`

   * You should only need ``"`` in :ref:`csv-tables <sphinx:table-directives>`
     for :wiki-pg:`line breaks <Newline>` in row data, so don't use them
     for the
     :doc:`directive options <sphinx:usage/restructuredtext/directives>`
     listed after ``:header:`` (even if the ``:header:``
     :doc:`directive options <sphinx:usage/restructuredtext/directives>` have
     a line break)

#. Use a single :wiki-pg:`space <Whitespace_character>` before
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`

.. _concepts-doc-example:

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

.. _concepts-jupyter-nbs-tree:

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
   and can :wiki-pg:`render <Rendering_(computer_graphics)>` any
   :xref:`Jupyter Notebook<Jupyter>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>` inside of a
   :xref:`web browser <web-browser>`, even if you don't have
   :xref:`Jupyter <Jupyter>`
