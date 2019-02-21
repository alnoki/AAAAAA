.. 0.3.0

.. _concepts-tools:


#####
Tools
#####

.. contents::
   :local:


****
Core
****

.. _tools-python:

Python
======

:xref:`Python` is an :xref:`open-source computer language <open-source>` with
various applications. The :xref:`source code <source-code>` for :term:`AAAAAA`
is written in :xref:`Python`, using assorted
:ref:`packages <python:tut-packages>`. See the :ref:`examples <examples>`
section for a showcase of :term:`AAAAAA` functionality

The :ref:`AAAAAA user guide <user-intro>` teaches :xref:`Python` as it
describes various features of :term:`AAAAAA`.
The :ref:`code concepts <concepts-code>` section describes some additional
specific :xref:`Python` considerations in :term:`AAAAAA` like syntax and
:xref:`directory <directory>` structure

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Python.org <Python>`, Official information
   :xref:`Corey Schafer tutorials <Corey-Schafer-vids>`, "Learn
   :xref:`Python` (recommended tutorial)"
   :doc:`python:tutorial/index`, Official tutorial
   :doc:`python:howto/functional`, ":ref:`Function <python:tut-functions>`
   techniques"
   :doc:`python:howto/index`, Specific use cases
   :doc:`python:faq/index`, Common issues
   :doc:`python:faq/programming`, Advanced technical information
   :doc:`The Python interpreter <tutorial/interpreter>`, "Mechanism that
   executes :xref:`source code <source-code>`"
   :ref:`Code concepts <concepts-code>`, ":term:`AAAAAA` usage
   (syntax, structure)"
   :ref:`AAAAAA user guide <user-intro>`, ":term:`AAAAAA` usage
   (:xref:`software <software>` walkthrough)"

.. _tools-anaconda:

Anaconda
========

:xref:`Anaconda` contains a collection of
:ref:`Python packages <python:tut-packages>` that are :xref:`free <money>` to
:wiki-pg:`download <Download>` and use. The base :xref:`Anaconda` collection
has way more :ref:`Python packages <python:tut-packages>` than :term:`AAAAAA`
require, so you can use :doc:`Miniconda<conda:user-guide/install/index>` to
access only the ones that you need

You can manage these :ref:`packages <conda:concept-conda-package>` using
:doc:`conda <conda:index>`, a configurator that automatically checks
dependencies and maintains compatibility between
:ref:`packages <conda:concept-conda-package>`.
:ref:`conda:concept-conda-package` can be downloaded from
different :ref:`conda channels <conda:channels-glossary>`, like the
:xref:`conda-forge`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`conda:index`, Official reference
   :doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :doc:`conda <conda:index>` commands"
   :ref:`Conda procedures <conda-procedures>`, :term:`AAAAAA` usage

The :ref:`developer environment setup <dev-env-intro>` describes how to
:doc:`create <conda:commands/create>` a new
:ref:`conda environment <conda:concept-conda-env>`, called :term:`a6`, which
you can also reproduce via the :ref:`import a6 procedure <conda-import-a6>`

.. glossary::

   a6
      A :ref:`conda environment <conda:concept-conda-env>` containing all
      the :ref:`packages <conda:concept-conda-package>` that :term:`AAAAAA`
      require

      .. _concepts-packages-table:

      .. csv-table:: :ref:`conda:concept-conda-package` required for
         :term:`AAAAAA`
         :header: Package, Function, Setup Phase, Channel
         :align: center

         :xref:`Python`, :xref:`source-code` creation, "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :doc:`conda <conda:index>`, "
         :ref:`Package <conda:concept-conda-package>` management", "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :pep:`8`, Check :ref:`code style <concepts-code-style>`, "
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :ref:`tools-sphinx` , "
         :ref:`Build documentation <sphinx-building-documentation>`", "
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :doc:`RTD Sphinx Theme <rtd-sphinx-theme:index>`, "
         :ref:`Documentation appearance <tools-read-the-docs>`", "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :xref:`Doc8 <Doc8>`, "Check
         :ref:`documentation style <concepts-documentation-style>`", "
         :ref:`Documenting <dev-env-documenting>`", :xref:`conda-forge`
         :ref:`tools-bibtex`, :ref:`Book citations <references-books>`, "
         :ref:`Documenting <dev-env-documenting>`", :xref:`conda-forge`
         :ref:`tools-sphinx-autobuild`, "
         :ref:`Auto-update documentation <sphinx-autobuilding>`", "
         :ref:`Documenting <dev-env-documenting>`", :xref:`conda-forge`
         :ref:`Jupyter Notebooks <tools-jupyter>`, Interactive analysis, "
         :ref:`dev-env-analyzing`","
         :ref:`conda <conda:channels-glossary>`"
         :doc:`Notebook Extensions <nb-extensions:index>`, "Enhance
         :ref:`Jupyter <tools-jupyter>`", :ref:`dev-env-analyzing`, "
         :xref:`conda-forge`"
         :doc:`NumPy <numpy:about>`, "Number processing", "
         :ref:`dev-env-analyzing`", :ref:`conda <conda:channels-glossary>`
         :doc:`Matplotlib <matplotlib:index>`, "Data plotting", "
         :ref:`dev-env-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :doc:`pandas <pandas:index>`, "Dataset management", "
         :ref:`dev-env-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :doc:`pip <python:installing/index>`, "
         :ref:`Configuring test code <conda-pip-AAAAAA>`", "
         :ref:`dev-env-testing`", :ref:`conda <conda:channels-glossary>`
         :ref:`pytest <tools-pytest>`, "
         :ref:`Code testing <pytest-procedures>`", ":ref:`dev-env-testing`", "
         :ref:`conda <conda:channels-glossary>`"

.. _tools-git:

Git
===

:xref:`Git <git-manual>` is used create and track changes to the
:xref:`AAAAAA-repo`. :xref:`Git <git-manual>` is a version control system that
allows the project to be updated with :xref:`commits <git-commit>`, which are
like snapshots in time that describe minor changes to the project throughout
its history. Each :xref:`commit <git-commit>` is identified by a :xref:`sha1`,
a unique identifier that can be accessed by
:ref:`viewing the project log <git-view-project-log>`

:xref:`Tags <git-tag>`, which provide a unique identifier for
:xref:`commits <git-commit>`, and :xref:`branches <git-branch>`, which enable
independent sequences of :xref:`commits <git-commit>`, are used to manage
:ref:`project versions <version-list>` on :xref:`GitHub`, a
:xref:`free <money>` service that hosts the :xref:`AAAAAA-repo`

There are several :xref:`command line<command-line>` text navigators that go
along with :xref:`Git <git-manual>`:

.. csv-table:: Text navigators
   :header: Tool, Usage
   :align: center

   :xref:`Vim <Vim-tutorial>`, ":ref:`Configuring <git-setup>` and
   :ref:`git-committing`"
   :xref:`less <less-pager>`, "
   :ref:`Viewing project history <git-view-project-log>`"

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`git-manual`, Quick practical reference
   :xref:`git-book`, In-depth conceptual explanations
   :xref:`git-commit-guidelines`, Contribution guidelines
   :doc:`Documentation webhooks <rtfd:webhooks>`, "Automatic
   :ref:`versioning <version-list>` integration"
   :xref:`Vim`, Official information
   :ref:`Git procedures <git-procedures>`, :term:`AAAAAA` usage

.. _tools-vs-code:

VS Code
=======

:xref:`VS-Code` is an
:wiki-pg:`integrated development environment (IDE)
<Integrated_development_environment>`
that is used to create :term:`AAAAAA`

The :xref:`AAAAAA-repo` comes with a collection of
:xref:`VS-Code-settings` that will automatically configure most of your
:wiki-pg:`software <Software>` workspace. If you completed the
:ref:`developer environment setup <dev-env-intro>`, then all the relevant
settings should already be
:wiki-pg:`installed <Installation_(computer_programs)>`! These settings will
help with things like :ref:`code style <concepts-code-style>` and
:ref:`test discovery <pytest-discover-tests>`

There is also the :xref:`VS Code Insider Edition <VS-Code-insiders>`,
which has all the latest features but may not be completely stable

.. csv-table:: Select :xref:`extensions <VS-Code-extensions>`
   :header: Extension, Purpose, Setup Phase
   :align: center

   :xref:`Bookmarks <VS-Code-bookmarks-ext>`, Mark/navigate content, "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`Python <VS-Code-Python-ext>`, Developing :ref:`tools-python`, "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`RST preview <RST-preview-ext>` [#]_ [#]_, "Edit
   :ref:`reST <tools-restructured-text>` ", "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`GitLens <GitLens>`, "Advanced :ref:`tools-git`
   functionality", :ref:`Documenting <dev-env-documenting>`
   :xref:`Python Test Explorer <Test-explorer-UI>`, "Using
   :doc:`pytest <pytest:index>`", :ref:`Testing <dev-env-testing>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Python integration <VS-Code-Python-tutorial>`, "Official tutorial for
   :ref:`tools-python` with :xref:`VS Code <VS-Code>`"
   :xref:`Command palette <command-palette>`, Quickly input user commands
   :xref:`Settings <VS-Code-settings>`, Environment configuration
   :xref:`Integrated terminal <VS-Code-terminal>`, "Run a
   :xref:`command line <command-line>` inside :xref:`VS Code <VS-Code>`"
   :xref:`VS-Code-unit-testing`, ":ref:`tools-pytest` integration"
   :xref:`Markdown`, For :ref:`planning version features <versioning-td3>`
   :ref:`Writing procedures <writing-procedures>`, :term:`AAAAAA` usage

.. rubric:: Footnotes

.. [#] Requires a :xref:`doc8-newline-issue`, included in the provided
   :xref:`VS-Code-settings`
.. [#] Offers live previewing, but is not as reliable as using a
   :xref:`browser <web-browser>` with :ref:`tools-sphinx-autobuild`. For
   example, fails to properly preview
   :ref:`intersphinx links <sphinx-intersphinx>`


*************
Documentation
*************

.. _tools-sphinx:

Sphinx
======

:doc:`Sphinx <sphinx:intro>` is the documentation engine that
:ref:`builds <sphinx-building-documentation>` the
the documentation :xref:`website <website>` for :term:`AAAAAA` and even for
:doc:`Python itself <py-dev-guide:documenting>`. Sphinx is built on
:ref:`tools-restructured-text` (``reST``), a particular style of
:wiki-pg:`markup language <Markup_language>`

:doc:`Sphinx <sphinx:intro>` has a
:ref:`table of contents <sphinx:toctree-directive>` feature, which provides a
linearly navigable structure that ensures access to all pages of documentation.
:term:`AAAAAA` are documented using the
:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which provides the
visual layout of this :xref:`website <website>`

:doc:`Sphinx extensions <sphinx:usage/extensions/index>` enable additional
functionality and several are used in :term:`AAAAAA`:

.. csv-table:: :doc:`Sphinx extensions <sphinx:usage/extensions/index>`
   in :term:`AAAAAA`
   :header: Extension, Purpose
   :align: center

   :ref:`Intersphinx <tools-intersphinx>`, "
   :ref:`Create links <sphinx-intersphinx>` to other
   :doc:`Sphinx <sphinx:intro>` projects"
   :ref:`xref <tools-xref>`, ":ref:`Create links <sphinx-xref>` to arbitrary
   :xref:`URLs <URL>`"
   :ref:`tools-extlinks`, ":ref:`Create links <sphinx-xref>` to common
   :xref:`URLs <URL>`"
   :ref:`tools-napoleon`, :ref:`Document code components <concepts-code-e4>`
   :ref:`tools-BibTeX`, :ref:`Cite books <sphinx-reference-book>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`Sphinx <sphinx:intro>`, Official documentation
   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :doc:`Sphinx <sphinx:intro>`"
   :xref:`Practical use seminar <Willing-Sphinx>`, "Practical
   :ref:`use examples <sphinx-procedures>`"
   :ref:`References extension configuration example <sublime-with-sphinx:use the external links extension>`, "
   :doc:`Extension <sphinx:usage/extensions/index>` installation and
   configuration"
   :doc:`conf.py <sphinx:usage/configuration>`, Configuration settings
   :ref:`tools-sphinx-autobuild`, "
   :ref:`Automatic documentation building <sphinx-autobuilding>`"
   :ref:`Sphinx procedures <sphinx-procedures>`, :term:`AAAAAA` usage

.. _tools-restructured-text:

reStructuredText
================

:xref:`reStructuredText <reST-documentation>` (``reST``) is a
:wiki-pg:`markup language <Markup_language>`
containing syntax to generate fancy components like ``this``, :guilabel:`this`,
or :menuselection:`t --> h --> i --> s`

The two most fundamental :doc:`reST <sphinx:usage/restructuredtext/basics>`
components are the :doc:`role <sphinx:usage/restructuredtext/roles>`, which
marks a piece of text (usually in-line), and the
:doc:`directive <sphinx:usage/restructuredtext/directives>`, which marks a
block of text

:wiki-pg:`Files <Computer_file>` that contain
:doc:`reST <sphinx:usage/restructuredtext/basics>` have an ``.rst``
:wiki-pg:`extension <Filename_extension>`, and :ref:`tools-sphinx` converts
them whenever :ref:`documentation is built <sphinx-building-documentation>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`sphinx:usage/restructuredtext/basics`, "
   :doc:`Sphinx <sphinx:intro>` tutorial on ``reST`` usage"
   :xref:`reStructuredText <reST-documentation>`, Official documentation
   :xref:`quick-reST`, Practical syntax
   :xref:`reST-cheatsheet`, Quick syntax reference
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   syntax"
   :doc:`sphinx:usage/restructuredtext/domains`, "Collections of
   :doc:`roles <sphinx:usage/restructuredtext/roles>` and
   :doc:`directives <sphinx:usage/restructuredtext/directives>`"
   :ref:`reST style <concepts-documentation-style>`, :term:`AAAAAA` usage


Many :ref:`tools-sphinx` documentation :xref:`website <website>` have an
:guilabel:`Edit on GitHub` (or similar) feature at
the top of each :xref:`webpage <webpage>`. This feature will :xref:`link <URL>`
to the :doc:`reST <sphinx:usage/restructuredtext/basics>` file that
:ref:`tools-sphinx` used to create the :xref:`webpage <webpage>`

.. tip::

   You can harvest the syntax for nearly any kind of
   :doc:`reST <sphinx:usage/restructuredtext/basics>` component from the
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, via the
   :guilabel:`Edit on GitHub` feature

.. _tools-read-the-docs:

Read the Docs
=============

:doc:`Read the Docs<rtfd:index>` is a :xref:`free <money>` online repository
that hosts :doc:`Sphinx <sphinx:intro>` projects, and even provides its own
:doc:`Sphinx Theme <rtd-sphinx-theme:index>`. :doc:`Read the Docs<rtfd:index>`
uses :doc:`webhooks <rtfd:webhooks>` to automatically detect any
:ref:`Git <tools-git>` updates, which trigger new
:ref:`documentation builds <sphinx-building-documentation>`.
:doc:`Read the Docs<rtfd:index>` supports multiple project documentation
:doc:`versions <rtfd:versions>`, too

:term:`AAAAAA` documentation uses the
:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which generates
the visual appearance of this :xref:`website <website>`!

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Quickstart tutorial <Yusuf-Sphinx-RTD>`, "Start a
   :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   project"
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   :ref:`tools-restructured-text` elements"
   :doc:`rtfd:webhooks`, Automatic project modification detection
   :doc:`rtfd:versions`, Automatic :ref:`version <version-list>` support
   :xref:`Writer-intro-to-Sphinx`, Introductory article for technical writers
   :ref:`Documentation versioning <versioning-releasing>`, :term:`AAAAAA` usage

.. _tools-sphinx-extensions:

Sphinx extensions
=================

.. contents::
   :local:

Included with Sphinx
--------------------

.. _tools-intersphinx:

Intersphinx
^^^^^^^^^^^

:doc:`Intersphinx <sphinx:usage/extensions/intersphinx>` helps manage
:ref:`links <references-links>` to other :ref:`tools-sphinx` projects, via the
:ref:`intersphinx procedures <sphinx-intersphinx>`

.. _tools-napoleon:

Napoleon
^^^^^^^^

:doc:`Napoleon <sphinx:usage/extensions/napoleon>` is a
:ref:`Sphinx extension <tools-sphinx>` that parses
:xref:`source code <source-code>` and creates
:ref:`documentation elements <concepts-code-e4>` from
:ref:`docstrings <python:tut-docstrings>` and :pep:`type annotations <484>`. It
uses the same
:ref:`directives <tools-restructured-text>` as
:doc:`autodoc <sphinx:usage/extensions/autodoc>`, but it
can accept :ref:`NumPy docstrings <numpy:format>`.
:doc:`Napoleon <sphinx:usage/extensions/napoleon>` and
:doc:`autodoc <sphinx:usage/extensions/autodoc>` both convert
:ref:`docstrings <python:tut-docstrings>` into
:ref:`reST <tools-restructured-text>`, like that used for
:ref:`info field lists <sphinx:info-field-lists>`

:ref:`Docstrings <python:tut-docstrings>` are annotated using the
:ref:`Python domain <sphinx:python-roles>`, which is also used to reference
:ref:`concepts-code-e4` elsewhere in documentation

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`Napoleon <sphinx:usage/extensions/napoleon>`, Official reference
   :ref:`Docstrings <python:tut-docstrings>`, ":ref:`python:comments` for
   special :xref:`source code <source-code>` components"
   :doc:`Autodoc <sphinx:usage/extensions/autodoc>`, "
   :doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
   :ref:`docstrings <python:tut-docstrings>`"
   :ref:`NumPy docstrings <numpy:format>`, "
   :ref:`Docstrings <python:tut-docstrings>` style"
   :pep:`Type annotations <484>`, "Specify
   :doc:`types <python:library/stdtypes>`"
   :ref:`Python domain <sphinx:python-roles>`, "
   :doc:`Roles <sphinx:usage/restructuredtext/roles>` and
   :doc:`directives <sphinx:usage/restructuredtext/directives>`"
   :xref:`Type checking <realpython-type-checking>`, "
   :xref:`RealPython <RealPython>` guide"
   :doc:`Sample automodule <demo/api>`, "
   :doc:`Autodoc <sphinx:usage/extensions/autodoc>` demo with
   :doc:`RTD Sphinx theme <rtd-sphinx-theme:index>`"
   :doc:`Example NumPy Strings <napoleon:example_numpy>`, "Example
   :ref:`docstrings <python:tut-docstrings>`"
   :ref:`sphinx:info-field-lists`, "Resultant
   :ref:`reST <tools-restructured-text>` syntax"
   :ref:`Napoleon example <concepts-code-e4>`, :term:`AAAAAA` usage

.. _tools-extlinks:

extlinks
^^^^^^^^

The :doc:`extlinks extension <sphinx:usage/extensions/extlinks>` functions like
:ref:`tools-xref`, but is exceptionally efficient
:ref:`for common websites <sphinx-reference-urls>`. Usage is
described at :ref:`extlinks procedures <sphinx-extlinks>`

Not included with Sphinx
------------------------

.. _tools-xref:

xref
^^^^

:xref:`Michael Jones' xref extension <xref-ext>` helps manage
:ref:`links <references-links>` to arbitrary :xref:`URLs <URL>` that can not be
accessed via :ref:`intersphinx <tools-intersphinx>`. A simple
:ref:`role <tools-restructured-text>` is used to insert
:ref:`links <references-links>`, and usage is described at
:ref:`xref procedures <sphinx-xref>`

.. _tools-bibtex:

BibTeX
^^^^^^

:xref:`bibtex` is a special type of :xref:`citation <citation>` syntax that
:term:`AAAAAA` uses for :ref:`books <references-books>`. The
:doc:`BibTeX Sphinx extension <bibtex:index>` converts
:ref:`refs.bib <concepts-documentation-structure>` into formatted
:ref:`book citations <references-books>`

If know the :xref:`ISBN` for a particular :ref:`book <references-books>`, you
can usually get the :xref:`bibtex` from :xref:`ottobib`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`book`, Information source
   :xref:`bibtex`, :xref:`Citation <citation>` format
   :doc:`BibTeX Sphinx extension <bibtex:index>`, Converts :xref:`bibtex`
   :xref:`ottobib`, :xref:`bibtex` database for :ref:`books <references-books>`
   :xref:`ISBN`, Unique identifier for :ref:`books <references-books>`
   :xref:`bibtex-syntax`, Syntax specifications
   :xref:`cite-multiple-authors`, Use of ``et. al``
   :ref:`BibTeX procedures <sphinx-reference-book>`, :term:`AAAAAA` usage

.. _tools-sphinx-autobuild:

sphinx-autobuild
================

:xref:`sphinx-autobuild` is a :ref:`package <tools-anaconda>` that
:ref:`automates <sphinx-autobuilding>` the iterative process of
:ref:`manual builds <sphinx-building-manually>`, which
is helpful when :ref:`proofreading documentation <writing-proofread>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`sphinx-autobuild`, User manual
   :ref:`tools-sphinx`, Tool to make documentation
   :ref:`Building manually <sphinx-building-manually>`, "Manual
   :term:`AAAAAA` usage"
   :ref:`Building automatically <sphinx-autobuilding>`, "Automated
   :term:`AAAAAA` usage"


********
Analysis
********

.. _tools-jupyter:

Jupyter
=======

:xref:`Jupyter Notebooks <Jupyter>` enable an interactive style of
algorithm development, and can quickly render :xref:`LaTeX`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Corey Schafer tutorial <Schafer-Jupyter>`, "Recommended
   :xref:`YouTube` tutorial"
   :xref:`Markdown`, "Syntax for making :xref:`links <URL>`,
   :xref:`tables <tables-generator>`, etc."
   :xref:`tables-generator`, Syntax generator

The interactive style of :xref:`Jupyter Notebooks <Jupyter>` make it easy to
analyze data with numerical :ref:`conda packages <conda:concept-conda-package>`

.. csv-table:: Numerical analysis :ref:`packages <conda:concept-conda-package>`
   :header: Package, Official tutorial, YouTube tutorial
   :align: center

   :doc:`NumPy <numpy:about>`, "
   :doc:`Quickstart <numpy:user/quickstart>`", "
   :xref:`NumPy <codebasics-numpy>`"
   :doc:`Matplotlib <matplotlib:index>`,"
   :doc:`matplotlib:tutorials/index`", "
   :xref:`Matplotlib <codebasics-matplotlib>`"
   :doc:`pandas <pandas:index>`, "
   :doc:`10 min tutorial <pandas:getting_started/10min>`", "
   :xref:`pandas <codebasics-pandas>`"

The :doc:`nb-extensions:index` provide additional functionality

.. csv-table:: Select :doc:`extensions <nb-extensions:index>`
   :header: Extension, Function
   :align: center

   :doc:`nb-extensions:nbextensions/collapsible_headings/readme`, "Section
   management"
   :doc:`nb-extensions:nbextensions/toc2/README`, "Automatic section
   linking"
   :doc:`nb-extensions:nbextensions/varInspector/README`, "Data value
   inspection"
   :xref:`live-md-preview`, "Quick previewing for :xref:`LaTeX` and
   :xref:`tables <tables-generator>`"

.. tip::

   This :xref:`AAAAAA-nbs` can render any :xref:`Jupyter Notebook<Jupyter>`
   from the :xref:`AAAAAA-repo` inside of a :xref:`web browser <web-browser>`,
   even if you don't have :xref:`Jupyter <Jupyter>`


*******
Testing
*******

.. _tools-pytest:

pytest
======

:term:`AAAAAA` uses :doc:`pytest <pytest:index>`, a
:ref:`conda package<tools-anaconda>`, to verify that
:ref:`source code <tools-python>` is functioning as expected

:ref:`tools-vs-code` natively integrates with :doc:`pytest <pytest:index>`,
and additional functionality is provided by the
:ref:`VS Code Python Test Explorer extension<tools-vs-code>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`pytest <pytest:index>`, Official documentation
   :xref:`codebasics-pytest`, Recommended :xref:`YouTube` tutorial
   :doc:`pytest tutorials <pytest:contents>`, Official tutorials
   :ref:`pytest procedures <pytest-procedures>`, :term:`AAAAAA` usage


************
Distributing
************

PyPI
====