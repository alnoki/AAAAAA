.. _concepts-documentation:


#############
Documentation
#############


******
Sphinx
******

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide to Documenting Python <py-dev-guide:documenting>`, "
   Official :xref:`Python` guide to documenting"
   :xref:`documenting-python`, General :xref:`Python` documentation practices
   :xref:`Practical Sphinx seminar <Willing-Sphinx>`, "Practical commands and
   functions for :std:doc:`Sphinx <sphinx:intro>`"


:std:doc:`Sphinx <sphinx:intro>` is a documentation engine that uses a markup
language called
:std:doc:`reStructuredText <sphinx:usage/restructuredtext/basics>` (``reST``).
Documentation files have a ``.rst`` extension and are parsed out by
:std:doc:`Sphinx <sphinx:intro>` whenever :ref:`building-documentation`

:term:`AAAAAA` are documented using the
:std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which provides
a mobile-friendly viewing experience. Many documentation websites made with
this theme have an :guilabel:`Edit on GitHub` (or similar) feature at
the top of the page which will display the
:std:doc:`reST <sphinx:usage/restructuredtext/basics>` file that created the
page

:ref:`Sphinx procedures <sphinx-procedures>` contain :term:`AAAAAA` usage
examples for :ref:`building-documentation`, :ref:`managing-references`, etc.

reST
====

:std:doc:`reStructuredText <sphinx:usage/restructuredtext/basics>` (``reST``)
is a markup language that has special syntax for making fancy
components like ``this``, :guilabel:`this`, etc.

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`reST-cheatsheet`, Quick syntax reference
   :std:doc:`sphinx:usage/restructuredtext/basics`, "Official
   :std:doc:`Sphinx <sphinx:intro>` tutorial for ``reST``"
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   syntax"


.. tip::

   You can harvest the syntax for nearly any kind of
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` component from the
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, via the
   :guilabel:`Edit on GitHub` feature

Style
=====

For consistency, :term:`AAAAAA` adopts stylistic recommendations from common
sources

.. csv-table:: Style references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   General :std:doc:`reST <sphinx:usage/restructuredtext/basics>` style guide"
   :xref:`Doc8`, ":std:doc:`conda:index` package to check
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` style [#]_"

.. rubric:: Footnotes

.. [#] Automatically runs through the :xref:`RST-preview-ext` for
   :xref:`VS-Code`


Select stylistic components worth mentioning:

   * Indent 3 spaces (especially for
     :xref:`nested lists <reST-list-indentation>`)
   * Lines should be a maximum length of 79 characters, unless a
     :ref:`link <links>` title can't be broken up (this is okay)
   * 2-lines of whitespace above anything that is overlined
   * Use a single, unescaped space before
     :std:doc:`footnotes <sphinx:usage/restructuredtext/basics>`
   * Lowercase hyphenated names when possible: ``the-fantastic-reference``

      .. code-block:: rest

          .. _reference-handle:


          ##############
          Document title
          ##############

          Welcome to this document!


          *******
          Section
          *******

          Welcome to this section! [#]_

          Subsection
          ==========

          .. rubric:: Footnotes

          .. [#] Footnote from the above section

The ``.rst`` files in :term:`AAAAAA` should clearly portray other relevant
stylistic components, simply look around in them for more examples


*****************
Jupyter Notebooks
*****************

:xref:`Jupyter Notebooks <Jupyter>` are used for an interactive style of
development and may be referenced throughout the documentation via direct links

This :xref:`AAAAAA-nbs` can render any :xref:`Jupyter Notebook<Jupyter>` from
:xref:`alnoki's AAAAAA repository <AAAAAA-repo>` in a web browser, and contains
a directory of all notebook in the project
