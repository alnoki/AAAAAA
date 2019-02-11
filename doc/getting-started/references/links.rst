.. 14a4fa4:

.. _references-links:


#####
Links
#####

This is a centralized and comprehensive list of online resources related to
:term:`AAAAAA`, and is managed according to
:ref:`references procedures <sphinx-managing-references>`

Links are not necessarily in order, but links with high priority are usually
placed at the top of a section

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

   * Definitive reference for the :xref:`Python` computer language

#. :std:doc:`python:tutorial/index`

   * Official :xref:`Python` tutorial from :xref:`Python.org <Python>`

#. :pep:`8`

   * Official :xref:`Python` style guide

#. :std:doc:`python:howto/functional`

   * Official tutorial on :xref:`Python` programming techniques

#. :std:doc:`python:howto/index`

   * Official in-depth :xref:`Python` tutorials for various advanced topics

#. :xref:`RealPython`

   * Comprehensive blog-style website with examples, guides, tips, etc.

#. :doc:`tutorial/interpreter`

   * The mechanism that runs :xref:`Python` code

Projects
========

#. :ref:`python:tut-packages`

   * Structuring of code and :xref:`directories <directory>` in a project

#. :xref:`print-dir-tree`

   * Sample code to print out a :xref:`directory <directory>` tree
   * Adapted for :ref:`directory tree procedure <writing-make-dir-tree>`

#. :xref:`directory`

   * Cataloging structure with references to computer data

Text
====

#. :xref:`Python-quote-convention`

   * Recommendation for using ``'`` vs ``"`` in :xref:`Python`

#. :ref:`python:comments`

   * Documentation inside code that is human-readable

#. :ref:`python:tut-docstrings`

   * :ref:`python:comments` for specific :xref:`Python` code components

Types
=====

#. :std:doc:`python:library/stdtypes`

   * Standard :xref:`Python` data structures

#. :term:`Object <python:object>`

   * The most basic :std:doc:`type <python:library/stdtypes>` upon which others
     are based

#. :std:ref:`python:tut-dictionaries`

   * A :std:doc:`type <python:library/stdtypes>` containing *key: value* pairs

#. :xref:`realpython-type-checking`

   * Guide to using correct :std:doc:`types <python:library/stdtypes>` in code

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

   * Specified processes that can act on :term:`arguments <python:argument>`

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
     which can be a function of
     :ref:`instance variables <python:tut-class-and-instance-variables>`
   * :py:attr:`AAAAAA.ledger.Transaction.per_share_amount` is a
     :py:class:`python:property`

Environments
============

#. :xref:`Anaconda`

   * :xref:`Python` package dependency manager and environment configurator

#. :std:doc:`anaconda:anaconda/index`

   * Documentation for :xref:`Anaconda`

#. :std:doc:`Miniconda<conda:user-guide/install/index>`

   * Abbreviated version of :xref:`Anaconda` that is quick to download

#. :std:doc:`conda:index`

   * Command line configurator for :xref:`Anaconda`

#. :ref:`conda:starting-conda`

   * Invocation methods for :std:doc:`conda <conda:index>`

#. :ref:`Conda package <conda:concept-conda-package>`

   * A collection of :xref:`Python` software contained in :xref:`Anaconda`

#. :ref:`Conda environment <conda:concept-conda-env>`

   * A collection of :ref:`conda packages <conda:concept-conda-package>`

#. :ref:`Conda channels <conda:channels-glossary>`

   * A repository that hosts
     :ref:`conda packages <conda:concept-conda-package>`

#. :xref:`conda-forge`

   * A community-driven :ref:`conda channel <conda:channels-glossary>`

#. :std:doc:`pip <python:installing/index>`

   * General installer for :xref:`Python` software
   * Used to :ref:`configure a6 <conda-pip-AAAAAA>` for use with
     :std:doc:`pytest <pytest:index>`

Conda syntax
------------

#. :std:doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`

   * Quick reference for common :std:doc:`conda <conda:index>` commands

#. :std:doc:`conda:commands/create`

   * Make a new :ref:`conda environment <conda:concept-conda-env>`

#. :std:doc:`conda:commands/install`

   * Add a :ref:`package <conda:concept-conda-package>` to a
     :ref:`conda environment <conda:concept-conda-env>`

#. :ref:`conda:activate-env`

   * Enable use of a :ref:`conda environment <conda:concept-conda-env>`

#. :std:doc:`conda:user-guide/tasks/manage-environments`

   * Exporting and importing :ref:`environment <conda:concept-conda-env>` files

#. :std:doc:`conda:commands/clean`

   * Removing unnecessary :ref:`conda packages <conda:concept-conda-package>`

#. :std:doc:`conda:commands/update`

   * Get the most recent version of
     :ref:`conda packages <conda:concept-conda-package>`

#. :std:doc:`conda:commands/list`

   * List the :ref:`conda packages <conda:concept-conda-package>` in a
     :ref:`conda environment <conda:concept-conda-env>`

OS-specific
============

#. :xref:`OS`

   * Computer system resource manager

#. :xref:`Mac OS<Mac>`

   * :xref:`Wikipedia` article about the :xref:`Mac OS<Mac>`

#. :xref:`Windows OS<Windows>`

   * :xref:`Wikipedia` article about the :xref:`Windows OS<Windows>`

#. :xref:`Linux OS family<Linux>`

   * :xref:`Wikipedia` article about the :xref:`Linux OS family<Linux>`

#. :xref:`cmd.exe-invocation`

   * :xref:`Windows` command line

#. :xref:`bash-man-page`

   * Command line for :xref:`Mac` and :xref:`Linux`

#. :xref:`Change-bash-prompt`

   * How to change :xref:`bash <bash-man-page>` prompt to a custom string like
     ``$``


********
Packages
********

Numerical Analysis
==================

NumPy
-----

#. :std:doc:`numpy:about`

   * Fundamental :ref:`package <conda:concept-conda-package>` for scientific
     :xref:`Python` computing

#. :std:doc:`numpy:user/quickstart`

   * Official :std:doc:`NumPy <numpy:about>` tutorial

#. :xref:`codebasics-numpy`

   * Recommended :std:doc:`NumPy <numpy:about>` tutorial on :xref:`YouTube`

Matplotlib
----------

#. :std:doc:`Matplotlib <matplotlib:index>`

   * Plotting tool for numerical data

#. :std:doc:`matplotlib:tutorials/index`

   * Instructions to use :std:doc:`Matplotlib <matplotlib:index>`

#. :xref:`codebasics-matplotlib`

   * Recommended :std:doc:`Matplotlib <matplotlib:index>` tutorial on
     :xref:`YouTube`

pandas
------

#. :std:doc:`pandas <pandas:index>`

   * For handling datasets

#. :std:doc:`pandas:getting_started/10min`

   * Official :std:doc:`pandas <pandas:index>` tutorial

#. :xref:`codebasics-pandas`

   * Recommended :std:doc:`pandas <pandas:index>` tutorial on :xref:`YouTube`

pytest
======

#. :std:doc:`pytest <pytest:index>`

   * Framework for writing test code

#. :xref:`codebasics-pytest`

   * Recommended :std:doc:`pytest <pytest:index>` tutorial on :xref:`YouTube`

#. :std:doc:`pytest tutorials <pytest:contents>`

   * Official comprehensive :std:doc:`pytest <pytest:index>` walkthroughs

#. :std:doc:`pytest:goodpractices`

   * Configuring :std:doc:`pytest <pytest:index>` to run with :term:`a6`

#. :xref:`pytest-discovery-issue`

   * :xref:`VS-Code` integration problem upon release of
     :std:doc:`pytest <pytest:index>`

******************
Project management
******************

AAAAAA codebase
===============

#. :xref:`AAAAAA-repo`

   * :xref:`GitHub` repository for :term:`AAAAAA` source code, test code, and
     documentation

#. :xref:`alnoki-repos`

   * Assorted :xref:`Jupyter Notebooks <Jupyter>` and code from other tutorials

#. :xref:`GitHub`

   * Online repository for software projects

#. :xref:`AAAAAA-zip-archive`

   * Compressed archive of :xref:`AAAAAA-repo` that is quick to download

Versioning
==========

#. :xref:`semver`

   * Guidelines for version number of style ``MAJOR.MINOR.PATCH``

#. :xref:`git-commit-guidelines`

   * General guidelines for contributing to a project

#. :xref:`commit-conventions`

   * Specific language style for contributing to a project


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

   * Set up user credentials

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

   * Learn :xref:`Vim` in several minutes

#. :xref:`Vim-cheatsheet`

   * Common :xref:`Vim` commands

Special features
================

#. :xref:`git-log-formatting`

   * Special formatting options for :xref:`git-log`

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

#. :std:doc:`Official Python Developer's Guide to Documenting Python <py-dev-guide:documenting>`

   * General :std:doc:`Sphinx <sphinx:intro>` use and
     :std:doc:`reStructuredTest <usage/restructuredtext/basics>` style guide

#. :xref:`RealPython Guide to Documenting Python <documenting-python>`

   * Recommended practices for documenting :xref:`Python`
   * Tips and examples from :xref:`RealPython`

Sphinx
======

Practical use
-------------

#. :std:doc:`Sphinx <sphinx:intro>`

   * Official documentation for the :std:doc:`Sphinx <sphinx:intro>`
     documentation engine

#. :std:doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`

   * How to start a documentation project from scratch

#. :std:doc:`Matplotlib sampledoc tutorial <matplotlib-sampledoc:index>`

   * Quick walkthrough with practical syntax examples
   * Interactive :xref:`Python` examples, using plots

#. :xref:`Willing-Sphinx`

   * Common workflow tasks
   * :ref:`sphinx-checking-links`
   * Team development ideologies

   .. csv-table::
      :header: "Time in video", "Topic"
      :align: center

      10:15, Incorporating :ref:`Jupyter Notebooks <tools-jupyter>`
      13:00, Checking spelling
      14:00, Incorporating images
      15:15, Including code
      17:00, Continuous integration
      20:00, :std:doc:`Autodoc <sphinx:usage/extensions/autodoc>`
      24:15, :ref:`Themes <tools-sphinx>`

#. :xref:`Writer-intro-to-Sphinx`

   * General explanation of using
     :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
     , written by Eric Holscher, co-founder of
     :std:doc:`Read the Docs<rtfd:index>`

Usage specifics
---------------

#. :std:doc:`sphinx:usage/extensions/index`

   * Additional functionalities for :std:doc:`Sphinx <sphinx:intro>` engine

#. :std:doc:`conf.py usage<sphinx:usage/configuration>`

   * How to configure a :std:doc:`Sphinx <sphinx:intro>` project

#. :ref:`sphinx:toctree-directive`

   * :std:doc:`Directive <sphinx:usage/restructuredtext/directives>` for
     creating project document structure

#. :std:doc:`Autodoc extension <sphinx:usage/extensions/autodoc>`

   * :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` for generating
     documentation straight from :xref:`Python` source code

#. :ref:`sublime-with-sphinx:use the external links extension`

   * Instructions for installing an example
     :std:doc:`Sphinx extension <sphinx:usage/extensions/index>`
   * Similar to :ref:`link management <sphinx-managing-references>` in
     :term:`AAAAAA`

#. :rst:role:`sphinx:math`

   * :std:doc:`Role <sphinx:usage/restructuredtext/roles>` for using
     :xref:`LaTeX` in-line

#. :rst:dir:`sphinx:math`

   * :std:doc:`Directive <sphinx:usage/restructuredtext/directives>` for using
     :xref:`LaTeX` on its own line

#. :xref:`http socket error fix <http-socket-error>`

   * Managing errors during documentation builds

#. :std:doc:`sphinx:usage/restructuredtext/domains`

   * Collection of
     :std:doc:`directives <sphinx:usage/restructuredtext/directives>` and
     :std:doc:`roles <sphinx:usage/restructuredtext/roles>` for specific topics

With Read the Docs
------------------

#. :xref:`Yusuf-Sphinx-RTD`

   * Setting up a project using :std:doc:`quickstart <sphinx:usage/quickstart>`
   * :std:doc:`toctree <sphinx:usage/quickstart>` and associated documentation
     structure
   * Basic :std:doc:`reST <usage/restructuredtext/basics>` syntax

#. :std:doc:`Read the Docs<rtfd:index>`

   * Online repository for hosting software documentation

#. :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`

   * Tutorial for starting a :std:doc:`Sphinx <sphinx:intro>` project hosted on
     :std:doc:`Read the Docs<rtfd:index>`

#. :std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`

   * A :std:doc:`Sphinx <sphinx:intro>` theme for creating a mobile-friendly
     webpage layout

Managing references
-------------------

#. :std:doc:`Intersphinx extension <sphinx:usage/extensions/intersphinx>`

   * Official :std:doc:`Sphinx <sphinx:intro>` documentation for referencing
     other :std:doc:`Sphinx <sphinx:intro>` projects

#. :xref:`xref-ext`

   * :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` to manage
     common external references in a project

#. :xref:`intersphinx-inv-targets`

   * Explains how to interpret
     :std:doc:`objects.inv <sphinx:usage/extensions/intersphinx>` files when
     using :std:doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`

#. :xref:`intersphinx-inv-parser`

   * Sample code for analyzing
     :std:doc:`objects.inv <sphinx:usage/extensions/intersphinx>` files

#. :xref:`intersphinx-numpy-matplotlib`

   * Instructions to reference numerical analysis and plotting tools via
     :std:doc:`Intersphinx <usage/extensions/intersphinx>`

#. :xref:`bibtex`

   * Citation management file format

#. :doc:`BibTeX extension <bibtex:index>`

   * :ref:`Sphinx extension <tools-sphinx>` for citing with :xref:`bibtex`

#. :xref:`ottobib`

   * :xref:`bibtex` database for books

#. :xref:`ISBN`

   * Unique identifier for books

Showing code
------------

#. :doc:`Autodoc <sphinx:usage/extensions/autodoc>`

   * :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
     content from code :ref:`docstrings <python:tut-docstrings>`

#. :ref:`NumPy docstrings <numpy:format>`

   * :ref:`Docstring <python:tut-docstrings>` format provided by
     :std:doc:`NumPy <numpy:about>`

#. :doc:`Napoleon <sphinx:usage/extensions/napoleon>`

   * :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
     content from :ref:`NumPy docstrings <numpy:format>`

#. :pep:`257`

   * Official conventions for :ref:`docstrings <python:tut-docstrings>`

#. :pep:`Type annotations <484>`

   * Syntax to indicate :std:doc:`types <python:library/stdtypes>` in code

#. :ref:`sphinx:python-roles`

   * :std:doc:`Domain <sphinx:usage/restructuredtext/domains>` for documenting
     :xref:`Python` components

#. :std:doc:`Read the Docs sample Python module <demo/api>`

   * Sample syntax for :doc:`autodoc <sphinx:usage/extensions/autodoc>`

#. :doc:`napoleon:example_numpy`

   * Sample :ref:`NumPy docstring <numpy:format>` syntax for
     :doc:`napoleon <sphinx:usage/extensions/napoleon>`

#. :ref:`sphinx:info-field-lists`

   * Syntax that :doc:`napoleon <sphinx:usage/extensions/napoleon>` produces

reStructuredText
================

General
-------

#. :std:doc:`sphinx:usage/restructuredtext/basics`

   * :std:doc:`Sphinx <sphinx:intro>` explanation of
     :std:doc:`reST <sphinx:usage/restructuredtext/basics>` markup language

#. :xref:`reST-documentation`

   * Official :std:doc:`reST <sphinx:usage/restructuredtext/basics>`
     documentation

#. :xref:`quick-reST`

   * Quick reference with
     :std:doc:`reST <sphinx:usage/restructuredtext/basics>` examples

#. :xref:`Doc8`

   * Style checker for :std:doc:`reST <sphinx:usage/restructuredtext/basics>`

Syntax
------

#. :xref:`reST-cheatsheet`

   * Quick reference for :std:doc:`reST <sphinx:usage/restructuredtext/basics>`
     usage

#. :xref:`reST-list-indentation`

   * Explanation of nested list syntax

#. :ref:`Tables <sphinx:table-directives>`

   * Syntax for creating various table styles

#. :doc:`Role <sphinx:usage/restructuredtext/roles>`

   * Element that marks a piece of text, usually in-line

#. :doc:`Directive <sphinx:usage/restructuredtext/directives>`

   * Element that marks a block of text

#. :ref:`Label role <ref-role>`

   * :doc:`Role <sphinx:usage/restructuredtext/roles>` syntax to link to
     arbritrary documentation components

#. :xref:`admonition`

   * A special badge of text

Engine-agnostic tools
=====================

#. :xref:`tables-generator`

   * Online tool to format tables in :xref:`Markdown`,
     :std:doc:`usage/restructuredtext/basics`, and plain text

#. :xref:`LaTeX`

   * Typesetting system for documenting equations in
     :xref:`Jupyter Notebooks <Jupyter>` and in
     :std:doc:`Sphinx <sphinx:intro>`

#. :xref:`Markdown`

   * Language syntax used to generate tables, lists, etc. for :xref:`GitHub`
     and :xref:`Jupyter Notebooks <Jupyter>`


***********
Mathematics
***********

#. :xref:`factorial-definition`

   * :xref:`Wikipedia` factorial page


*****
Tools
*****

Jupyter
=======

General
-------

#. :xref:`Jupyter Notebooks <Jupyter>`

   * Interactive :xref:`Python` notebook format used for algorithm development
   * Code, :xref:`LaTeX`, :xref:`Markdown`, and plotting in one document

#. :xref:`Schafer-Jupyter`

   * Recommended starting point for learning to use
     :xref:`Jupyter Notebooks <Jupyter>`
   * Tutorial video produced by :xref:`Corey Schafer <Corey-Schafer-vids>`

#. :xref:`AAAAAA-nbs`

   * Online viewer for :xref:`Jupyter Notebooks <Jupyter>` in :term:`AAAAAA`

Extensions
----------

#. :std:doc:`nb-extensions:index`

   * Additional functionality for :xref:`Jupyter Notebooks <Jupyter>`

#. :std:doc:`nb-extensions:nbextensions/collapsible_headings/readme`

   * Section navigation and management

#. :std:doc:`nb-extensions:nbextensions/toc2/README`

   * Automatic section linking

#. :std:doc:`nb-extensions:nbextensions/varInspector/README`

   * Inspect data values

#. :xref:`live-md-preview`

   * Preview :xref:`Markdown` and :xref:`LaTeX` syntax real-time

VS Code
=======

General
-------

#. :xref:`VS-Code`

   * Preferred :xref:`open-source` environment for software development,
     documentation, and testing
   * Has a collection of :xref:`extensions <VS-Code-extensions>` developed by
     the :xref:`open-source` community

#. :xref:`VS-Code-extensions`

   * Tools to enable additional functionality

#. :xref:`VS-Code-Python-tutorial`

   * Tutorial for using :xref:`Python` in :xref:`VS-Code`

#. :xref:`VS-Code-unit-testing`

   * Enables use of :std:doc:`pytest <pytest:index>` with :xref:`VS-Code`

#. :xref:`VS-Code-settings`

   * Explanation of user configurations via ``settings.json``

#. :xref:`VS Code integrated terminal <VS-Code-terminal>`

   * Description of using a terminal inside :xref:`VS-Code`

#. :xref:`VS Code command palette <command-palette>`

   * Direct input for various development commands in :xref:`VS-Code`

#. :xref:`VS-Code-insiders`

   * Has the latest features, may be unstable

Extensions
----------

#. :xref:`GitLens`

   * Enhanced :ref:`tools-git` functionality

#. :xref:`VS-Code-Python-ext`

   * Syntax highlighting, autocomplete, etc.

#. :xref:`Selecting the Python interpreter <VS-Code-interpreter>`

   * Selecting the version of :xref:`Python` to use in :xref:`VS-Code`

#. :xref:`Test-explorer-UI`

   * Graphical interface that enables use of :std:doc:`pytest <pytest:index>`

#. :xref:`VS-Code-bookmarks-ext`

   * Tool for marking and navigating to lines in code

#. :xref:`RST-preview-ext`

   * Syntax highlighting for
     :std:doc:`reST <sphinx:usage/restructuredtext/basics>`
   * Limited live preview functionality

#. :xref:`doc8-newline-issue`

   * Fix for syntax highlighter bug in :xref:`RST-preview-ext`


****************************
General computer information
****************************

Online information
==================

#. :xref:`Google`

   * Preferred online search engine for general topic inquiries

#. :xref:`Wikipedia`

   * Preferred online encyclopedia

#. :xref:`YouTube`

   * For accessing tutorials and other video information

#. :xref:`Open-source software <open-source>`

   * :xref:`Wikipedia` article

Software design standards
=========================

#. :xref:`219-Design`

   * Embedded systems design consulting firm

#. :xref:`DO-178B`

   * Software design assurance standards for aviation devices

#. :xref:`Attitude Heading and Reference System (AHRS) <AHRS>`

   * Aviation device certified to :xref:`DO-178B Level A <DO-178B>`

#. :xref:`Garmin`

   * Manufacturer of :xref:`DO-178B Level A <DO-178B>` aviation products

*********
Financial
*********

Securities mechanics
====================

#. :xref:`corporation`

   * An organization that acts as a single entity

#. :xref:`finance-share`

   * A single unit representing fractional owenership

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

   * A widely accepted token that can be exhanged for something else

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
