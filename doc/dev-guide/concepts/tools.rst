.. 0.3.0

.. _concepts-tools:


#####
Tools
#####

.. contents::
   :local:


**************
The Holy Grail
**************

.. _tools-google:

Google
======

This is by far the most important :ref:`tool <concepts-tools>` that
:github:`alnoki` has in the :term:`AAAAAA` arsenal

Nearly everything that :github:`alnoki` has done to create :term:`AAAAAA` has
started with :wiki-pg:`searches <Web_search_engine>` on :xref:`Google`. Because
so many components of :term:`AAAAAA` are
:wiki-pg:`open-source software <Open-source_software>`, the primary means of
accessing them is the :wiki-pg:`Internet`, which :xref:`Google` has done a
remarkable job of indexing. With the exception of a few
:ref:`books <references-books>` (which are likely on the :wiki-pg:`Internet`,
too), all the information you see here is
:wiki-pg:`free <Money>`, and you can find it with :xref:`Google`

It is not an exaggeration to say that you can legitimately figure out all of
this for yourself with a :wiki-pg:`laptop <Laptop>`, access to :xref:`Google`,
and enough curiosity. That is of course, how :github:`alnoki` did it, after all

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
specific :xref:`Python` considerations in :term:`AAAAAA` like
:wiki-pg:`syntax <Syntax_(programming_languages)>` and
:xref:`directory <directory>` structure

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Python.org <Python>`, Official information
   :yt-pl:`Corey Schafer tutorials <-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU>`, "Learn
   :xref:`Python` (recommended tutorial)"
   :doc:`python:tutorial/index`, Official tutorial
   :doc:`python:howto/functional`, ":ref:`Function <python:tut-functions>`
   techniques"
   :doc:`python:howto/index`, Specific use cases
   :doc:`python:faq/index`, Common issues
   :doc:`python:faq/programming`, Advanced technical information
   :doc:`The Python interpreter <tutorial/interpreter>`, "Mechanism that
   executes :xref:`source code <source-code>`"
   :ref:`Code structure <concepts-code-tree>`, :term:`AAAAAA` components
   :ref:`Code concepts <concepts-code>`, ":term:`AAAAAA` usage
   (:wiki-pg:`syntax <Syntax_(programming_languages)>`, structure of
   :wiki-pg:`files <Computer_file>`)"
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
:doc:`conda <conda:index>`, a :wiki-pg:`command line <Command_line>` utility
that automatically checks dependencies and maintains compatibility between
:ref:`packages <conda:concept-conda-package>`.
:ref:`conda:concept-conda-package` can be downloaded from
different :ref:`conda channels <conda:channels-glossary>`, like the
:xref:`conda-forge`

.. csv-table:: :doc:`conda:index` references
   :header: Reference, Topic
   :align: center

   :doc:`conda:index`, Official reference
   :doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :wiki-pg:`commands <Command_line>` for :doc:`conda <conda:index>`"
   :ref:`Conda procedures <conda-procedures>`, :term:`AAAAAA` usage
   :doc:`Miniconda <conda:user-guide/install/download>`, ":wiki-pg:`URL <URL>`
   for :wiki-pg:`download <Download>`"

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
         :pep:`8`, ":wiki-pg:`Linter <Lint_(software)>` for
         :ref:`code style <concepts-code-style>`","
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :ref:`tools-sphinx` , "
         :ref:`Build documentation <sphinx-building-doc>`", "
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :doc:`RTD Sphinx Theme <rtd-sphinx-theme:index>`, "
         :ref:`Documentation appearance <tools-read-the-docs>`", "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :xref:`Doc8 <Doc8>`, "Check
         :ref:`documentation style <concepts-doc-style>`", "
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

:xref:`Git <git-manual>` is used manage changes to
:wiki-pg:`files <Computer_file>` in the
:github:`AAAAAA repository <alnoki/AAAAAA>`. :xref:`Git <git-manual>` is a
:wiki-pg:`version control <Version_control>` system that allows :term:`AAAAAA`
to be updated with :xref:`commits <git-commit>`, which are like snapshots in
:wiki-pg:`time <Time>` that describe minor changes to :term:`AAAAAA`. Each
:xref:`commit <git-commit>` is identified by a :xref:`sha1`, a unique
identifier that can be accessed by
:ref:`viewing the project log <git-view-project-log>`

:xref:`Tags <git-tag>`, which provide a unique identifier for
:xref:`commits <git-commit>`, and :xref:`branches <git-branch>`, which enable
independent sequences of :xref:`commits <git-commit>`, are used to manage
:ref:`project versions <version-list>` on :xref:`GitHub`, a
:xref:`free <money>` service that :wiki-pg:`hosts <Host_(network)>` the
:github:`AAAAAA repository <alnoki/AAAAAA>` for :wiki-pg:`free <Money>`

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
   :ref:`Git configuration <configs-Git>`, "
   :ref:`Configuration <concepts-configs>` for :term:`AAAAAA`"
   :ref:`Git procedures <git-procedures>`, :term:`AAAAAA` usage

.. _tools-vs-code:

VS Code
=======

:xref:`VS-Code` is an
:wiki-pg:`integrated development environment (IDE)
<Integrated_development_environment>`
that is used to create :term:`AAAAAA`

The :github:`AAAAAA repository <alnoki/AAAAAA>` comes with a collection of
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
   :vs-code-ext:`Python <ms-python.python>`, Using :ref:`tools-python`, "
   :ref:`Documenting <dev-env-documenting>`"
   :vs-code-ext:`reStructuredText <lextudio.restructuredtext>` [#]_ [#]_, "
   :wiki-pg:`Linter <Lint_(software)>` for
   :ref:`reST <tools-restructured-text>` ", "
   :ref:`Documenting <dev-env-documenting>`"
   :vs-code-ext:`GitLens <eamodio.gitlens>`, "Advanced :ref:`tools-git`
   functionality", :ref:`Documenting <dev-env-documenting>`
   ":vs-code-ext:`Python Test Explorer
   <LittleFoxTeam.vscode-python-test-adapter>`", "Using
   :ref:`pytest <tools-pytest>`", :ref:`Testing <dev-env-testing>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :vs-code-doc:`Python integration <languages/python>`, "Official tutorial
   for :ref:`tools-python` with :xref:`VS Code <VS-Code>`"
   :xref:`Command palette <command-palette>`, "Quickly input
   :wiki-pg:`commands <Command_line>`"
   :xref:`Settings <VS-Code-settings>`, "
   :ref:`Configuration options <configs-settings-json>`"
   :xref:`Integrated terminal <VS-Code-terminal>`, "Run a
   :xref:`command line <command-line>` inside :xref:`VS Code <VS-Code>`"
   :vs-code-doc:`VS Code unit testing <python/unit-testing>`,"
   :ref:`tools-pytest` integration"
   :xref:`Markdown`, For :ref:`planning version features <versioning-td3>`
   :ref:`Writing procedures <writing-procedures>`, :term:`AAAAAA` usage

.. rubric:: Footnotes

.. [#] Requires a :xref:`doc8-newline-issue`, included in the provided
   :ref:`VS Code settings <configs-vs-code>`
.. [#] Offers :wiki-pg:`rendering <Rendering_(computer_graphics)>` in
   :wiki-pg:`real-time <Time>`, but is not as reliable as using a
   :xref:`browser <web-browser>` with :ref:`tools-sphinx-autobuild`. For
   example, fails for :ref:`intersphinx links <sphinx-intersphinx>`


*************
Documentation
*************

.. _tools-sphinx:

Sphinx
======

:doc:`Sphinx <sphinx:intro>` is the
:wiki-pg:`documentation <Software_documentation>` engine that
:ref:`builds <sphinx-building-doc>` the :xref:`website <website>` for
:term:`AAAAAA` and even for :doc:`Python itself <py-dev-guide:documenting>`.
Sphinx uses :ref:`tools-restructured-text` (``reST``), a particular style of
:wiki-pg:`markup language <Markup_language>`, which it converts to
:wiki-pg:`HTML` when :ref:`building a website <sphinx-building-doc>`

:doc:`Sphinx <sphinx:intro>` has a
:ref:`table of contents <sphinx:toctree-directive>` feature, which provides a
linearly navigable structure that ensures access to all
:wiki-pg:`pages <Webpage>` of
:wiki-pg:`Documentation <Software_documentation>`.
:term:`AAAAAA` are :wiki-pg:`documented <Software_documentation>` using the
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

   :doc:`Sphinx <sphinx:intro>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :doc:`Sphinx <sphinx:intro>`"
   :yt-vid:`Practical use seminar <0ROZRNZkPS8>`, "Practical
   :ref:`use examples <sphinx-procedures>`"
   ":ref:`References extension configuration example
   <sublime-with-sphinx:use the external links extension>`", "Similar usage and
   :ref:`configuration <configs-conf-py>`"
   :doc:`conf.py <sphinx:usage/configuration>`, "
   :ref:`Configurations <configs-conf-py>`"
   :ref:`tools-sphinx-autobuild`, "
   :ref:`Automatic documentation building <sphinx-autobuilding>`"
   :ref:`Sphinx configuration <configs-sphinx>`, "
   :ref:`Configuration <concepts-configs>` for :term:`AAAAAA`"
   :ref:`Documentation structure <concepts-doc-tree>`, ":term:`AAAAAA`
   components"
   :ref:`Sphinx procedures <sphinx-procedures>`, :term:`AAAAAA` usage

.. _tools-restructured-text:

reStructuredText
================

:xref:`reStructuredText <reST-documentation>` (``reST``) is a
:wiki-pg:`markup language <Markup_language>`
containing :wiki-pg:`syntax <Syntax_(programming_languages)>` to generate fancy
components like ``this``, :guilabel:`this`, or
:menuselection:`t --> h --> i --> s`

The two most fundamental :doc:`reST <sphinx:usage/restructuredtext/basics>`
components are the :doc:`role <sphinx:usage/restructuredtext/roles>`, which
marks a piece of text (usually in-line), and the
:doc:`directive <sphinx:usage/restructuredtext/directives>`, which marks a
block of text

:wiki-pg:`Files <Computer_file>` that contain
:doc:`reST <sphinx:usage/restructuredtext/basics>` have an ``.rst``
:wiki-pg:`extension <Filename_extension>`, and :ref:`tools-sphinx` converts
them to :wiki-pg:`HTML` whenever
:ref:`documentation is built <sphinx-building-doc>`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :doc:`sphinx:usage/restructuredtext/basics`, "
   :doc:`Sphinx <sphinx:intro>` tutorial on ``reST`` usage"
   :xref:`reStructuredText <reST-documentation>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :xref:`quick-reST`, "Practical
   :wiki-pg:`syntax <Syntax_(programming_languages)>`"
   :xref:`reST-cheatsheet`, "Quick
   :wiki-pg:`syntax <Syntax_(programming_languages)>` reference"
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   :wiki-pg:`syntax <Syntax_(programming_languages)>`"
   :doc:`sphinx:usage/restructuredtext/domains`, "Collections of
   :doc:`roles <sphinx:usage/restructuredtext/roles>` and
   :doc:`directives <sphinx:usage/restructuredtext/directives>`"
   :ref:`reST style <concepts-doc-style>`, :term:`AAAAAA` usage


Many :ref:`tools-sphinx`-style :xref:`websites <website>` for
:wiki-pg:`documentation <Software_documentation>` have an
:guilabel:`Edit on GitHub` (or similar) feature at
the top/bottom of each :xref:`webpage <webpage>`. This feature will
:xref:`link <URL>` to the
:doc:`reST file <sphinx:usage/restructuredtext/basics>`
that :ref:`tools-sphinx` used to create the :xref:`webpage <webpage>`

.. tip::

   You can harvest the :wiki-pg:`syntax <Syntax_(programming_languages)>` for
   nearly any kind of :doc:`reST <sphinx:usage/restructuredtext/basics>`
   component from the
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, via the
   :guilabel:`Edit on GitHub` feature

   After :wiki-pg:`clicking <Point_and_click>` :guilabel:`Edit on GitHub`, look
   for a :guilabel:`Raw` button, which should show you the
   :doc:`reST <sphinx:usage/restructuredtext/basics>`

.. _tools-read-the-docs:

Read the Docs
=============

:doc:`Read the Docs<rtfd:index>` is a :xref:`free <money>` provider of
:wiki-pg:`hosting services <Host_(network)>` for
:doc:`Sphinx <sphinx:intro>` projects, and even provides its own
:doc:`Sphinx Theme <rtd-sphinx-theme:index>`. :doc:`Read the Docs<rtfd:index>`
uses :doc:`webhooks <rtfd:webhooks>` to automatically detect any
:ref:`Git <tools-git>` updates, which trigger new
:ref:`documentation builds <sphinx-building-doc>`.
:doc:`Read the Docs<rtfd:index>` also supports multiple
:doc:`versions <rtfd:versions>` of
:wiki-pg:`documentation <Software_documentation>`

:wiki-pg:`Documentation <Software_documentation>` for :term:`AAAAAA` uses the
:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which generates
the :wiki-pg:`visual appearance <Rendering_(computer_graphics)>` of this
:xref:`website <website>`. The :doc:`theme <rtd-sphinx-theme:index>`
even :wiki-pg:`renders <Rendering_(computer_graphics)>` on the
:wiki-pg:`web browser <Web_browser>` for
:wiki-pg:`mobile devices <Mobile_device>`!

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :yt-vid:`Quickstart tutorial <oJsUvBQyHBs>`, "Start a
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
:ref:`concepts-code-e4` elsewhere in
:wiki-pg:`documentation <Software_documentation>`

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
   :ref:`reST syntax <tools-restructured-text>`"
   :ref:`Napoleon example <concepts-code-e4>`, :term:`AAAAAA` usage

.. _tools-extlinks:

extlinks
^^^^^^^^

The :doc:`extlinks extension <sphinx:usage/extensions/extlinks>` functions like
:ref:`tools-xref`, but is exceptionally efficient
:ref:`for common websites <sphinx-reference-urls>`. Usage is
described at :ref:`extlinks procedures <sphinx-extlinks>`

.. _tools-sphinx-exts-extra:

Not included with Sphinx
------------------------

.. _tools-xref:

xref
^^^^

:github:`Michael Jones' xref extension <michaeljones/sphinx-xref>` helps manage
:ref:`links <references-links>` to arbitrary :xref:`URLs <URL>` that can not be
accessed via :ref:`intersphinx <tools-intersphinx>`. A simple
:ref:`role <tools-restructured-text>` is used to insert
:ref:`links <references-links>`, and usage is described at
:ref:`xref procedures <sphinx-xref>`

.. _tools-bibtex:

BibTeX
^^^^^^

:xref:`bibtex` is a special type of
:wiki-pg:`syntax <Syntax_(programming_languages)>` that :term:`AAAAAA` use to
make :wiki-pg:`citations <Citation>` for :ref:`books <references-books>`. The
:doc:`BibTeX Sphinx extension <bibtex:index>` converts
:ref:`refs.bib <concepts-doc-tree>` into formatted
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
   :xref:`bibtex-syntax`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>`
   specifications"
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

   :xref:`sphinx-autobuild`, :wiki-pg:`User <User_(computing)>` manual
   :ref:`tools-sphinx`, ":ref:`Tool <concepts-tools>` to make
   :wiki-pg:`documentation <Software_documentation>`"
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

:xref:`Jupyter Notebooks <Jupyter>` enable an interactive
:wiki-pg:`development <Software_development>` style for creating
:wiki-pg:`algorithms <Algorithms>`, and for
quickly :wiki-pg:`rendering <Rendering_(computer_graphics)>` equations in
:xref:`LaTeX`

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`Corey Schafer tutorial <Schafer-Jupyter>`, "Recommended
   :xref:`YouTube` tutorial"
   :xref:`Markdown`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>` for
   making :wiki-pg:`links <URL>`, :xref:`tables <tables-generator>`, etc."
   :xref:`tables-generator`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` generator"
   :ref:`Notebook structure <concepts-jupyter-nbs-tree>`, "
   :term:`AAAAAA` components"

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

   This :xref:`AAAAAA-nbs` can
   :wiki-pg:`render <Rendering_(computer_graphics)>` any
   :xref:`Jupyter Notebook<Jupyter>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>` inside of a
   :xref:`web browser <web-browser>`, even if you don't have
   :xref:`Jupyter <Jupyter>`


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

   :doc:`pytest <pytest:index>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :xref:`codebasics-pytest`, Recommended :xref:`YouTube` tutorial
   :doc:`pytest tutorials <pytest:contents>`, Official tutorials
   :ref:`Code structure <concepts-code-tree>`, :term:`AAAAAA` components
   :ref:`testing <testing-intro>`, :term:`AAAAAA` walkthrough
   :ref:`pytest procedures <pytest-procedures>`, :term:`AAAAAA` usage


************
Distributing
************

.. _tools-pypi:

PyPI
====

*Coming soon*
