.. 5863379

.. _concepts-tools:


#####
Tools
#####

.. contents::
   :local:

.. _tools-anaconda:


********
Anaconda
********

:xref:`Anaconda` contains a collection of
:ref:`software packages <conda:concept-conda-package>` that are free to
download and use. The base :xref:`Anaconda` collection has way more
:ref:`packages <conda:concept-conda-package>` than :term:`AAAAAA` require, so
you can use :std:doc:`Miniconda<conda:user-guide/install/index>` to acess only
the ones that you need

You can manage these :ref:`packages <conda:concept-conda-package>` using
:std:doc:`conda <conda:index>`, a command-line configurator that automatically
checks dependencies and maintains compatibility between
:ref:`packages <conda:concept-conda-package>`.
:ref:`conda:concept-conda-package` can be downloaded from
different :ref:`conda channels <conda:channels-glossary>`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`conda:index`, Official reference
   :std:doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :std:doc:`conda <conda:index>` commands"
   :xref:`Corey Schafer tutorials <Corey-Schafer-vids>`, "Learn
   :xref:`Python`"
   :ref:`Conda procedures <conda-procedures>`, :term:`AAAAAA` usage

The :ref:`developer setup <dev-env-intro>` describes how to
:std:doc:`create <conda:commands/create>` a new
:ref:`conda environment <conda:concept-conda-env>`, called :term:`a6`:

.. glossary::

   a6
      A :ref:`conda environment <conda:concept-conda-env>` containing all
      the :ref:`packages <conda:concept-conda-package>` that :term:`AAAAAA`
      require

      .. tip::

         :ref:`conda-import-a6` requires less commands than the
         :ref:`developer setup <dev-env-intro>`

      .. _concepts-packages-table:

      .. csv-table:: :ref:`conda:concept-conda-package` required for
         :term:`AAAAAA`
         :header: "Package", "Function", "Setup Phase", "Channel"
         :align: center

         :xref:`Python`, Code creation, "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`conda <conda:index>`, Package management, "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :pep:`8`, Check code style, "
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`Sphinx <sphinx:intro>` , Create documentation, "
         :ref:`Documenting <dev-env-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`RTD Sphinx Theme <rtd-sphinx-theme:index>`, "Documentation
         appearance", "
         :ref:`Documenting <dev-env-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :xref:`Doc8 <Doc8>`, Check documentation syntax, "
         :ref:`Documenting <dev-env-documenting>`", :xref:`conda-forge`
         :ref:`tools-bibtex`, :ref:`Book citations <references-books>`, "
         :ref:`Documenting <dev-env-documenting>`", :xref:`conda-forge`
         :xref:`Jupyter Notebook <Jupyter>`, Interactive analysis, "
         :ref:`dev-env-analyzing`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`Notebook Extensions <nb-extensions:index>`, "Extra analysis
         tools", :ref:`dev-env-analyzing`, :xref:`conda-forge`
         :std:doc:`NumPy <numpy:about>`, "Number processing", "
         :ref:`dev-env-analyzing`", :ref:`conda <conda:channels-glossary>`
         :std:doc:`Matplotlib <matplotlib:index>`, "Data plotting", "
         :ref:`dev-env-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pandas <pandas:index>`, "Dataset management", "
         :ref:`dev-env-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pip <python:installing/index>`, Configuring test code, "
         :ref:`dev-env-testing`", :ref:`conda <conda:channels-glossary>`
         :std:doc:`pytest <pytest:index>`, Code testing, "
         :ref:`dev-env-testing`", "
         :ref:`conda <conda:channels-glossary>`"

.. _tools-git:


***
Git
***

:xref:`Git <git-manual>` is used create and track changes to the
:xref:`AAAAAA-repo`. :xref:`Git <git-manual>` is a version control system that
allows the project to be updated with :xref:`commits <git-commit>`, which are
like snapshots in time that describe minor changes to the project throughout
its history. Each :xref:`commit <git-commit>` is identified by a :xref:`sha1`,
a unique identifier that can be accessed by viewing a
:xref:`commit log <git-log>`

:xref:`Tags <git-tag>`, which provide a unique identifier for
:xref:`commits <git-commit>`, and :xref:`branches <git-branch>`, which enable
independent sequences of :xref:`commits <git-commit>`, are used to manage
:ref:`project versions <version-list>`

:xref:`GitHub` is a free service that hosts the :xref:`AAAAAA-repo`

There are several command-line style text navigators that go along with
:xref:`Git <git-manual>`

.. csv-table:: Text navigators
   :header: "Tool", "Topic"
   :align: center

   :xref:`Vim <Vim-tutorial>`, ":ref:`Configuring <git-setup>` and
   :ref:`git-committing`"
   :xref:`less <less-pager>`, "
   :ref:`Viewing project history <git-view-project-log>`"

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`git-manual`, Quick practical reference
   :xref:`git-book`, In-depth conceptual explanations
   :xref:`git-commit-guidelines`, Contribution guidelines
   :ref:`Git procedures <git-procedures>`, :term:`AAAAAA` usage


*************
Documentation
*************

.. _tools-sphinx:

Sphinx
======

:std:doc:`Sphinx <sphinx:intro>` is the documentation engine that creates all
the documentation for :term:`AAAAAA` and even for
:std:doc:`Python itself <python:tutorial/index>`. Sphinx is built on the
:ref:`tools-restructured-text` (``reST``) markup language

:std:doc:`Sphinx <sphinx:intro>` has a
:ref:`table of contents <sphinx:toctree-directive>` feature, which provides a
linearly navigable structure that ensures access to all pages of documentation.
:term:`AAAAAA` are documented using the
:std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which provides
a mobile-friendly viewing experience with a modern look

:std:doc:`Sphinx extensions <sphinx:usage/extensions/index>` enable additional
functionality and several are used in :term:`AAAAAA`:

.. csv-table:: :std:doc:`Sphinx extensions <sphinx:usage/extensions/index>`
   in :term:`AAAAAA`
   :header: "Extension", "Purpose"
   :align: center

   :ref:`Intersphinx <tools-intersphinx>`, "Create
   :ref:`links <references-links>` to other :doc:`Sphinx <sphinx:intro>`
   projects"
   :ref:`xref <tools-xref>`, "Reference external
   :ref:`links <references-links>`"
   :ref:`tools-napoleon`, Document code components
   :ref:`tools-BibTeX`, Cite books

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :doc:`Python Developer's Guide<py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :std:doc:`Sphinx <sphinx:intro>`"
   :doc:`Sphinx <sphinx:intro>`, Official documentation
   :xref:`Practical use seminar <Willing-Sphinx>`, "Practical commands and
   functions"
   :ref:`References extension configuration <sublime-with-sphinx:use the external links extension>`, "
   :doc:`Extension <sphinx:usage/extensions/index>` installation and
   configuration"
   :doc:`conf.py <sphinx:usage/configuration>`, Configuration settings
   :ref:`Sphinx procedures <sphinx-procedures>`, :term:`AAAAAA` usage

.. _tools-restructured-text:

reStructuredText
================

:xref:`reStructuredText <reST-documentation>` (``reST``) is a markup language
containing syntax to generate fancy components like ``this``, :guilabel:`this`,
or :menuselection:`t --> h --> i --> s`

The two most fundamental :std:doc:`reST <sphinx:usage/restructuredtext/basics>`
components are the :std:doc:`role <sphinx:usage/restructuredtext/roles>`, which
marks a piece of text (usually in-line), and the
:std:doc:`directive <sphinx:usage/restructuredtext/directives>`, which marks a
block of text

:doc:`reST <sphinx:usage/restructuredtext/basics>` files have an ``.rst``
extension, and :ref:`tools-sphinx` converts them whenever documentation is
built

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`sphinx:usage/restructuredtext/basics`, "
   :std:doc:`Sphinx <sphinx:intro>` tutorial on ``reST`` usage"
   :xref:`reST-documentation`, Official documentation
   :xref:`quick-reST`, Practical syntax
   :xref:`reST-cheatsheet`, Quick syntax reference
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   syntax"
   :std:doc:`sphinx:usage/restructuredtext/domains`, "Collections of
   :std:doc:`roles <sphinx:usage/restructuredtext/roles>` and
   :std:doc:`directives <sphinx:usage/restructuredtext/directives>`"

Many :ref:`tools-sphinx` documentation websites have an
:guilabel:`Edit on GitHub` (or similar) feature at
the top of each page. This feature will display the
:std:doc:`reST <sphinx:usage/restructuredtext/basics>` file that created the
page

.. tip::
   You can harvest the syntax for nearly any kind of
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` component from the
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, via the
   :guilabel:`Edit on GitHub` feature

Read the Docs
=============

:std:doc:`Read the Docs<rtfd:index>` is a free online repository that hosts
:std:doc:`Sphinx <sphinx:intro>` projects, and even provides its own
:std:doc:`Sphinx Theme <rtd-sphinx-theme:index>`

:term:`AAAAAA` use the
:std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which generates
the visual appearance of this website!

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Quickstart tutorial <Yusuf-Sphinx-RTD>`, "Starting a
   :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   project"
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   documentation elements"
   :xref:`Writer-intro-to-Sphinx`, Introductory article for technical writers

Sphinx extensions
=================

.. _tools-intersphinx:

Intersphinx
-----------

:doc:`Intersphinx <sphinx:usage/extensions/intersphinx>` helps manage
:ref:`links <references-links>` to other :ref:`tools-sphinx` projects

Usage is described at :ref:`intersphinx procedures <sphinx-intersphinx>`

.. _tools-xref:

xref
----

:xref:`Michael Jones' xref extension <xref-ext>` helps manage
:ref:`links <references-links>` to external content that can not be accessed
via :ref:`intersphinx <tools-intersphinx>`. A simple
:ref:`role <tools-restructured-text>` is used to insert
:ref:`links <references-links>`, and usage is described at
:ref:`xref procedures <sphinx-xref>`

.. _tools-napoleon:

Napoleon
--------

:std:doc:`Napoleon <sphinx:usage/extensions/napoleon>` is a
:ref:`Sphinx extension <tools-sphinx>` that parses code and
creates documentation elements from :ref:`docstrings <python:tut-docstrings>`
and :pep:`type annotations <484>`. It uses the same
:ref:`directives <tools-restructured-text>` as
:doc:`autodoc <sphinx:usage/extensions/autodoc>`, but it
can accept :std:ref:`NumPy docstrings <numpy:format>`

:doc:`Napoleon <sphinx:usage/extensions/napoleon>` and
:doc:`autodoc <sphinx:usage/extensions/autodoc>` both parse
:ref:`docstrings <python:tut-docstrings>` into syntax (like that used for
:ref:`field lists <sphinx:info-field-lists>`) which is native to
:ref:`reST <tools-restructured-text>`

:ref:`Docstrings <python:tut-docstrings>` are annotated using the
:ref:`Python domain <sphinx:python-roles>`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`Docstrings <python:tut-docstrings>`, ":ref:`python:comments` for
   :xref:`Python` code components"
   :doc:`Autodoc <sphinx:usage/extensions/autodoc>`, "
   :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` to include
   :ref:`docstrings <python:tut-docstrings>`"
   :std:ref:`NumPy docstrings <numpy:format>`, "
   :ref:`Docstrings <python:tut-docstrings>` style"
   :pep:`Type annotations <484>`, Syntax guide
   :doc:`Napoleon <sphinx:usage/extensions/napoleon>`, "Accepts
   :std:ref:`NumPy docstrings <numpy:format>`"
   :ref:`Python domain <sphinx:python-roles>`, "
   :std:doc:`Roles <sphinx:usage/restructuredtext/roles>` and
   :std:doc:`directives <sphinx:usage/restructuredtext/directives>`"
   :xref:`Type checking <realpython-type-checking>`, "
   :xref:`RealPython <RealPython>` guide"
   :std:doc:`Sample automodule <demo/api>`, "
   :doc:`Autodoc <sphinx:usage/extensions/autodoc>` demo with
   :std:doc:`RTD Sphinx theme <rtd-sphinx-theme:index>`"
   :doc:`Example NumPy Strings <napoleon:example_numpy>`, Example syntax
   :ref:`sphinx:info-field-lists`, "Resultant
   :ref:`reST <tools-restructured-text>` syntax"

.. _tools-bibtex:

BibTeX
------

:xref:`bibtex` is a special type of citation syntax that :term:`AAAAAA` use
to cite :ref:`books <references-books>`. The
:doc:`BibTeX extension <bibtex:index>` converts
:ref:`refs.bib <concepts-documentation-structure>` into formatted
:ref:`book citations <references-books>`

If know the :xref:`ISBN` for a particular :ref:`book <references-books>`, you
can usually get the :xref:`bibtex` from :xref:`ottobib`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`book`, Information source
   :xref:`bibtex`, Citation file format
   :doc:`BibTeX extension <bibtex:index>`, Parses :xref:`bibtex`
   :xref:`ottobib`, :xref:`bibtex` database for :ref:`books <references-books>`
   :xref:`ISBN`, Unique identifier for :ref:`books <references-books>`
   :xref:`bibtex-syntax`, Syntax specifications
   :xref:`cite-multiple-authors`, Use of ``et. al``
   :ref:`BibTeX procedures <sphinx-reference-book>`, :term:`AAAAAA` usage

.. _tools-vs-code:


*******
VS Code
*******

:xref:`VS-Code` is an integrated development environment that is used to
develop, to document, and to test code

The :xref:`AAAAAA-repo` comes with a collection of
:xref:`VS-Code-settings` that will automatically configure most of your
workspace. If you completed the :ref:`developer setup <dev-env-intro>`, then
all the relevant settings should already be installed!

You can also download the :xref:`VS Code Insider Edition <VS-Code-insiders>`,
which has all the latest features and bug fixes, although it may not be as
stable as the most recent official release

.. csv-table:: :xref:`VS Code extensions <VS-Code-extensions>` used with
   :term:`AAAAAA`
   :header: "Extension", "Purpose", "Setup Phase"
   :align: center

   :xref:`Bookmarks <VS-Code-bookmarks-ext>`, Mark/navigate code, "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`Python <VS-Code-Python-ext>`, Developing :xref:`Python`, "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`RST preview <RST-preview-ext>` [#]_ [#]_, "Editing
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` ", "
   :ref:`Documenting <dev-env-documenting>`"
   :xref:`GitLens <GitLens>`, "Advanced :xref:`Git <git-manual>`
   functionality", :ref:`Documenting <dev-env-documenting>`
   :xref:`Python Test Explorer <Test-explorer-UI>`, "Testing with
   :std:doc:`pytest <pytest:index>`", :ref:`Testing <dev-env-testing>`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Python integration <VS-Code-Python-tutorial>`, "Official tutorial for
   :xref:`Python` with :xref:`VS Code <VS-Code>`"
   :xref:`Command palette <command-palette>`, Quickly input user commands
   :xref:`Settings <VS-Code-settings>`, Settings configuration
   :xref:`Integrated terminal <VS-Code-terminal>`, "Run a command line inside
   :xref:`VS Code <VS-Code>`"
   :xref:`VS-Code-unit-testing`, ":std:doc:`pytest <pytest:index>` integration
   setup"
   :xref:`Markdown`, For :ref:`planning version features <versioning-td3>`
   :ref:`Writing procedures <writing-procedures>`, :term:`AAAAAA` usage

.. rubric:: Footnotes

.. [#] Requires a :xref:`doc8-newline-issue`, included in the provided
   :xref:`VS-Code-settings`
.. [#] Offers live rendering, but is not as reliable as
   :ref:`using a browser <sphinx-building-documentation>`. For example, fails
   to properly render :ref:`intersphinx links <sphinx-intersphinx>`

.. _tools-pytest:


******
pytest
******

:term:`AAAAAA` uses :std:doc:`pytest <pytest:index>`, a
:ref:`conda package<tools-anaconda>`, to verify that code is
functioning as expected

:xref:`VS-Code` natively integrates with :std:doc:`pytest <pytest:index>`,
and additional functionality is provided by the
:ref:`VS Code Python Test Explorer extension<tools-vs-code>`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :doc:`pytest <pytest:index>`, Official documentation
   :xref:`codebasics-pytest`, Recommended :xref:`YouTube` tutorial
   :std:doc:`pytest tutorials <pytest:contents>`, Official tutorials
   :ref:`pytest procedures <pytest-procedures>`, :term:`AAAAAA` usage


.. _tools-jupyter:


*******
Jupyter
*******

:xref:`Jupyter Notebooks <Jupyter>` enable an interactive style of
algorithm development, and can quickly render :xref:`LaTeX`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Corey Schafer tutorial <Schafer-Jupyter>`, "Recommended
   :xref:`YouTube` tutorial"
   :xref:`Markdown`, "Syntax for making links, tables, etc."
   :xref:`tables-generator`, "Table syntax generator"

The interactive style of :xref:`Jupyter Notebooks <Jupyter>` make it easy to
analyze data with numerical :ref:`conda packages <conda:concept-conda-package>`

.. csv-table:: Numerical analysis :ref:`packages <conda:concept-conda-package>`
   :header: "Package", "Official tutorial", "YouTube tutorial"
   :align: center

   :std:doc:`NumPy <numpy:about>`, "
   :std:doc:`Quickstart <numpy:user/quickstart>`", "
   :xref:`NumPy <codebasics-numpy>`"
   :std:doc:`Matplotlib <matplotlib:index>`,"
   :std:doc:`matplotlib:tutorials/index`", "
   :xref:`Matplotlib <codebasics-matplotlib>`"
   :std:doc:`pandas <pandas:index>`, "
   :std:doc:`10 min tutorial <pandas:getting_started/10min>`", "
   :xref:`pandas <codebasics-pandas>`"

The :std:doc:`nb-extensions:index` provide additional functionality

.. csv-table:: Select :std:doc:`extensions <nb-extensions:index>`
   :header: "Extension", "Function"
   :align: center

   :std:doc:`nb-extensions:nbextensions/collapsible_headings/readme`, "Section
   management"
   :std:doc:`nb-extensions:nbextensions/toc2/README`, "Automatic section
   linking"
   :std:doc:`nb-extensions:nbextensions/varInspector/README`, "Data value
   inspection"
   :xref:`live-md-preview`, "Quick equation rendering"

.. tip::
   This :xref:`AAAAAA-nbs` can render any :xref:`Jupyter Notebook<Jupyter>`
   from the :xref:`AAAAAA-repo` inside of a browser, even if
   :xref:`Jupyter <Jupyter>` isn't installed
