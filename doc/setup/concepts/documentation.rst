.. _concepts-documentation:


#############
Documentation
#############

.. contents:: Contents
   :local:


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
components like ``this``, :guilabel:`this`, etc. The two most fundamental
components are the :std:doc:`role <sphinx:usage/restructuredtext/roles>`, which
marks a piece of text (usually in-line), and the
:std:doc:`directive <sphinx:usage/restructuredtext/directives>`, which marks a
block of text

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

.. _documentation-style:

Style
=====

:term:`AAAAAA` adopts stylistic recommendations from common sources, with some
particular emphases

.. csv-table:: Style references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   General :std:doc:`reST <sphinx:usage/restructuredtext/basics>` style guide"
   :xref:`Doc8`, ":std:doc:`conda:index` package to check
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` style [#]_"

.. rubric:: Footnotes

.. [#] Automatically runs via the :xref:`RST-preview-ext` for :xref:`VS-Code`

Whitespace
----------

#. Indent 3 spaces (especially for
   :xref:`nested lists <reST-list-indentation>`)
#. Lines should be a maximum length of 79 characters, unless
   :std:doc:`role content <sphinx:usage/restructuredtext/roles>` can't be
   broken up (this is okay)
#. Use 2 lines of whitespace above anything that is overlined
#. Use a single, unescaped space before
   :std:doc:`footnotes <sphinx:usage/restructuredtext/basics>`

General syntax
--------------

#. :ref:`Labels <ref-role>` should be lowercase hyphenated, and should use
   similar categorical naming when possible:

   * ``tools-anaconda``
   * ``git-view-project-log``

#. See :ref:`the packages table <anaconda-packages-table>` for some sample
   :ref:`csv-table <sphinx:table-directives>` syntax with appropriate line
   breaks
#. :ref:`Link <Links>` capitalization should be natural with regard to the
   rest of the sentence

   * :ref:`Links` are here
   * Here are some :ref:`links <Links>`


Simple example
--------------

.. code-block:: rest

   .. _my-label:


   ##########
   Part title
   ##########

   Welcome to this document! Don't forget the double overline!


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

The ``.rst`` files in :term:`AAAAAA` should clearly portray other relevant
stylistic components, simply look around in them for more examples


*****************
Jupyter Notebooks
*****************

:xref:`Jupyter Notebooks <Jupyter>` are used for an interactive style of
development and may be referenced throughout the documentation via direct links

This :xref:`AAAAAA-nbs` can render any :xref:`Jupyter Notebook<Jupyter>` from
:xref:`alnoki's AAAAAA repository <AAAAAA-repo>` in a web browser, and contains
a directory of all :xref:`Jupyter Notebooks <Jupyter>` created for
:term:`AAAAAA`
