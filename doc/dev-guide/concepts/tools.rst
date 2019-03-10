.. 0.3.0

.. _concepts-tools:


#####
Tools
#####

.. contents::
   :local:
   :depth: 2


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

:xref:`Python` is an
:wiki-pg:`open-source computer language <Open-source_software>` with various
applications. The :xref:`source code <source-code>` for :term:`AAAAAA` is
written in :xref:`Python`, using assorted
:ref:`packages <python:tut-packages>`. See the :ref:`examples <examples>`
section for a showcase of :term:`AAAAAA` functionality

The :ref:`AAAAAA user guide <user-intro>` teaches :xref:`Python` as it
describes various features of :term:`AAAAAA`.
The :ref:`code concepts <concepts-code>` section describes some additional
specific :xref:`Python` considerations in :term:`AAAAAA` like
:wiki-pg:`syntax <Syntax_(programming_languages)>` and
:xref:`directory <directory>` structure

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`Code concepts <concepts-code>`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>`, structure of
   :wiki-pg:`files <Computer_file>`"
   :ref:`User guide <user-intro>`, Walkthrough

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`Conda procedures <procedures-conda>`, Usage
   :ref:`Conda configuration <configs-conda>`, Options

.. csv-table:: :doc:`conda:index` references
   :align: center
   :header: Reference, Topic

   :doc:`conda:index`, Official reference
   :doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :wiki-pg:`commands <Command_line>` for :doc:`conda <conda:index>`"
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
         :align: center
         :header: Package, Function, Setup Phase, Channel

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
         :conda-forge:`Doc8 reST linter <doc8>`, "Check
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
         :ref:`Code testing <procedures-pytest>`", ":ref:`dev-env-testing`", "
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
:ref:`project versions <indices-versions>` on :github:`GitHub <>`, a
:xref:`free <money>` service that :wiki-pg:`hosts <Host_(network)>` the
:github:`AAAAAA repository <alnoki/AAAAAA>` for :wiki-pg:`free <Money>`

There are several :xref:`command line<command-line>` text manipulators that go
along with :xref:`Git <git-manual>`

.. csv-table:: Text manipulators
   :align: center
   :header: Tool, Usage

   :xref:`Vim <Vim-tutorial>`, ":ref:`Configuring <git-setup>` and
   :ref:`git-committing`"
   :xref:`less <less-pager>`, "
   :ref:`Viewing project history <git-view-project-log>`"

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`Git configuration <configs-Git>`, Options
   :ref:`Git procedures <procedures-git>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`git-manual`, Quick practical reference
   :xref:`git-book`, In-depth conceptual explanations
   :xref:`git-commit-guidelines`, Contribution guidelines
   :doc:`Documentation webhooks <rtfd:webhooks>`, "Automatic
   :ref:`version <indices-versions>` support"
   :xref:`Vim`, Official information

.. _tools-vs-code:

VS Code
=======

:xref:`VS-Code` is an
:wiki-pg:`integrated development environment (IDE)
<Integrated_development_environment>`
that is used to create :term:`AAAAAA`, with additional functionality provided
by :vs-code-doc:`extensions <editor/extension-gallery>`

The :github:`AAAAAA repository <alnoki/AAAAAA>` comes with a collection of
:vs-code-doc:`VS Code settings <getstarted/settings>` that will automatically
:ref:`configure <concepts-configs>` most of your
:wiki-pg:`software <Software>` workspace. If you completed the
:ref:`developer environment setup <dev-env-intro>`, then all the relevant
:ref:`configurations <configs-vs-code>` should already be
:wiki-pg:`installed <Installation_(computer_programs)>`! These
:ref:`configurations <configs-vs-code>` will
help with things like :ref:`code style <concepts-code-style>` and
:ref:`test discovery <pytest-discover-tests>`. Additionally, this will
:ref:`configure <concepts-configs>` your
:vs-code-doc:`VS Code user interface <getstarted/userinterface>` with some
select :wiki-pg:`X11 colors <Web_colors>`

There is also the :xref:`VS Code Insider Edition <VS-Code-insiders>`,
which has all the latest features but may not be completely stable

.. csv-table:: Select :xref:`extensions <VS-Code-extensions>`
   :align: center
   :header: Extension, Purpose, Setup Phase

   :vs-code-ext:`Bookmarks <alefragnani.Bookmarks>`, Mark/navigate content, "
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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`VS Code configuration <configs-vs-code>`, Options
   :ref:`VS Code procedures <procedures-vs-code>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :vs-code-doc:`User interface <getstarted/userinterface>`, "Official
   introduction"
   :vs-code-doc:`Python integration <languages/python>`, "Official tutorial
   for :ref:`tools-python` with :xref:`VS Code <VS-Code>`"
   ":vs-code-doc:`Command palette
   <getstarted/userinterface#_command-palette>`", "Quickly input
   :wiki-pg:`commands <Command_line>`"
   :vs-code-doc:`Settings <getstarted/settings>`, "Official
   :ref:`configuration options <configs-settings-json>`"
   :vs-code-doc:`Extensions <editor/extension-gallery>`, "Additional
   functionality"
   :vs-code-doc:`Integrated terminal <editor/integrated-terminal>`, "Use a
   :xref:`command line <command-line>` inside :xref:`VS Code <VS-Code>`"
   :vs-code-doc:`VS Code unit testing <python/unit-testing>`,"
   :ref:`tools-pytest` integration"
   :github-help:`Markdown <basic-writing-and-formatting-syntax>`, "
   :ref:`Planning version features <versioning-td3>`"

.. csv-table:: Modifying :wiki-pg:`colors <Web_colors>`
   :align: center
   :header: Reference, Topic

   :vs-code-doc:`Themes <getstarted/themes>`, General usage
   :vs-code-api:`Color theme extension guide <extension-guides/color-theme>`, "
   Enhanced functionality"
   :vs-code-api:`Token color customizations <references/theme-color>`, "
   Official reference"
   :github:`Token color customizations <Microsoft/vscode/pull/29393>`, "
   Advanced usage"

.. rubric:: Footnotes

.. [#] Requires a
   :github:`doc8 newline issue fix
   <vscode-restructuredtext/vscode-restructuredtext/issues/84>`, included in
   the provided :ref:`VS Code settings <configs-vs-code>`
.. [#] Offers :wiki-pg:`rendering <Rendering_(computer_graphics)>` in
   :wiki-pg:`real-time <Time>`, but is not as reliable as using a
   :xref:`browser <web-browser>` with :ref:`tools-sphinx-autobuild`. For
   example, fails for :ref:`intersphinx links <sphinx-intersphinx>`

.. _tools-vim:

Vim
===



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
:ref:`table of contents <sphinx:toctree-directive>` feature
(:rst:dir:`toctree`), which provides a linearly navigable structure that
ensures access to all :wiki-pg:`pages <Webpage>` of
:wiki-pg:`Documentation <Software_documentation>`.
:term:`AAAAAA` are :wiki-pg:`documented <Software_documentation>` using the
:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which provides the
visual layout of this :xref:`website <website>`

:doc:`Sphinx extensions <sphinx:usage/extensions/index>` enable additional
functionality and :ref:`several are used <tools-sphinx-extensions>` in
:term:`AAAAAA`

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`Sphinx configuration <configs-sphinx>`, Options
   :ref:`tools-restructured-text`, :wiki-pg:`Markup language <Markup_language>`
   :ref:`Documentation structure <concepts-doc-tree>`, Specific components
   :ref:`Sphinx procedures <procedures-sphinx>`, Usage
   :ref:`Sphinx extensions <tools-sphinx-extensions>`, Extended functionality
   :ref:`tools-sphinx-autobuild`, Automation
   :ref:`Distributing documentation <dist-doc>`, Walkthrough

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :doc:`Sphinx <sphinx:intro>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :doc:`conf.py <sphinx:usage/configuration>`, "Official
   :ref:`configuration options <configs-conf-py>`"
   :doc:`sphinx:usage/builders/index`, "Create different styles of
   :wiki-pg:`documentation <Software_documentation>`"
   :doc:`Python Developer's Guide <py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :doc:`Sphinx <sphinx:intro>`"
   :yt-vid:`Practical use seminar <0ROZRNZkPS8>`, "Practical
   :ref:`use examples <procedures-sphinx>`"
   ":ref:`References extension configuration example
   <sublime-with-sphinx:use the external links extension>`", "Similar usage and
   :ref:`configuration <configs-conf-py>`"

.. _tools-restructured-text:

reStructuredText
================

:docutils:`reStructuredText <rst.html>` (``reST``) is a
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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`reST style <concepts-doc-style>`, Style
   :ref:`tools-sphinx`, ":wiki-pg:`Documentation <Software_documentation>`
   engine"

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :doc:`sphinx:usage/restructuredtext/basics`, "
   :doc:`Sphinx <sphinx:intro>` tutorial on ``reST`` usage"
   :docutils:`reStructuredText <rst.html>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :docutils:`docs/user/rst/quickref.html`, "Practical
   :wiki-pg:`syntax <Syntax_(programming_languages)>`"
   ":github:`reST cheatsheet
   <ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`", "Quick
   :wiki-pg:`syntax <Syntax_(programming_languages)>` reference"
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   :wiki-pg:`syntax <Syntax_(programming_languages)>`"
   :doc:`sphinx:usage/restructuredtext/domains`, "Collections of
   :doc:`roles <sphinx:usage/restructuredtext/roles>` and
   :doc:`directives <sphinx:usage/restructuredtext/directives>`"

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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`RTD Configurations <configs-read-the-docs>`, Options
   :ref:`Distributing documentation <dist-doc>`, Walkthrough
   :ref:`Documentation versioning <versioning-releasing>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :yt-vid:`Quickstart tutorial <oJsUvBQyHBs>`, "Start a
   :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   project"
   :doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   :ref:`tools-restructured-text` elements"
   :doc:`rtfd:webhooks`, Automatic project modification detection
   :doc:`rtfd:versions`, Automatic :ref:`version <indices-versions>` support
   :xref:`Writer-intro-to-Sphinx`, Introductory article for technical writers

.. _tools-sphinx-extensions:

Sphinx extensions
=================

:term:`AAAAAA` uses some
:doc:`built-in Sphinx extensions <sphinx:usage/extensions/index>` and some that
are not :doc:`built-in <sphinx:usage/extensions/index>`

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Purpose

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`tools-sphinx`, Conceptual explanation

.. csv-table:: :doc:`Sphinx extensions <sphinx:usage/extensions/index>`
   in :term:`AAAAAA`
   :align: center
   :header: Extension, Purpose

   :ref:`Intersphinx <tools-intersphinx>`, "
   :ref:`Create links <sphinx-intersphinx>` to other
   :doc:`Sphinx <sphinx:intro>` projects"
   :ref:`tools-napoleon`, :ref:`Document code components <concepts-code-e4>`
   :ref:`tools-extlinks`, ":ref:`Create links <sphinx-xref>` to common
   :wiki-pg:`URLs <URL>`"
   :ref:`xref <tools-xref>`, ":ref:`Create links <sphinx-xref>` to arbitrary
   :wiki-pg:`URLs <URL>`"
   :ref:`tools-BibTeX`, :ref:`Cite books <sphinx-reference-book>`

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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Documentation syntax <concepts-doc-style>`, Usage
   :ref:`Napoleon example <concepts-code-e4>`, Usage
   :ref:`Napoleon procedures <procedures-napoleon>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

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
   :real-py:`RealPython <>` guide"
   :doc:`Sample automodule <demo/api>`, "
   :doc:`Autodoc <sphinx:usage/extensions/autodoc>` demo with
   :doc:`RTD Sphinx theme <rtd-sphinx-theme:index>`"
   :doc:`Example NumPy Strings <napoleon:example_numpy>`, "Example
   :ref:`docstrings <python:tut-docstrings>`"
   :ref:`sphinx:info-field-lists`, "Resultant
   :ref:`reST syntax <tools-restructured-text>`"

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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`BibTeX procedures <sphinx-reference-book>`, Usage
   :ref:`refs.bib <concepts-doc-tree>`, "
   :wiki-pg:`File structure <Computer_file>`"
   :ref:`references-books`, :wiki-pg:`Citation` catalogue

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`book`, Information source
   :xref:`bibtex`, :xref:`Citation <citation>` format
   :doc:`BibTeX Sphinx extension <bibtex:index>`, Converts :xref:`bibtex`
   :xref:`ottobib`, :xref:`bibtex` database for :ref:`books <references-books>`
   :xref:`ISBN`, Unique identifier for :ref:`books <references-books>`
   :xref:`bibtex-syntax`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>`
   specifications"
   :xref:`cite-multiple-authors`, Use of ``et. al``

.. _tools-sphinx-autobuild:

sphinx-autobuild
================

:xref:`sphinx-autobuild` is a :ref:`package <tools-anaconda>` that
:ref:`automates <sphinx-autobuilding>` the iterative process of
:ref:`manual builds <sphinx-building-manually>`, which
is helpful when :ref:`proofreading documentation <writing-proofread>`

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-sphinx`, ":wiki-pg:`Documentation <Software_documentation>`
   engine"
   :ref:`Building manually <sphinx-building-manually>`, Usage
   :ref:`Building automatically <sphinx-autobuilding>`, Usage

.. csv-table:: Select reference
   :align: center
   :header: Reference, Topic

   :xref:`sphinx-autobuild`, :wiki-pg:`User <User_(computing)>` manual


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
:wiki-pg:`LaTeX`

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer enviroment <dev-env-intro>`, Setup
   :ref:`Notebook structure <concepts-nbs-tree>`, "
   :wiki-pg:`File <Computer_file>` layout"

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :yt-vid:`Corey Schafer tutorial <HW29067qVWk>`, "Recommended
   :xref:`YouTube` tutorial"
   :github-help:`Markdown <basic-writing-and-formatting-syntax>`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` for
   making :wiki-pg:`links <URL>`, :xref:`tables <tables-generator>`, etc."
   :xref:`tables-generator`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` generator"

The interactive style of :xref:`Jupyter Notebooks <Jupyter>` make it easy to
analyze data with numerical :ref:`conda packages <conda:concept-conda-package>`

.. csv-table:: Numerical analysis :ref:`packages <conda:concept-conda-package>`
   :align: center
   :header: Package, Official tutorial, YouTube tutorial

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
   :align: center
   :header: Extension, Function

   :doc:`nb-extensions:nbextensions/collapsible_headings/readme`, "Section
   management"
   :doc:`nb-extensions:nbextensions/toc2/README`, "Automatic section
   linking"
   :doc:`nb-extensions:nbextensions/varInspector/README`, "Data value
   inspection"
   :xref:`live-md-preview`, "Quick previewing for :wiki-pg:`LaTeX` and
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

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`Developer environment <dev-env-intro>`, Setup
   :ref:`Code structure <concepts-code-tree>`, Specific components
   :ref:`Testing <testing-intro>`, Walkthrough
   :ref:`tools-vs-code`, Integration
   :ref:`pytest procedures <procedures-pytest>`, Usage

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :doc:`pytest <pytest:index>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   :xref:`codebasics-pytest`, Recommended :xref:`YouTube` tutorial
   :doc:`pytest tutorials <pytest:contents>`, Official tutorials

************
Distributing
************

.. _tools-pypi:

PyPI
====

*Coming soon*
