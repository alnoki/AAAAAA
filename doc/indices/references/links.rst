.. _references-links:


#####
Links
#####

This is a centralized and comprehensive list of :xref:`online <internet>`
information :xref:`cited <citation>` throughout
:wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA`,
in :xref:`URL` format

:xref:`Links <URL>` are not necessarily in order, but :xref:`links <URL>` with
high priority are usually placed at the top of a section

.. tip::

   If you manage a :xref:`website <website>` using :ref:`Sphinx <tools-sphinx>`
   and you want to create a list like this, see the
   :ref:`references procedures <sphinx-managing-references>`

.. contents:: Contents
   :local:


******
Python
******

General
=======

#. :yt-pl:`Corey Schafer YouTube playlist: Python Tutorials
   <-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU>`

   * Recommended starting point for learning :xref:`Python`

#. :xref:`Python.org <Python>`

   * Definitive reference for the :xref:`Python`

#. :doc:`python:tutorial/index`

   * Official :xref:`Python` tutorial

#. :pep:`8`

   * Official :xref:`Python` style guide for :xref:`source code <source-code>`

#. :doc:`python:howto/functional`

   * Official tutorial on :xref:`Python` techniques

#. :doc:`python:howto/index`

   * Official in-depth :xref:`Python` tutorials for various advanced topics

#. :doc:`python:faq/index`

   * In-depth answers to specific questions about core functionality

#. :doc:`python:faq/programming`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>`, methods,
     recommended practices

#. :real-py:`RealPython <>`

   * Comprehensive :xref:`website <website>` with examples, guides, tips, etc.

#. :doc:`tutorial/interpreter`

   * Instructions for the mechanism that runs :xref:`Python` code

Project structure
=================

#. :ref:`python:tut-packages`

   * Structuring of :xref:`source code <source-code>` and
     :xref:`directories <directory>` in a project

#. :xref:`print-dir-tree`

   * Sample :xref:`code <source-code>` to make a :xref:`directory <directory>`
     tree
   * Adapted for the :ref:`directory tree procedure <writing-make-dir-tree>`

#. :doc:`pip <python:installing/index>`

   * General installer for :ref:`packages <python:tut-packages>`
   * Used to :ref:`configure a6 <conda-pip-AAAAAA>` for use with
     :doc:`pytest <pytest:index>`

#. :ref:`Module <python:tut-modules>`

   * A :wiki-pg:`file <Computer_file>` that ends with a ``.py``
     :wiki-pg:`extension <Filename_extension>`

Text
====

#. :stack-q:`Python quote convention
   <56011/single-quotes-vs-double-quotes-in-python>`

   * Recommendation for using ``'`` vs ``"`` in :xref:`strings <string>`

#. :ref:`python:comments`

   * :wiki-pg:`Documentation <Software_documentation>` inside
     :xref:`source code <source-code>`

#. :ref:`python:tut-docstrings`

   * :ref:`python:comments` for specific :xref:`Python` components

#. :py:func:`python:print`

   * Display a :wiki-pg:`string <String_(computer_science)>`

Types
=====

#. :doc:`python:library/stdtypes`

   * Standard :xref:`Python` data structures

#. :term:`Object <python:object>`

   * The most basic :doc:`type <python:library/stdtypes>`, from which others
     are derived

#. :ref:`python:tut-dictionaries`

   * A :doc:`type <python:library/stdtypes>` containing *key: value* pairs

#. :xref:`realpython-type-checking`

   * How to verify correct :doc:`types <python:library/stdtypes>` in
     :xref:`source code <source-code>`

#. :ref:`python:tut-numbers`

   * Simple introduction to :py:obj:`python:int` and :py:obj:`python:float`

#. :py:obj:`python:int`

   * A :ref:`number <python:tut-numbers>` like ``2`` or ``128`` but not ``2.3``

#. :py:obj:`python:float`

   * A :ref:`number <python:tut-numbers>` like ``1.5`` or ``3.0`` but not ``3``

#. :doc:`Decimals <python:library/decimal>`

   * A precise way to represent things like :xref:`money <money>`

#. :doc:`python:tutorial/floatingpoint`

   * When to use :doc:`decimals <python:library/decimal>` instead of
     :py:obj:`floats <python:float>`

Control flow
============

#. :ref:`Functions <python:tut-functions>`

   * Processes that can act on :term:`arguments <python:argument>`

#. :ref:`python:tut-defaultargs`

   * Values that must be passed to a :ref:`function <python:tut-functions>`

#. :ref:`python:tut-keywordargs`

   * Values that may be (but do not need to be) passed to a
     :ref:`function <python:tut-functions>`

#. :term:`Argument <python:argument>`

   * Concise definition for both :ref:`positional <python:tut-defaultargs>` and
     :ref:`keyword <python:tut-keywordargs>` styles

Classes
=======

#. :ref:`python:tut-classes`

   * A way to bundle data and functionality together

#. :ref:`python:tut-classobjects`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>` and
     :ref:`instance <python:tut-classes>` concepts, like ``__init__()``

#. :term:`Attributes <python:attribute>`

   * Accessed via dotted notation: ``big_thing.small_attribute``

#. :ref:`python:tut-scopes`

   * Domains of association

#. :ref:`python:tut-class-and-instance-variables`

   * :ref:`Attributes <python:tut-scopes>` of a
     :ref:`class <python:tut-classes>` that have
     different :ref:`scopes <python:tut-scopes>`

#. :py:class:`python:property`

   * A special :term:`python:attribute` of a :ref:`class <python:tut-classes>`
     which can be a :ref:`function <python:tut-functions>`
     :ref:`instance variables <python:tut-class-and-instance-variables>`
   * :py:attr:`AAAAAA.ledger.Transaction.per_share_amount` is a
     :py:class:`python:property`

Environments
============

Anaconda
--------

#. :xref:`Anaconda`

   * A manager for :ref:`Python packages <python:tut-packages>`

#. :doc:`anaconda:anaconda/index`

   * Official :wiki-pg:`documentation <Software_documentation>`

#. :doc:`Miniconda<conda:user-guide/install/index>`

   * Small manageable version of :xref:`Anaconda`

#. :doc:`conda:index`

   * :xref:`command-line` configurator for :xref:`Anaconda`

#. :ref:`conda:starting-conda`

   * Invocation methods for :doc:`conda <conda:index>`

#. :ref:`Conda package <conda:concept-conda-package>`

   * :ref:`Python package <python:tut-packages>` managed by :xref:`Anaconda`

#. :ref:`Conda environment <conda:concept-conda-env>`

   * A collection of :ref:`conda packages <conda:concept-conda-package>`

#. :ref:`Conda channel <conda:channels-glossary>`

   * A :wiki-pg:`host <Host_(network)>` for
     :ref:`conda packages <conda:concept-conda-package>`

#. :xref:`conda-forge`

   * A community-driven :ref:`conda channel <conda:channels-glossary>`

Conda syntax
------------

#. :doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`

   * Common :wiki-pg:`commands <Command_line>` for :doc:`conda <conda:index>`

#. :doc:`conda:commands/create`

   * Make a new :ref:`conda environment <conda:concept-conda-env>`

#. :doc:`conda:commands/install`

   * Add a :ref:`package <conda:concept-conda-package>` to a
     :ref:`conda environment <conda:concept-conda-env>`

#. :ref:`conda:activate-env`

   * Enable use of a :ref:`conda environment <conda:concept-conda-env>`

#. :doc:`conda:user-guide/tasks/manage-environments`

   * Using :ref:`environment files <conda:concept-conda-env>`

#. :doc:`conda:commands/clean`

   * Removing unnecessary :ref:`conda packages <conda:concept-conda-package>`

#. :doc:`conda:commands/update`

   * Get the most recent version of
     :ref:`conda packages <conda:concept-conda-package>`

#. :doc:`conda:commands/list`

   * List the :ref:`conda packages <conda:concept-conda-package>` in a
     :ref:`conda environment <conda:concept-conda-env>`


********
Packages
********

Numerical Analysis
==================

NumPy
-----

#. :doc:`NumPy <numpy:about>`

   * Fundamental :ref:`package <conda:concept-conda-package>` for advanced
     numerical :xref:`Python`

#. :doc:`numpy:user/quickstart`

   * Official :doc:`NumPy <numpy:about>` tutorial

#. :xref:`codebasics-numpy`

   * Recommended :doc:`NumPy <numpy:about>` tutorial on :xref:`YouTube`

Matplotlib
----------

#. :doc:`Matplotlib <matplotlib:index>`

   * Plotting tool for numerical data

#. :doc:`matplotlib:tutorials/index`

   * Instructions to use :doc:`Matplotlib <matplotlib:index>`

#. :xref:`codebasics-matplotlib`

   * Recommended :doc:`Matplotlib <matplotlib:index>` tutorial on
     :xref:`YouTube`

pandas
------

#. :doc:`pandas <pandas:index>`

   * For handling datasets

#. :doc:`pandas:getting_started/10min`

   * Official :doc:`pandas <pandas:index>` tutorial

#. :xref:`codebasics-pandas`

   * Recommended :doc:`pandas <pandas:index>` tutorial on :xref:`YouTube`

pytest
======

#. :doc:`pytest <pytest:index>`

   * Framework for writing test code

#. :xref:`codebasics-pytest`

   * Recommended :doc:`pytest <pytest:index>` tutorial on :xref:`YouTube`

#. :doc:`pytest tutorials <pytest:contents>`

   * Official comprehensive :doc:`pytest <pytest:index>` walkthroughs

#. :doc:`pytest:goodpractices`

   * Configuring :doc:`pytest <pytest:index>` to run with :term:`a6`

#. :xref:`pytest-discovery-issue`

   * A potential problem (and solution) when using :xref:`VS-Code` with
     :doc:`pytest <pytest:index>`


******************
Project management
******************

AAAAAA codebase
===============

#. :github:`AAAAAA repository <alnoki/AAAAAA>`

   * :github:`GitHub <>` repository for :term:`AAAAAA`

#. :github:`alnoki's GitHub repositories <alnoki>`

   * Assorted :xref:`Jupyter Notebooks <Jupyter>` and
     :xref:`code <source-code>` from other tutorials

#. :github:`GitHub <>`

   * :xref:`Online <internet>` repository for
     :xref:`software <software>` projects

#. :xref:`AAAAAA-zip-archive`

   * Quickly :wiki-pg:`download <Download>` the
     :github:`AAAAAA repository <alnoki/AAAAAA>`

Versioning
==========

#. :xref:`semver`

   * :ref:`Version number <indices-versions>` guidelines: ``MAJOR.MINOR.PATCH``

#. :xref:`git-commit-guidelines`

   * General guidelines for describing contributions to a project

#. :xref:`commit-conventions`

   * Specific language style for contributing to a project

#. :xref:`mvp-development`

   * An incremental way to create or add features

Distribution
============

#. :ref:`pypa:requirements files`

   * Help :ref:`tools-read-the-docs` identify :ref:`tools-sphinx-extensions`

#. :doc:`pypa-guide:tutorials/packaging-projects`

   * Create a :ref:`Python package <python:tut-packages>`


*******************
Git version control
*******************

General
=======

#. :wiki-pg:`Version control <Version_control>`

   * A way to track changes to :wiki-pg:`files <Computer_file>`

#. :git-doc:`Git manual <user-manual>`

   * Quick practical reference

#. :git-scm:`Git book <book/en/v2>`

   * In-depth conceptual explanations

#. :git-scm:`downloads`

   * Get :git-doc:`Git <user-manual>`

#. :xref:`git-setup`

   * Getting started

#. :xref:`sha1`

   * Unique identifier attached to each :xref:`commit <git-commit>`

#. :git-doc:`.gitignore <user-manual.html#ignoring-files>`

   * Ignore certain :wiki-pg:`files <Computer_file>`

#. :xref:`less-pager`

   * For viewing :xref:`git-log`

Core commands
=============

#. :git-doc:`git-clone`

   * :wiki-pg:`Download` a :wiki-pg:`software <Software>` project

#. :xref:`git-config`

   * Setup :wiki-pg:`user credentials <User_(computing)>`

#. :xref:`git-log`

   * See project history

#. :xref:`git-commit`

   * Create saved changes to a project

#. :git-doc:`git-add`

   * Prepare changes for :ref:`committing <git-committing>`

#. :xref:`git-push`

   * :wiki-pg:`Upload` a :xref:`commit <git-commit>`

#. :xref:`git-tag`

   * Assign a special identifier to a :xref:`commit <git-commit>`

#. :xref:`git-branch`

   * Work with independent sequences of :xref:`commits <git-commit>`

#. :xref:`git-checkout`

   * Switch between :xref:`branches <git-branch>`

#. :xref:`git-merge`

   * Combine :xref:`branches <git-branch>`

Auxiliary commands
==================

#. :git-doc:`git-reset`

   * Fix mistakes

#. :git-doc:`git-show`

   * Inspect :git-doc:`tags <git-tag>` and :git-doc:`commits <git-commit>`

#. :git-doc:`git-rev-list`

   * Get number of :git-doc:`commits <git-commit>`

Special features
================

#. :xref:`git-log-formatting`

   * Special options for inspecting :xref:`git-log`

#. :xref:`list-git-developers`

   * Identifying unique :xref:`committers <git-commit>`

#. :xref:`github-change-authors`

   * :github:`GitHub <>` instructions to re-write :xref:`git-commit` history

#. :xref:`git-branch-filtering`

   * Extra options for
     :xref:`re-writing commit history <github-change-authors>`


*************
Documentation
*************

General
=======

#. :doc:`Python Developer's Guide to Documenting Python
   <py-dev-guide:documenting>`

   * Guide to general :doc:`Sphinx <sphinx:intro>` use
   * :doc:`reStructuredTest <sphinx:usage/restructuredtext/basics>` style guide

#. :real-py:`RealPython guide to documenting Python <documenting-python-code>`

   * Recommended :wiki-pg:`documentation <Software_documentation>` practices
     for :xref:`Python`

#. :wiki-pg:`Acronym`

   * A short way to say something, like :term:`AAAAAA`

#. :xref:`citation`

   * A way to create a :ref:`reference <references>` to a source of information

#. :xref:`book`

   * Information source

#. :xref:`ISBN`

   * Unique identifier for :xref:`books <book>`

#. :xref:`cite-multiple-authors`

   * Use of ``et. al``

#. :wiki-pg:`Copyright`

   * Defines rules for using content

Sphinx
======

Practical use
-------------

#. :doc:`Sphinx <sphinx:intro>`

   * Official :wiki-pg:`documentation <Software_documentation>` for the
     :doc:`Sphinx <sphinx:intro>` engine, which creates
     :wiki-pg:`documentation <Software_documentation>`

#. :doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`

   * How to start a new :wiki-pg:`documentation <Software_documentation>`
     project

#. :doc:`Matplotlib sampledoc tutorial <matplotlib-sampledoc:index>`

   * Quick walkthrough with practical
     :wiki-pg:`syntax <Syntax_(programming_languages)>` examples
   * Interactive :xref:`Python` examples, using plots

#. :yt-vid:`Carol Willing's Practical Sphinx talk from PyCon 2018
   <0ROZRNZkPS8>`

   * Common :wiki-pg:`development <Software_development>` tasks [#]_, like
     :ref:`checking links <sphinx-checking-links>`
   * Team :wiki-pg:`development <Software_development>` strategies

#. :doc:`Sphinx builders <sphinx:usage/builders/index>`

   * Create different styles of
     :wiki-pg:`documentation <Software_documentation>`

#. :xref:`sphinx-autobuild`

   * Automatically update :ref:`documentation builds <sphinx-building-doc>`

#. :xref:`Writer-intro-to-Sphinx`

   * General explanation of using
     :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   * From Eric Holscher, co-founder of
     :doc:`Read the Docs<rtfd:index>`

#. :doc:`HTTP server <python:library/http.server>`

   * :ref:`Python package <python:tut-packages>` that can
     :wiki-pg:`host <Host_(network)>` a
     :xref:`website <website>` for viewing
     :wiki-pg:`documentation <Software_documentation>`

.. rubric:: Footnotes

.. [#]
   .. csv-table::
      :align: center
      :header: :wiki-pg:`Time` in video, Topic

      10:15, Incorporating :ref:`Jupyter Notebooks <tools-jupyter>`
      13:00, Checking spelling
      14:00, Incorporating images
      15:15, :ref:`Including code <tools-napoleon>`
      17:00, Continuous integration
      20:00, :doc:`Autodoc <sphinx:usage/extensions/autodoc>`
      24:15, :ref:`Themes <tools-read-the-docs>`

Usage specifics
---------------

#. :doc:`sphinx:usage/extensions/index`

   * Additional :doc:`Sphinx <sphinx:intro>` functionality

#. :doc:`conf.py usage<sphinx:usage/configuration>`

   * How to :ref:`configure <configs-sphinx>` a :ref:`Sphinx <tools-sphinx>`
     project

#. :ref:`sphinx:toctree-directive`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` for
     creating project :wiki-pg:`documentation <Software_documentation>`
     structure

#. :doc:`Autodoc extension <sphinx:usage/extensions/autodoc>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` for generating
     :wiki-pg:`documentation <Software_documentation>` directly from
     :xref:`source code <source-code>`

#. :ref:`sublime-with-sphinx:use the external links extension`

   * Instructions for :wiki-pg:`installing <Installation_(computer_programs)>`
     an example :doc:`Sphinx extension <sphinx:usage/extensions/index>`
   * Similar to :ref:`external link management <sphinx-xref>` in
     :term:`AAAAAA`

#. :rst:role:`sphinx:math`

   * :doc:`Role <sphinx:usage/restructuredtext/roles>` for using
     :wiki-pg:`LaTeX` in-:wiki-pg:`line <Source_lines_of_code>`

#. :rst:dir:`sphinx:math`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` for using
     :wiki-pg:`LaTeX` on its own :wiki-pg:`line <Source_lines_of_code>`

#. :stack-q:`HTTP socket error fix
   <19071512/socket-error-errno-48-address-already-in-use>`

   * Potential problem (and solution) when
     :ref:`building documentation <sphinx-building-doc>`

#. :doc:`sphinx:usage/restructuredtext/domains`

   * Collection of
     :doc:`directives <sphinx:usage/restructuredtext/directives>` and
     :doc:`roles <sphinx:usage/restructuredtext/roles>` for specific topics

#. :ref:`sphinx:metadata`

   * Enable :ref:`orphan pages <sphinx:metadata>`, like
     :ref:`sample-doc.rst <sample-doc>`

With Read the Docs
------------------

#. :yt-vid:`Mahdi Yusuf's Sphinx & Read the Docs screencast <oJsUvBQyHBs>`

   * Setting up a project using :doc:`quickstart <sphinx:usage/quickstart>`
   * :rst:dir:`toctree` and associated
     :wiki-pg:`documentation <Software_documentation>` structure
   * Basic :ref:`reST syntax <tools-restructured-text>`

#. :doc:`Read the Docs<rtfd:index>`

   * :xref:`Online <internet>` repository for
     :wiki-pg:`software documentation <Software_documentation>`

#. :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`

   * Tutorial for starting a :doc:`Sphinx <sphinx:intro>` project
     :wiki-pg:`hosted <Host_(network)>` on
     :doc:`Read the Docs<rtfd:index>`

#. :doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`

   * Contains sample :ref:`reST syntax <tools-restructured-text>`

#. :doc:`Read the Docs Sphinx Theme configuration
   <rtd-sphinx-theme:configuring>`

   * Values to use in :ref:`conf.py <configs-conf-py>`

#. :doc:`rtfd:webhooks`

   * Automatic project modification detection

#. :doc:`rtfd:versions`

   * Automatic support for :ref:`versions <indices-versions>`

#. :doc:`rtfd:builds`

   * How the :wiki-pg:`host computer <Host_(network)>` performs
     :ref:`Sphinx build procedures <sphinx-building-doc>` for
     :ref:`tools-read-the-docs`

#. :xref:`rtfd-account`

   * Interface for :ref:`distributing documentation <dist-doc>`

Reference management
--------------------

#. :doc:`Intersphinx extension <sphinx:usage/extensions/intersphinx>`

   * Official :wiki-pg:`documentation <Software_documentation>`
   * For :ref:`linking <references-links>` to other
     :doc:`Sphinx <sphinx:intro>` projects

#. :github:`Michael Jones' xref extension <michaeljones/sphinx-xref>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to manage
     common :ref:`links <references-links>` in a project

#. :doc:`extlinks <sphinx:usage/extensions/extlinks>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` for
     :wiki-pg:`URLs <URL>` from common sources

#. :stack-q:`Intersphinx objects.inv explanation
   <45699577/how-to-link-to-root-page-in-intersphinx>`

   * Interpretation of :doc:`objects.inv <sphinx:usage/extensions/intersphinx>`
     when using :doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`

#. :stack-q:`Intersphinx inventory parser
   <30939867/how-to-properly-write-cross-references-to-external-documentation-\
   with-intersphin>`

   * Sample :wiki-pg:`code <Source_code>` for analyzing
     :doc:`objects.inv <sphinx:usage/extensions/intersphinx>` maps

#. :stack-q:`Intersphinx with NumPy/Matplotlib
   <21538983/specifying-targets-for-intersphinx-links-to-numpy-scipy-and-\
   matplotlib>`

   * Instructions for using
     :doc:`Intersphinx <usage/extensions/intersphinx>` with specific
     :ref:`packages <python:tut-packages>`

#. :xref:`bibtex`

   * :xref:`citation` management format

#. :doc:`BibTeX extension <bibtex:index>`

   * :ref:`Sphinx extension <tools-sphinx>` for :xref:`citing <citation>` with
     :xref:`bibtex`

#. :xref:`ottobib`

   * Provides :xref:`bibtex` data for a :xref:`book <book>` with a given
     :xref:`ISBN`

#. :xref:`bibtex-syntax`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>` for identifying
     specific :xref:`citation <citation>` components

Showing code
------------

#. :rst:dir:`code-block`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` to show
     sections of :wiki-pg:`code <Source_code>`

#. :rst:dir:`literalinclude`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` to show
     sections of :wiki-pg:`code <Source_code>`, directly from a
     :wiki-pg:`file <Computer_file>`

#. :pep:`Type annotations <484>`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>` to indicate
     :doc:`types <python:library/stdtypes>` in :xref:`code <source-code>`

#. :ref:`Python roles <sphinx:python-roles>`

   * :doc:`Sphinx Domain <sphinx:usage/restructuredtext/domains>` for
     :xref:`Python` component :wiki-pg:`documentation <Software_documentation>`

#. :doc:`Read the Docs sample Python module <demo/api>`

   * Sample :wiki-pg:`syntax <Syntax_(programming_languages)>` for
     :doc:`autodoc <sphinx:usage/extensions/autodoc>`

#. :ref:`sphinx:info-field-lists`

   * :ref:`reST syntax <tools-restructured-text>` shown at
     :ref:`concepts-code-e4`

Napoleon
--------

#. :doc:`Napoleon <sphinx:usage/extensions/napoleon>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
     content from :ref:`NumPy docstrings <numpy:format>`

#. :doc:`Autodoc <sphinx:usage/extensions/autodoc>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to include content
     from :ref:`docstrings <python:tut-docstrings>`

#. :pep:`257`

   * Official conventions for :ref:`docstrings <python:tut-docstrings>`

#. :ref:`NumPy docstrings <numpy:format>`

   * :ref:`Docstring <python:tut-docstrings>` format provided by
     :doc:`NumPy <numpy:about>`

#. :doc:`napoleon:example_numpy`

   * Sample :ref:`NumPy docstring syntax <numpy:format>` for
     :doc:`napoleon <sphinx:usage/extensions/napoleon>`

#. :rst:dir:`automodule`

   * Show :ref:`modules <python:tut-modules>`

#. :rst:dir:`autodata`

   * Show :ref:`attributes <python:tut-scopes>`

#. :rst:dir:`autofunction`

   * Show :ref:`functions <python:tut-functions>`

reStructuredText
================

General
-------

#. :doc:`sphinx:usage/restructuredtext/basics`

   * :doc:`Sphinx <sphinx:intro>` explanation of
     :doc:`reST <sphinx:usage/restructuredtext/basics>`, a particular
     :wiki-pg:`markup language <Markup_language>`

#. :docutils:`reStructuredText <rst.html>`

   * Official :wiki-pg:`documentation <Software_documentation>`

#. :docutils:`Quick reST <docs/user/rst/quickref.html>`

   * Official reference with :ref:`reST <tools-restructured-text>` examples

#. :conda-forge:`Doc8 reST linter <doc8>`

   * :wiki-pg:`Linter <Lint_(software)>` for
     :doc:`reST <sphinx:usage/restructuredtext/basics>`

Syntax
------

#. :github:`reST cheatsheet
   <ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`

   * Quick reference for :doc:`reST <sphinx:usage/restructuredtext/basics>`
     usage

#. :stack-q:`reST list indentation
   <5550089/how-to-create-a-nested-list-in-restructuredtext>`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>` tip

#. :ref:`Tables <sphinx:table-directives>`

   * :wiki-pg:`Syntax <Syntax_(programming_languages)>` options

#. :doc:`Role <sphinx:usage/restructuredtext/roles>`

   * Element that marks a piece of text, usually
     in-:wiki-pg:`line <Source_lines_of_code>`

#. :doc:`Directive <sphinx:usage/restructuredtext/directives>`

   * Element that marks a block of text

#. :rst:role:`guilabel`

   * :guilabel:`Fancy buttons`

#. :ref:`Label role <sphinx:ref-role>`

   * :doc:`Role syntax <sphinx:usage/restructuredtext/roles>` to
     :wiki-pg:`link <URL>` to arbritrary
     :wiki-pg:`documentation <Software_documentation>` locations

#. :xref:`admonition`

   * A special badge of text [#]_

.. rubric:: Footnotes

.. [#]
      .. danger::

         This is an :xref:`admonotion <admonition>`

Engine-agnostic formatting
==========================

#. :xref:`tables-generator`

   * :xref:`Online <internet>` tool to format tables in :wiki-pg:`LaTeX`,
     :github-help:`Markdown <basic-writing-and-formatting-syntax>`,
     :ref:`tools-restructured-text`, and plain text

#. :wiki-pg:`LaTeX`

   * System for :wiki-pg:`documentating <Software_documentation>` equations in
     :xref:`Jupyter Notebooks <Jupyter>` and in
     :doc:`Sphinx <sphinx:intro>`

#. :wiki-pg:`Markup language <Markup_language>`

   * A way to create :wiki-pg:`documentation <Software_documentation>` in
     a :wiki-pg:`computer <Computer>`

#. :github-help:`Markdown <basic-writing-and-formatting-syntax>`

   * :wiki-pg:`Markup language <Markup_language>` used to generate
     tables, lists, and other components
   * Used for :github:`GitHub <>`, :xref:`Jupyter Notebooks <Jupyter>`, and
     :ref:`AAAAAA task management <versioning-td3>`

#. :wiki-pg:`NATO phonetic alphabet <NATO_phonetic_alphabet>`

   * A: ``Alfa``, B: ``Bravo``, and so on


*****
Tools
*****

Jupyter
=======

General
-------

#. :xref:`Jupyter Notebooks <Jupyter>`

   * Interactive :xref:`Python` environment
   * :xref:`Code <source-code>`, :wiki-pg:`LaTeX`,
     :github-help:`Markdown <basic-writing-and-formatting-syntax>`, and
     plotting in one :wiki-pg:`file <Computer_file>`

#. :yt-vid:`Corey Schafer tutorial <HW29067qVWk>`

   * Recommended for learning to use :xref:`Jupyter Notebooks <Jupyter>`
   * Tutorial video from
     :yt-pl:`Corey Schafer <-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU>`

#. :xref:`AAAAAA-nbs`

   * :xref:`Online <internet>` viewer for :xref:`Jupyter Notebooks <Jupyter>`
     in :term:`AAAAAA`

Extensions
----------

#. :doc:`nb-extensions:index`

   * Additional functionality for :xref:`Jupyter Notebooks <Jupyter>`

#. :doc:`nb-extensions:nbextensions/collapsible_headings/readme`

   * Section navigation and management

#. :doc:`nb-extensions:nbextensions/toc2/README`

   * Automatic section linking

#. :doc:`nb-extensions:nbextensions/varInspector/README`

   * Inspect data values

#. :xref:`live-md-preview`

   * Preview :github-help:`Markdown <basic-writing-and-formatting-syntax>` and
     :wiki-pg:`LaTeX`

VS Code
=======

General
-------

#. :wiki-pg:`Integrated development environment (IDE)
   <Integrated_development_environment>`

   * :wiki-pg:`Software` that is used to make :wiki-pg:`software <Software>`

#. :xref:`VS-Code`

   * An :wiki-pg:`IDE <Integrated_development_environment>` that is
     :wiki-pg:`open-source <Open-source_software>`
   * Has a collection of :xref:`extensions <VS-Code-extensions>` developed by
     the :wiki-pg:`open-source <Open-source_software>` community

#. :xref:`VS-Code-extensions`

   * Enable additional functionality

#. :vs-code-doc:`VS Code Python tutorial <languages/python>`

   * Setup and basic usage

#. :vs-code-doc:`VS Code unit testing <python/unit-testing>`

   * Use :ref:`tools-pytest`

#. :vs-code-doc:`VS Code settings <getstarted/settings>`

   * :ref:`concepts-configs` in :ref:`configs-settings-json`

#. :vs-code-doc:`User interface <getstarted/userinterface>`

   * Explanation of core components

#. :vs-code-doc:`VS Code integrated terminal <editor/integrated-terminal>`

   * Use a :xref:`command line <command-line>`

#. :vs-code-doc:`VS Code Command Palette
   <getstarted/userinterface#_command-palette>`

   * Direct :wiki-pg:`command <Command_line>` input

#. :xref:`VS-Code-insiders`

   * Has the latest features, may have problems

Colors
------

#. :vs-code-doc:`Themes <getstarted/themes>`

   * General :wiki-pg:`colors <Web_colors>` for the
     :wiki-pg:`IDE <Integrated_development_environment>`

#. :vs-code-api:`Token color customizations <references/theme-color>`

   * Reference for changing specific :wiki-pg:`colors <Web_colors>`

#. :vs-code-api:`Color theme extension guide <extension-guides/color-theme>`

   * Enhanced :wiki-pg:`color <Web_colors>` customization functionality

#. :github:`Token color customizations usage <Microsoft/vscode/pull/29393>`

   * Advanced :wiki-pg:`color <Web_colors>` manipulation

Extensions
----------

#. :vs-code-doc:`Managing extensions <editor/extension-gallery>`

   * Official :wiki-pg:`documentation <Software_documentation>`

#. :vs-code-ext:`GitLens <eamodio.gitlens>`

   * Enhanced :ref:`tools-git` functionality

#. :vs-code-ext:`Python <ms-python.python>`

   * Work with :ref:`tools-python`

#. :vs-code-doc:`Selecting the Python interpreter
   <python/environments#_select-and-activate-an-environment>`

   * Integrate the :doc:`Python interpreter <python:tutorial/interpreter>`

#. :vs-code-ext:`Python Test Explorer Extension
   <LittleFoxTeam.vscode-python-test-adapter>`

   * Use :ref:`tools-pytest`

#. :vs-code-ext:`VS Code Bookmarks extension <alefragnani.Bookmarks>`

   * Mark and navigate :xref:`source code <source-code>`

#. :vs-code-ext:`reStructuredText <lextudio.restructuredtext>`

   * :wiki-pg:`Syntax highlighting <Syntax_highlighting>` for
     :ref:`tools-restructured-text`
   * Limited :wiki-pg:`live rendering <Rendering_(computer_graphics)>`
     functionality

#. :github:`Doc8 newline issue fix
   <vscode-restructuredtext/vscode-restructuredtext/issues/84>`

   * Fix for :wiki-pg:`syntax highlighting <Syntax_highlighting>`
     problem in
     :vs-code-ext:`reStructuredText extension <lextudio.restructuredtext>`

#. :vs-code-ext:`Vim extension for VS code <vscodevim.vim>`

   * Use :ref:`tools-vim` in :ref:`tools-vs-code`

Vim
===

Official information
--------------------

#. :xref:`Vim`

   * For :xref:`git-config`, :xref:`git-commit`, and :ref:`tools-vs-code`

#. :vim-wiki:`Mac OS syntax highlighting <Turn_on_syntax_coloring_in_Mac_OS_X>`

   * Enable :wiki-pg:`syntax highlighting <Syntax_highlighting>`

#. :vim-wiki:`.vimrc file <Open_vimrc_file>`

   * :ref:`Vim configuration file <configs-vim>` for
     :wiki-pg:`syntax highlighting <Syntax_highlighting>`

#. :vim-wiki:`Repeating keystrokes <Recording_keys_for_repeated_jobs>`

   * Do similar :wiki-pg:`commands <Command_line>` repeatedly

#. :vim-wiki:`Official tutorial <Tutorial>`

   * Simple instructions

#. :vim-wiki:`All the right moves <All_the_right_moves>`

   * Intermediate :wiki-pg:`command <Command_line>` reference

Unofficial supplements
----------------------

#. :xref:`Vim-tutorial`

   * Learn :xref:`Vim <Vim>`

#. :xref:`Vim-cheatsheet`

   * Common :wiki-pg:`commands <Command_line>` for :xref:`Vim <Vim>`

#. :yt-vid:`Mastering Vim by Chris Toomey <wlR5gYd6um0>`

   * Demonstrative video with tips and :wiki-pg:`commands <Command_line>`

#. :stack-q:`Vim E325 error <45489008/vim-opening-file-e325-attention-error>`

   * Can happen when :ref:`committing <git-committing>` incorrectly

#. :xref:`vim-learn-plan`

   * Become efficient with :xref:`Vim`


*********
Computers
*********

General
=======

#. :xref:`computer`

   * A system that manipulates information using :wiki-pg:`software <Software>`

#. :wiki-pg:`User <User_(computing)>`

   * Who is using :wiki-pg:`software <Software>`

#. :wiki-pg:`Developer <Programmer>`

   * Who is creating :wiki-pg:`software <Software>`

#. :wiki-pg:`Install <Installation_(computer_programs)>`

   * Provide :wiki-pg:`software <Software>` for a
     :wiki-pg:`computer <Computer>`

Interfaces
==========

#. :xref:`mobile-device`

   * A small, portable :xref:`computer <computer>`

#. :wiki-pg:`Laptop`

   * A portable :xref:`computer <computer>`

#. :wiki-pg:`Copy-paste <Cut,_copy,_and_paste>`

   * One way to share :xref:`source code <source-code>`

#. :wiki-pg:`Typing`

   * How to create :wiki-pg:`strings <String_(computer_science)>`

#. :wiki-pg:`Web colors <Web_colors>`

   * Colors for the :wiki-pg:`Internet`

#. :wiki-pg:`Point and click <Point_and_click>`

   * One way to use a :wiki-pg:`computer <Computer>`

#. :wiki-pg:`Rendering <Rendering_(computer_graphics)>`

   * Creating visualizations on a :wiki-pg:`computer <Computer>`

#. :wiki-pg:`Scrolling`

   * Moving visualizations around

#. :wiki-pg:`Sidebar <Sidebar_(computing)>`

   * Keeps information on the side of a :wiki-pg:`program <Software>`

#. :wiki-pg:`Button <Button_(computing)>`

   * A component that you can :wiki-pg:`click <Point_and_click>`

Software
========

#. :wiki-pg:`Source code <Source_code>`

   * A way to communicate with a :xref:`computer <computer>`

#. :wiki-pg:`Software`

   * A structured collection of :xref:`source code <source-code>`

#. :wiki-pg:`Open-source software <Open-source_software>`

   * Public way to share :xref:`source code <source-code>`

#. :wiki-pg:`Software documentation <Software_documentation>`

   * Describes how :wiki-pg:`software <Software>` works

#. :wiki-pg:`Development <Software_development>`

   * Making :wiki-pg:`software <Software>`

#. :wiki-pg:`Line of code <Source_lines_of_code>`

   * One portion of :wiki-pg:`source code <Source_code>`

#. :wiki-pg:`Algorithm`

   * A :wiki-pg:`software <Software>` process

#. :wiki-pg:`Linter <Lint_(software)>`

   * Check :wiki-pg:`source code <Source_code>` for
     :wiki-pg:`syntax <Syntax_(programming_languages)>` or style errors

#. :wiki-pg:`Execution <Execution_(computing)>`

   * When a :wiki-pg:`computer <Computer>` uses :wiki-pg:`software <Software>`

Syntax
======

#. :wiki-pg:`Syntax <Syntax_(programming_languages)>`

   * :wiki-pg:`String <String_(computer_science)>` composition rules

#. :wiki-pg:`Syntax highlighting <Syntax_highlighting>`

   * :wiki-pg:`Rendering <Rendering_(computer_graphics)>` for special
     components in a :wiki-pg:`file <Computer_file>`

#. :wiki-pg:`Character <Character_(computing)>`

   * Usually, a text symbol

#. :wiki-pg:`String <String_(computer_science)>`

   * How a :wiki-pg:`computer <Computer>` stores
     :wiki-pg:`characters <Character_(computing)>`

#. :wiki-pg:`Line <Line_(text_file)>`

   * A sequence of :wiki-pg:`characters <Character_(computing)>`

#. :wiki-pg:`Line break <Newline>`

   * A way to indicate the end of a :wiki-pg:`line <Line_(text_file)>`

#. :wiki-pg:`Whitespace <Whitespace_character>`

   * A way to separate :wiki-pg:`characters <Character_(computing)>`

#. :wiki-pg:`Indentation <Indentation_(typesetting)>`

   * One style of :wiki-pg:`whitespace <Whitespace_character>`

#. :wiki-pg:`Delimiter`

   * A data boundary marker

Data storage
============

#. :wiki-pg:`Directory <Directory_(computing)>`

   * Cataloging structure for :xref:`computer <computer>` data

#. :wiki-pg:`File <Computer_file>`

   * A way to store data in a :wiki-pg:`computer <Computer>`

#. :wiki-pg:`Path <Path_(computing)>`

   * Identifier for a :wiki-pg:`directory <Directory_(computing)>` or
     :wiki-pg:`file <Computer_file>`

#. :wiki-pg:`Filename extension <Filename_extension>`

   * A way to identify a type of a :wiki-pg:`file <Computer_file>`

#. :wiki-pg:`PDF`

   * A general document :wiki-pg:`filetype <Filename_extension>`

Time
====

#. :wiki-pg:`Time`

   * The passage of events

#. :wiki-pg:`Time standard <Time_standard>`

   * A way to measure :wiki-pg:`time <Time>`

#. :wiki-pg:`ISO 8601 <ISO_8601>`

   * A specific :wiki-pg:`time standard <Time_standard>`

#. :wiki-pg:`UTC <Coordinated_Universal_Time>`

   * A :wiki-pg:`time standard <Time_standard>` that works with
     :wiki-pg:`ISO 8601 <ISO_8601>`

#. :xref:`dencode`

   * Convert between :wiki-pg:`time standards <Time_standard>`

OS specifics
============

#. :xref:`OS`

   * :xref:`computer` resource manager

#. :wiki-pg:`Mac OS <Macintosh_operating_systems>`

   * A common :xref:`operating system <OS>`

#. :wiki-pg:`Mircosoft Windows <Microsoft_Windows>`

   * A common :xref:`operating system <OS>`

#. :wiki-pg:`Linux`

   * A common :xref:`operating system <OS>`, which is
     :wiki-pg:`open-source <Open-source_software>`

#. :xref:`torvalds-interview`

   * Creator of :wiki-pg:`Linux`
   * :xref:`Cited <citation>` at
     :ref:`the spirit of alnoki's apps <zen-spirit>`

#. :xref:`command-line`

   * A direct way to communicate with an :xref:`operating system <OS>`

#. :xref:`cmd.exe <cmd.exe-invocation>`

   * :xref:`command-line` for :wiki-pg:`Windows <Microsoft_Windows>`

#. :linux-die:`bash`

   * :xref:`command-line` for :wiki-pg:`Mac <Macintosh_operating_systems>`
     and :wiki-pg:`Linux`

#. :xref:`Change-bash-prompt`

   * How to change :linux-die:`bash` prompt to a custom
     :xref:`string <string>` like ``$``

#. :wiki-pg:`Exit status <Exit_status>`

   * A report from :wiki-pg:`software <Software>` when it is done

The Internet
============

#. :xref:`internet`

   * An interconnected system of :wiki-pg:`computers <Computer>` and
     information

#. :xref:`website`

   * A way to view content on the :xref:`internet`

#. :xref:`web-browser`

   * A viewer for a :xref:`website <website>`

#. :wiki-pg:`Web browsing history <Web_browsing_history>`

   * :ref:`Identify links <writing-proofread-new>` you have not
     :wiki-pg:`clicked <Point_and_click>`

#. :xref:`webpage`

   * What a :xref:`web browser <web-browser>` shows

#. :wiki-pg:`Hypertext Markup Language (HTML) <HTML>`

   * Standard :wiki-pg:`markup language <Markup_language>` for
     :wiki-pg:`webpages <Webpage>`

#. :xref:`URL`

   * A way to identify a :xref:`webpage <webpage>`

#. :wiki-pg:`Download`

   * Gather information from the :wiki-pg:`Internet`

#. :wiki-pg:`Upload`

   * Provide information to the :wiki-pg:`Internet`

#. :wiki-pg:`Host <Host_(network)>`

   * A :wiki-pg:`computer <Computer>` that provides resources to other
     :wiki-pg:`computers <Computer>` via the :wiki-pg:`Internet`

Information sources
===================

#. :wiki-pg:`Search engine <Web_search_engine>`

   * A :wiki-pg:`software <Software>` system that indexes :wiki-pg:`Internet`
     information

#. :xref:`Google`

   * Preferred :wiki-pg:`search engine <Web_search_engine>`

#. :wiki-pg:`Wikipedia`

   * Preferred source of :xref:`online <internet>` information

#. :xref:`YouTube`

   * For accessing tutorials and other video information

#. :xref:`stack-overflow`

   * Community :wiki-pg:`website <Website>` that provides answers to
     :wiki-pg:`computer <Computer>` questions

Software design standards
=========================

#. :xref:`219-Design`

   * *Smart product* design consulting firm

#. :wiki-pg:`DO-178B`

   * :xref:`Software <software>` design standards for aviation devices

#. :wiki-pg:`Attitude Heading and Reference System (AHRS)
   <Attitude_and_heading_reference_system>`

   * Aviation device, sometimes :wiki-pg:`DO-178B Level A <DO-178B>`

#. :wiki-pg:`Garmin Ltd. <Garmin>`

   * Manufacturer of :wiki-pg:`DO-178B Level A <DO-178B>` aviation products

#. :xref:`why-poignant-guide`

   * Explanation of :xref:`software <software>`, mentioned in :ref:`zen-aipaip`


*********
Financial
*********

Securities mechanics
====================

#. :xref:`corporation`

   * An organization that acts as a single entity

#. :xref:`finance-share`

   * A single unit representing fractional ownership

#. :xref:`finance-stock`

   * The combination of all :xref:`shares <finance-share>` that form
     representative ownership of a :xref:`corporation <corporation>`

#. :xref:`financial-asset`

   * A non-physical asset, like :xref:`shares <finance-share>` of
     :xref:`stock <finance-stock>`

#. :xref:`finance-security`

   * Tradable forms of :xref:`financial assets <financial-asset>`

#. :xref:`brokerage`

   * Facilitates the buying and selling of
     :xref:`securities <finance-security>`

#. :xref:`ticker-symbol`

   * Identifier used to buy or sell a :xref:`security <finance-security>`
     through a :xref:`brokerage <brokerage>`

#. :xref:`dividend`

   * Typically, :xref:`money <money>` that a :xref:`corporation <corporation>`
     pays to its :xref:`shareholders <finance-share>`

Money definitions
=================

#. :wiki-pg:`Finance`

   * The management of :wiki-pg:`money <Money>`

#. :xref:`medium-of-exchange`

   * A widely accepted token that can be exchanged for something else

#. :xref:`money`

   * An item or verifiable record that is accepted as a
     :xref:`medium of exchange <medium-of-exchange>`

#. :xref:`finance-transaction`

   * Typically, an exchange of :xref:`money <money>` for something else

#. :xref:`USD`

   * A unit of :xref:`money <money>`

#. :xref:`finance-cent`

   * :math:`\frac{1}{100}` of a basic :xref:`money <money>` unit

#. :xref:`fee`

   * An amount of :xref:`money <money>` paid for services

#. :xref:`bank`

   * An institution that manages :xref:`money <money>`


***********
Mathematics
***********

#. :wiki-pg:`Factorial`

   * :math:`x! = x(x - 1)(x - 2)...`

#. :xref:`mactex`

   * :wiki-pg:`LaTeX` for :wiki-pg:`Mac <Macintosh_operating_systems>`

#. :xref:`texlive`

   * :wiki-pg:`LaTeX` for :wiki-pg:`Windows <Microsoft_windows>` (and probably
     :wiki-pg:`Linux`)


**********
Philosophy
**********

Personal motivation
===================

#. :xref:`schafer-interview`

   * Reasons for making content
   * :xref:`Cited <citation>` in :ref:`zen-aipaip`

#. :xref:`quantity-trumps-quality`

   * Just keep making content
   * :xref:`Cited <citation>` in :ref:`zen-aipaip`

Places worth visiting
=====================

#. :xref:`msfc-lab`

   * Flight testing procedures :xref:`cited <citation>` in
     :ref:`zen-aipaip`

#. :xref:`caye-caulker`

   * Island with the mantra *go slow*, :xref:`cited <citation>` in
     :ref:`zen-aipaip`
