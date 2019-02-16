.. 0.3.0:

.. _references-links:


#####
Links
#####

This is a centralized and comprehensive list of :xref:`online <internet>`
information :xref:`cited <citation>` throughout :term:`AAAAAA` documentation,
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

#. :xref:`Corey-Schafer-vids`

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

   * Syntax, methods, best practices

#. :xref:`RealPython`

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

#. :xref:`directory`

   * Cataloging structure for :xref:`computer <computer>` data

#. :doc:`pip <python:installing/index>`

   * General installer for :ref:`packages <python:tut-packages>`
   * Used to :ref:`configure a6 <conda-pip-AAAAAA>` for use with
     :doc:`pytest <pytest:index>`

Text
====

#. :xref:`Python-quote-convention`

   * Recommendation for using ``'`` vs ``"`` in :xref:`strings <string>`

#. :ref:`python:comments`

   * Documentation inside :xref:`code <source-code>`

#. :ref:`python:tut-docstrings`

   * :ref:`python:comments` for specific :xref:`Python` components

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

   * Syntax and instance concepts, like ``__init__()``

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

   * Documentation for :xref:`Anaconda`

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

#. :ref:`Conda channels <conda:channels-glossary>`

   * A repository that hosts
     :ref:`conda packages <conda:concept-conda-package>`

#. :xref:`conda-forge`

   * A community-driven :ref:`conda channel <conda:channels-glossary>`

Conda syntax
------------

#. :doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`

   * Quick reference for common :doc:`conda <conda:index>` commands

#. :doc:`conda:commands/create`

   * Make a new :ref:`conda environment <conda:concept-conda-env>`

#. :doc:`conda:commands/install`

   * Add a :ref:`package <conda:concept-conda-package>` to a
     :ref:`conda environment <conda:concept-conda-env>`

#. :ref:`conda:activate-env`

   * Enable use of a :ref:`conda environment <conda:concept-conda-env>`

#. :doc:`conda:user-guide/tasks/manage-environments`

   * Exporting and importing :ref:`environment <conda:concept-conda-env>` files

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

#. :xref:`AAAAAA-repo`

   * :xref:`GitHub` repository for :term:`AAAAAA` project contents

#. :xref:`alnoki-repos`

   * Assorted :xref:`Jupyter Notebooks <Jupyter>` and
     :xref:`code <source-code>` from other tutorials

#. :xref:`GitHub`

   * :xref:`Online <internet>` repository for
     :xref:`software <software>` projects

#. :xref:`AAAAAA-zip-archive`

   * Fastest way to access the :xref:`AAAAAA-repo`

Versioning
==========

#. :xref:`semver`

   * :ref:`Version number <version-list>` guidelines: ``MAJOR.MINOR.PATCH``

#. :xref:`git-commit-guidelines`

   * General guidelines for describing contributions to a project

#. :xref:`commit-conventions`

   * Specific language style for contributing to a project

#. :xref:`mvp-development`

   * An incremental way to create or add features


*******************
Git version control
*******************

General
=======

#. :xref:`git-manual`

   * Quick practical reference

#. :xref:`git-book`

   * In-depth conceptual explanations

#. :xref:`git-download`

   * Download :xref:`Git <git-manual>`

#. :xref:`git-setup`

   * Getting started

#. :xref:`sha1`

   * Unique identifier attached to each :xref:`commit <git-commit>`

Core commands
=============

#. :xref:`git-config`

   * Setup user credentials

#. :xref:`git-log`

   * See project history

#. :xref:`git-commit`

   * Create saved changes to a project

#. :xref:`git-push`

   * Upload a :xref:`commit <git-commit>`

#. :xref:`git-tag`

   * Assign a special identifier to a :xref:`commit <git-commit>`

#. :xref:`git-branch`

   * Work with independent sequences of :xref:`commits <git-commit>`

#. :xref:`git-checkout`

   * Switch between :xref:`branches <git-branch>`

#. :xref:`git-merge`

   * Combine :xref:`branches <git-branch>`

Text manipulation
=================

#. :xref:`less-pager`

   * For viewing :xref:`git-log`

#. :xref:`Vim`

   * For :xref:`git-config` and :xref:`git-commit`

#. :xref:`Vim-tutorial`

   * Learn :xref:`Vim <Vim>`

#. :xref:`Vim-cheatsheet`

   * Common :xref:`Vim <Vim>` commands

Special features
================

#. :xref:`git-log-formatting`

   * Special options for inspecting :xref:`git-log`

#. :xref:`list-git-developers`

   * Identifying unique :xref:`committers <git-commit>`

#. :xref:`github-change-authors`

   * :xref:`GitHub` instructions to re-write :xref:`git-commit` history

#. :xref:`git-branch-filtering`

   * Extra options for
     :xref:`re-writing commit history <github-change-authors>`


*************
Documentation
*************

General
=======

#. :doc:`Python Developer's Guide to Documenting Python <py-dev-guide:documenting>`

   * Guide to general :doc:`Sphinx <sphinx:intro>` use
   * :doc:`reStructuredTest <usage/restructuredtext/basics>` style guide

#. :xref:`RealPython Guide to Documenting Python <documenting-python>`

   * Recommended practices for documenting :xref:`Python`
   * Tips and examples from :xref:`RealPython`

Sphinx
======

Practical use
-------------

#. :doc:`Sphinx <sphinx:intro>`

   * Official documentation for the :doc:`Sphinx <sphinx:intro>`
     documentation engine

#. :doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`

   * How to start a new documentation project

#. :doc:`Matplotlib sampledoc tutorial <matplotlib-sampledoc:index>`

   * Quick walkthrough with practical syntax examples
   * Interactive :xref:`Python` examples, using plots

#. :xref:`Willing-Sphinx`

   * Common workflow tasks [#]_, like
     :ref:`checking links <sphinx-checking-links>`
   * Team development ideologies

#. :xref:`sphinx-autobuild`

   * Automatically update
     :ref:`documentation builds <sphinx-building-documentation>`

#. :xref:`Writer-intro-to-Sphinx`

   * General explanation of using
     :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   * From Eric Holscher, co-founder of
     :doc:`Read the Docs<rtfd:index>`

#. :doc:`HTTP server <python:library/http.server>`

   * :ref:`Python package <python:tut-packages>` that creates a
     :xref:`website <website>` for viewing documentation

.. rubric:: Footnotes

.. [#]
   .. csv-table::
      :header: Time in video, Topic
      :align: center

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

   * How to configure a :doc:`Sphinx <sphinx:intro>` project

#. :ref:`sphinx:toctree-directive`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` for
     creating project document structure

#. :doc:`Autodoc extension <sphinx:usage/extensions/autodoc>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` for generating
     documentation straight from :xref:`source code <source-code>`

#. :ref:`sublime-with-sphinx:use the external links extension`

   * Instructions for installing an example
     :doc:`Sphinx extension <sphinx:usage/extensions/index>`
   * Similar to :ref:`external link management <sphinx-xref>` in
     :term:`AAAAAA`

#. :rst:role:`sphinx:math`

   * :doc:`Role <sphinx:usage/restructuredtext/roles>` for using
     :xref:`LaTeX` in-line

#. :rst:dir:`sphinx:math`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` for using
     :xref:`LaTeX` on its own line

#. :xref:`http socket error fix <http-socket-error>`

   * Potential problem (and solution) when
     :ref:`building documentatoin <sphinx-building-documentation>`

#. :doc:`sphinx:usage/restructuredtext/domains`

   * Collection of
     :doc:`directives <sphinx:usage/restructuredtext/directives>` and
     :doc:`roles <sphinx:usage/restructuredtext/roles>` for specific topics

With Read the Docs
------------------

#. :xref:`Yusuf-Sphinx-RTD`

   * Setting up a project using :doc:`quickstart <sphinx:usage/quickstart>`
   * :rst:dir:`toctree` and associated documentation structure
   * Basic :ref:`tools-restructured-text` syntax

#. :doc:`Read the Docs<rtfd:index>`

   * :xref:`Online <internet>` repository for :xref:`software <software>`
     documentation

#. :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`

   * Tutorial for starting a :doc:`Sphinx <sphinx:intro>` project hosted on
     :doc:`Read the Docs<rtfd:index>`

#. :doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`

   * Contains sample :ref:`tools-restructured-text` syntax

#. :doc:`rtfd:webhooks`

   * Automatic project modification detection

#. :doc:`rtfd:versions`

   * Automatic support for :ref:`versions <version-list>`

Managing references
-------------------

#. :doc:`Intersphinx extension <sphinx:usage/extensions/intersphinx>`

   * Official :doc:`Sphinx <sphinx:intro>` documentation for referencing
     other :doc:`Sphinx <sphinx:intro>` projects

#. :xref:`xref-ext`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to manage
     common :ref:`links <references-links>` in a project

#. :xref:`intersphinx-inv-targets`

   * Explains how to interpret
     :doc:`objects.inv <sphinx:usage/extensions/intersphinx>` files when
     using :doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`

#. :xref:`intersphinx-inv-parser`

   * Sample code for analyzing
     :doc:`objects.inv <sphinx:usage/extensions/intersphinx>` files

#. :xref:`intersphinx-numpy-matplotlib`

   * Instructions to for using
     :doc:`Intersphinx <usage/extensions/intersphinx>` with specific
     :ref:`packages <python:tut-packages>`

#. :xref:`citation`

   * A way to create a :ref:`reference <references>` to a source of information

#. :xref:`bibtex`

   * :xref:`citation` management format

#. :doc:`BibTeX extension <bibtex:index>`

   * :ref:`Sphinx extension <tools-sphinx>` for :xref:`citing <citation>` with
     :xref:`bibtex`

#. :xref:`book`

   * Information source

#. :xref:`ISBN`

   * Unique identifier for :xref:`books <book>`

#. :xref:`ottobib`

   * Provides :xref:`bibtex` data for a :xref:`book <book>` with a given
     :xref:`ISBN`

#. :xref:`bibtex-syntax`

   * Syntax for identifying specific :xref:`citation <citation>` components

#. :xref:`cite-multiple-authors`

   * Use of ``et. al``

Showing code
------------

#. :rst:dir:`code-block`

   * :doc:`Directive <sphinx:usage/restructuredtext/directives>` to show
     sections of :xref:`code <source-code>`

#. :doc:`Autodoc <sphinx:usage/extensions/autodoc>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to include content
     from code :ref:`docstrings <python:tut-docstrings>`

#. :ref:`NumPy docstrings <numpy:format>`

   * :ref:`Docstring <python:tut-docstrings>` format provided by
     :doc:`NumPy <numpy:about>`

#. :doc:`Napoleon <sphinx:usage/extensions/napoleon>`

   * :doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
     content from :ref:`NumPy docstrings <numpy:format>`

#. :pep:`257`

   * Official conventions for :ref:`docstrings <python:tut-docstrings>`

#. :pep:`Type annotations <484>`

   * Syntax to indicate :doc:`types <python:library/stdtypes>` in
     :xref:`code <source-code>`

#. :ref:`sphinx:python-roles`

   * :doc:`Sphinx Domain <sphinx:usage/restructuredtext/domains>` for
     documenting :xref:`Python` components

#. :doc:`Read the Docs sample Python module <demo/api>`

   * Sample syntax for :doc:`autodoc <sphinx:usage/extensions/autodoc>`

#. :doc:`napoleon:example_numpy`

   * Sample :ref:`NumPy docstring <numpy:format>` syntax for
     :doc:`napoleon <sphinx:usage/extensions/napoleon>`

#. :ref:`sphinx:info-field-lists`

   * :ref:`tools-restructured-text` syntax that
     :doc:`napoleon <sphinx:usage/extensions/napoleon>` produces

reStructuredText
================

General
-------

#. :doc:`sphinx:usage/restructuredtext/basics`

   * :doc:`Sphinx <sphinx:intro>` explanation of
     :doc:`reST <sphinx:usage/restructuredtext/basics>` markup language

#. :xref:`reST-documentation`

   * Official :doc:`reST <sphinx:usage/restructuredtext/basics>`
     documentation

#. :xref:`quick-reST`

   * Quick reference with
     :doc:`reST <sphinx:usage/restructuredtext/basics>` examples

#. :xref:`Doc8`

   * Style checker for :doc:`reST <sphinx:usage/restructuredtext/basics>`

Syntax
------

#. :xref:`reST-cheatsheet`

   * Quick reference for :doc:`reST <sphinx:usage/restructuredtext/basics>`
     usage

#. :xref:`reST-list-indentation`

   * Syntax tip

#. :ref:`Tables <sphinx:table-directives>`

   * Syntax options

#. :doc:`Role <sphinx:usage/restructuredtext/roles>`

   * Element that marks a piece of text, usually in-line

#. :doc:`Directive <sphinx:usage/restructuredtext/directives>`

   * Element that marks a block of text

#. :rst:dir:`toctree`

   * Project structure management

#. :ref:`Label role <ref-role>`

   * :doc:`Role <sphinx:usage/restructuredtext/roles>` syntax to
     :xref:`link <URL>` to arbritrary documentation locations

#. :xref:`admonition`

   * A special badge of text [#]_

.. rubric:: Footnotes

.. [#]
      .. danger::

         This is an :xref:`admonotion <admonition>`

Engine-agnostic tools
=====================

#. :xref:`tables-generator`

   * :xref:`Online <internet>` tool to format tables in :xref:`LaTeX`,
     :xref:`Markdown`, :ref:`tools-restructured-text`, and plain text

#. :xref:`LaTeX`

   * Typesetting system for documenting equations in
     :xref:`Jupyter Notebooks <Jupyter>` and in
     :doc:`Sphinx <sphinx:intro>`

#. :xref:`Markdown`

   * Language syntax used to generate tables, lists, and other components
   * Used for :xref:`GitHub`, :xref:`Jupyter Notebooks <Jupyter>`, and
     :ref:`AAAAAA task management <versioning-td3>`

*****
Tools
*****

Jupyter
=======

General
-------

#. :xref:`Jupyter Notebooks <Jupyter>`

   * Interactive :xref:`Python` environment
   * :xref:`Code <source-code>`, :xref:`LaTeX`, :xref:`Markdown`, and plotting
     in one document

#. :xref:`Schafer-Jupyter`

   * Recommended for learning to use :xref:`Jupyter Notebooks <Jupyter>`
   * Tutorial video from :xref:`Corey Schafer <Corey-Schafer-vids>`

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

   * Preview :xref:`Markdown` and :xref:`LaTeX`

VS Code
=======

General
-------

#. :xref:`VS-Code`

   * :xref:`Open-source <open-source>` environment for
     :xref:`software <software>` development
   * Has a collection of :xref:`extensions <VS-Code-extensions>` developed by
     the :xref:`open-source` community

#. :xref:`VS-Code-extensions`

   * Tools to enable additional functionality

#. :xref:`VS-Code-Python-tutorial`

   * Setup and basic usage

#. :xref:`VS-Code-unit-testing`

   * Use :ref:`tools-pytest`

#. :xref:`VS-Code-settings`

   * Configurations in ``settings.json``

#. :xref:`VS Code integrated terminal <VS-Code-terminal>`

   * Using a :xref:`command line <command-line>`

#. :xref:`VS Code command palette <command-palette>`

   * Direct input for :xref:`software <software>` commands

#. :xref:`VS-Code-insiders`

   * Has the latest features, may have problems

Extensions
----------

#. :xref:`GitLens`

   * Enhanced :ref:`tools-git` functionality

#. :xref:`VS-Code-Python-ext`

   * Work with :ref:`tools-python`

#. :xref:`Selecting the Python interpreter <VS-Code-interpreter>`

   * Integrate the :doc:`Python interpreter <python:tutorial/interpreter>`

#. :xref:`Test-explorer-UI`

   * Work with :ref:`tools-pytest`

#. :xref:`VS-Code-bookmarks-ext`

   * Mark and navigate :xref:`source code <source-code>`

#. :xref:`RST-preview-ext`

   * Syntax highlighting for
     :ref:`tools-restructured-text`
   * Limited preview functionality

#. :xref:`doc8-newline-issue`

   * Fix for syntax highlight problem in :xref:`RST-preview-ext`


*********
Computers
*********

General
=======

#. :xref:`computer`

   * A system that manipulates information

#. :xref:`mobile-device`

   * A small, portable :xref:`computer <computer>`

#. :xref:`source-code`

   * A way to communicate to a :xref:`computer <computer>`

#. :xref:`software`

   * A structured collection of :xref:`source code <source-code>`

#. :xref:`copy-paste`

   * One way to share :xref:`source code <source-code>`

#. :xref:`string`

   * How a :xref:`computer <computer>` stores text

OS specifics
============

#. :xref:`OS`

   * :xref:`computer` resource manager

#. :xref:`Mac OS<Mac>`

   * :xref:`Wikipedia` article about the :xref:`Mac OS<Mac>`

#. :xref:`Windows OS<Windows>`

   * :xref:`Wikipedia` article about the :xref:`Windows OS<Windows>`

#. :xref:`Linux OS family<Linux>`

   * :xref:`Wikipedia` article about the :xref:`Linux OS family<Linux>`

#. :xref:`torvalds-interview`

   * Creator of :xref:`Linux`
   * :xref:`Cited <citation>` at
     :ref:`the spirit of alnoki's apps <zen-spirit>`

#. :xref:`command-line`

   * A direct way to communicate with an :xref:`operating system <OS>`

#. :xref:`cmd.exe-invocation`

   * :xref:`command-line` for :xref:`Windows`

#. :xref:`bash-man-page`

   * :xref:`command-line` for :xref:`Mac` and :xref:`Linux`

#. :xref:`Change-bash-prompt`

   * How to change :xref:`bash <bash-man-page>` prompt to a custom
     :xref:`string <string>` like ``$``

Online information
==================

#. :xref:`internet`

   * An interconnected system of information

#. :xref:`website`

   * A way to view content on the :xref:`internet`

#. :xref:`web-browser`

   * A viewer for a :xref:`website <website>`

#. :xref:`webpage`

   * What a :xref:`web browser <web-browser>` shows

#. :xref:`URL`

   * A way to locate a :xref:`webpage <webpage>`

#. :xref:`Google`

   * Preferred way to search for :xref:`online <internet>` information

#. :xref:`Wikipedia`

   * Preferred source of :xref:`online <internet>` information

#. :xref:`YouTube`

   * For accessing tutorials and other video information

#. :xref:`Open-source software <open-source>`

   * Public way to share :xref:`source code <source-code>`

Software design standards
=========================

#. :xref:`219-Design`

   * *Smart product* design consulting firm

#. :xref:`DO-178B`

   * :xref:`Software <software>` design standards for aviation devices

#. :xref:`Attitude Heading and Reference System (AHRS) <AHRS>`

   * Aviation device certified to :xref:`DO-178B Level A <DO-178B>`

#. :xref:`Garmin`

   * Manufacturer of :xref:`DO-178B Level A <DO-178B>` aviation products

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

#. :xref:`factorial-definition`

   * :xref:`Wikipedia` page for :math:`x!`


**********
Philosophy
**********

Personal motivation
===================

#. :xref:`schafer-interview`

   * Reasons for making content
   * :xref:`Cited <citation>` in :ref:`zen-aipaip`

Places worth visiting
=====================

#. :xref:`msfc-lab`

   * Flight testing procedures :xref:`cited <citation>` in
     :ref:`zen-aipaip`

#. :xref:`caye-caulker`

   * Island with the mantra *go slow*, :xref:`cited <citation>` in
     :ref:`zen-aipaip`
