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

A list of common :term:`AAAAAA` usage examples is at
:ref:`conda procedures <conda-procedures>`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`conda:index`, Official reference
   :std:doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :std:doc:`conda <conda:index>` commands"
   :xref:`Corey Schafer tutorials <Corey-Schafer-vids>`, "Learn
   :xref:`Python`"

The :ref:`developer setup <setup-dev-environment>` describes how to
:std:doc:`create <conda:commands/create>` a new
:ref:`conda environment <conda:concept-conda-env>`, called :term:`a6`:

.. glossary::

   a6
      A :ref:`conda environment <conda:concept-conda-env>` containing all
      the :ref:`packages <conda:concept-conda-package>` that :term:`AAAAAA`
      require

      .. tip::

         :ref:`conda-import-a6` requires less commands than the
         :ref:`developer setup <setup-dev-environment>`

      .. _concepts-packages-table:

      .. csv-table:: :ref:`conda:concept-conda-package` required for
         :term:`AAAAAA`
         :header: "Package", "Function", "Setup Phase", "Channel"
         :align: center

         :xref:`Python`, Code creation, "
         :ref:`Documenting <setup-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`conda <conda:index>`, Package management, "
         :ref:`Documenting <setup-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :pep:`8`, Check code style, "
         :ref:`Documenting <setup-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`Sphinx <sphinx:intro>` , Create documentation, "
         :ref:`Documenting <setup-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`RTD Sphinx Theme <rtd-sphinx-theme:index>`, "Documentation
         appearance", "
         :ref:`Documenting <setup-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :xref:`Doc8 <Doc8>`, Check documentation syntax, "
         :ref:`Documenting <setup-documenting>`", :xref:`conda-forge`
         :xref:`Jupyter Notebook <Jupyter>`, Interactive analysis, "
         :ref:`setup-analyzing`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`Notebook Extensions <nb-extensions:index>`, "Extra analysis
         tools", :ref:`setup-analyzing`, :xref:`conda-forge`
         :std:doc:`NumPy <numpy:about>`, "Number processing", "
         :ref:`setup-analyzing`", :ref:`conda <conda:channels-glossary>`
         :std:doc:`Matplotlib <matplotlib:index>`, "Data plotting", "
         :ref:`setup-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pandas <pandas:index>`, "Dataset management", "
         :ref:`setup-analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pip <python:installing/index>`, Configuring test code, "
         :ref:`setup-testing`", :ref:`conda <conda:channels-glossary>`
         :std:doc:`pytest <pytest:index>`, Code testing, "
         :ref:`setup-testing`", "
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

:xref:`GitHub` is a free service that hosts the :xref:`AAAAAA-repo`

A list of common :term:`AAAAAA` usage examples is at
:ref:`Git procedures <git-procedures>`

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

.. _tools-sphinx:


******
Sphinx
******

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

A list of common :term:`AAAAAA` usage examples is at
:ref:`Sphinx procedures <sphinx-procedures>`

:std:doc:`Sphinx extensions <sphinx:usage/extensions/index>` enable additional
functionality and several are used in :term:`AAAAAA`

.. csv-table:: :std:doc:`Sphinx extensions <sphinx:usage/extensions/index>`
   in :term:`AAAAAA`
   :header: "Extension", "Purpose"
   :align: center

   :ref:`Intersphinx <sphinx-intersphinx>`, "Link to other
   :std:doc:`Sphinx <sphinx:intro>` projects"
   :ref:`xref <sphinx-xref>`, "Reference external
   :ref:`links <references-links>`"

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide<py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :std:doc:`Sphinx <sphinx:intro>`"
   :std:doc:`Sphinx <sphinx:intro>`, Official documentation
   :xref:`Practical use seminar <Willing-Sphinx>`, "Practical commands and
   functions"
   :ref:`References extension configuration <sublime-with-sphinx:use the external links extension>`, "
   :std:doc:`Extension <sphinx:usage/extensions/index>` installation and
   configuration"
   :std:doc:`conf.py <sphinx:usage/configuration>`, Configuration settings

.. _tools-restructured-text:


****************
reStructuredText
****************

:xref:`reStructuredText <reST-documentation>` (``reST``) is a markup language
containing syntax to generate fancy components like ``this``, :guilabel:`this`,
or :menuselection:`t --> h --> i --> s`

The two most fundamental :std:doc:`reST <sphinx:usage/restructuredtext/basics>`
components are the :std:doc:`role <sphinx:usage/restructuredtext/roles>`, which
marks a piece of text (usually in-line), and the
:std:doc:`directive <sphinx:usage/restructuredtext/directives>`, which marks a
block of text

:std:doc:`reST <sphinx:usage/restructuredtext/basics>` files have an ``.rst``
extension, and :ref:`tools-sphinx` parses them whenever documentation is built

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


*************
Read the Docs
*************

:std:doc:`Read the Docs<rtfd:index>` is a free online repository that hosts
:std:doc:`Sphinx <sphinx:intro>` projects, and even provides its own
:std:doc:`Sphinx Theme <rtd-sphinx-theme:index>`

:term:`AAAAAA` use the
:std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`, which generates
the visual appearance of this website!

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Quick start tutorial <Yusuf-Sphinx-RTD>`, "Starting a
   :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   project"
   :std:doc:`Read the Docs sample project <rtd-sphinx-theme:index>`, "Sample
   documentation elements"
   :xref:`Writer-intro-to-Sphinx`, Introductory article for technical writers

.. _tools-napoleon:


********
Napoleon
********

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

.. _tools-vs-code:


*******
VS Code
*******

:xref:`VS-Code` is an integrated development environment that is used to
develop, to document, and to test code

The :xref:`AAAAAA-repo` comes with a collection of
:xref:`VS-Code-settings` that will automatically configure most of your
workspace. If you completed the :ref:`developer setup <setup-dev-environment>`,
then all the relevant settings should already be installed!

You can also download the :xref:`VS Code Insider Edition <VS-Code-insiders>`,
which has all the latest features and bug fixes, although it may not be as
stable as the most recent official release

.. csv-table:: :xref:`VS Code extensions <VS-Code-extensions>` used with
   :term:`AAAAAA`
   :header: "Extension", "Purpose", "Setup Phase"
   :align: center

   :xref:`Bookmarks <VS-Code-bookmarks-ext>`, Mark/navigate code, "
   :ref:`Documenting <setup-documenting>`"
   :xref:`Python <VS-Code-Python-ext>`, Developing :xref:`Python`, "
   :ref:`Documenting <setup-documenting>`"
   :xref:`RST preview <RST-preview-ext>` [#]_ [#]_, "Editing
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` ", "
   :ref:`Documenting <setup-documenting>`"
   :xref:`GitLens <GitLens>`, "Advanced :xref:`Git <git-manual>`
   functionality", :ref:`Documenting <setup-documenting>`
   :xref:`Python Test Explorer <Test-explorer-UI>`, "Testing with
   :std:doc:`pytest <pytest:index>`", :ref:`Testing <setup-testing>`

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

   :std:doc:`pytest <pytest:index>`, Official documentation
   :xref:`codebasics-pytest`, Recommended :xref:`YouTube` tutorial
   :std:doc:`pytest tutorials <pytest:contents>`, Official tutorials


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
