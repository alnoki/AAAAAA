.. _tools:


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
:ref:`packages <conda:concept-conda-package>` that are free to download and
use. The base :xref:`Anaconda` collection has way more
:ref:`packages <conda:concept-conda-package>` than :term:`AAAAAA` require, so
you can use :std:doc:`Miniconda<conda:user-guide/install/index>` to acess only
the ones that you need

You can manage these :ref:`packages <conda:concept-conda-package>` using
:std:doc:`conda <conda:index>`, a command-line
style configurator that automatically checks dependencies and maintains
compatibility. :ref:`conda:concept-conda-package` can be downloaded from
different :ref:`conda channels <conda:channels-glossary>`

The :ref:`documenting <setup-documenting>` setup instructions describe how to
:std:doc:`create <conda:commands/create>` a new
:ref:`conda environment <conda:concept-conda-env>`, called :term:`a6`:

.. glossary::

   a6
      A :ref:`conda environment <conda:concept-conda-env>` that contains all
      the necessary :ref:`packages <conda:concept-conda-package>` that
      :term:`AAAAAA` needs

      .. tip::

         :ref:`conda-import-a6` requires less commands than the
         :ref:`developer setup <setup-documenting>`

      .. _anaconda-packages-table:

      .. csv-table:: :ref:`conda:concept-conda-package` in :term:`AAAAAA`
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
         :std:doc:`Sphinx <sphinx:intro>` , Build documentation, "
         :ref:`Documenting <setup-documenting>`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`RTD Sphinx Theme <rtd-sphinx-theme:index>`, "Documentation
         appearance", "
         :ref:`Documenting <setup-documenting>`", "
         :ref:`conda <conda:channels-glossary>`"
         :xref:`Doc8 <Doc8>`, Check documentation syntax, "
         :ref:`Documenting <setup-documenting>`", :xref:`conda-forge`
         :xref:`Jupyter Notebook <Jupyter>`, Interactive analysis, "
         :ref:`analyzing`","
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`Notebook Extensions <nb-extensions:index>`, "Extra analysis
         tools", :ref:`analyzing`, :xref:`conda-forge`
         :std:doc:`NumPy <numpy:about>`, "Number processing", "
         :ref:`analyzing`", :ref:`conda <conda:channels-glossary>`
         :std:doc:`Matplotlib <matplotlib:index>`, "Data plotting", "
         :ref:`analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pandas <pandas:index>`, "Dataset management", "
         :ref:`analyzing`", "
         :ref:`conda <conda:channels-glossary>`"
         :std:doc:`pytest <pytest:index>`, Code testing, Testing, "
         :ref:`conda <conda:channels-glossary>`"

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`conda:index`, General functionality information
   :std:doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
   :std:doc:`conda <conda:index>` commands"
   :xref:`Corey Schafer tutorials <Corey-Schafer-vids>`, "Learn
   :xref:`Python`"
   :xref:`codebasics tutorials <codebasics-pytest>`, "Learn
   :std:doc:`pytest <pytest:index>`"

.. _tools-git:


***
Git
***

:xref:`Git <git-manual>` is used create and track changes to the
:xref:`AAAAAA-repo`. It is a version control system that allows the project
to be updated with :xref:`commits <git-commit>`, which are like
snapshots in time that describe minor changes to the project throughout its
history

:xref:`GitHub` is a free service that hosts the :xref:`AAAAAA-repo`

There are several command-line style text navigators that go along with
:xref:`Git <git-manual>`

.. csv-table:: Text navigators
   :header: "Tool", "Topic"
   :align: center

   :xref:`Vim <Vim-tutorial>`, ":ref:`Configuring <git-setup>` and
   :ref:`committing`"
   :xref:`less <less-pager>`, "
   :ref:`Viewing project history <git-view-project-log>`"

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`git-manual`, Quick practical reference
   :xref:`git-book`, In-depth conceptual explanations

A list of common :term:`AAAAAA` usage examples is at
:ref:`Git Procedures <git-procedures>`


******
Sphinx
******

:std:doc:`Sphinx <sphinx:intro>` is the engine used to create all the
documentation for :term:`AAAAAA` and even for
:std:doc:`Python itself <python:tutorial/index>`. Sphinx uses the
:std:doc:`reStructuredText <sphinx:usage/restructuredtext/basics>` (``reST``)
markup language

The :ref:`table of contents <sphinx:toctree-directive>` facility provides a
linearly navigable structure that ensures access to all pages of documentation

:std:doc:`Sphinx extensions <sphinx:usage/extensions/index>` enable additional
functionality and several are used in :term:`AAAAAA`

.. csv-table:: :std:doc:`Sphinx extensions <sphinx:usage/extensions/index>`
   in :term:`AAAAAA`
   :header: "Extension", "Purpose"
   :align: center

   :ref:`Intersphinx <intersphinx-linking>`, "Link to other
   :std:doc:`Sphinx <sphinx:intro>` projects"
   :ref:`xref <xref-linking>`, Reference external :ref:`links`
   :std:doc:`Read the Docs theme <rtd-sphinx-theme:index>`, "Visual appearance
   for this website"

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`Python Developer's Guide<py-dev-guide:documenting>`, "
   :xref:`Python` guide to using :std:doc:`Sphinx <sphinx:intro>`"
   :std:doc:`Sphinx <sphinx:intro>`, Official documentation
   :xref:`Practical use seminar <Willing-Sphinx>`, "Practical commands and
   functions"
   :xref:`quick-reST`, "
   :std:doc:`reStructuredText <sphinx:usage/restructuredtext/basics>`
   syntax"
   :ref:`References extension configuration <sublime-with-sphinx:use the external links extension>`, "
   :std:doc:`Extensions <sphinx:usage/extensions/index>` installation and
   configuration"


A list of common :term:`AAAAAA` usage examples is at
:ref:`Sphinx Procedures <sphinx-procedures>`


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

.. _tools-VS-Code:


*******
VS Code
*******

:xref:`VS-Code` is an integrated development environment that is used to
develop, to document, and to test code

.. csv-table:: :xref:`VS Code extensions <VS-Code-extensions>` used with
   :term:`AAAAAA`
   :header: "Extension", "Purpose"
   :align: center

   :xref:`Python <VS-Code-Python-ext>`, Developing :xref:`Python`
   :xref:`Bookmarks <VS-Code-bookmarks-ext>`, Mark/navigate code
   :xref:`RST preview <RST-preview-ext>` [#]_ [#]_, "Editing
   :std:doc:`reST <sphinx:usage/restructuredtext/basics>` "
   :xref:`Test explorer UI <Test-explorer-UI>`, "Testing with
   :std:doc:`pytest <pytest:index>`"
   :xref:`GitLens <GitLens>`, Advanced :xref:`Git <git-manual>` functionality

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

The :xref:`AAAAAA-repo` comes with a collection of
:xref:`VS-Code-settings` that will automatically configure most of your
workspace. If you completed the :ref:`developer setup <dev-environment>`, then
all the relevant settings should already be installed!

.. rubric:: Footnotes

.. [#] Requires a :xref:`doc8-newline-issue`, included in the provided
   :xref:`VS-Code-settings`
.. [#] Offers live rendering, but is not as reliable as
   :ref:`using a browser <building-documentation>`. For example, fails to
   properly render :ref:`intersphinx links <intersphinx-linking>`


*******
Jupyter
*******

:xref:`Jupyter Notebooks <Jupyter>` enable an interactive style of
algorithm development, and can quickly render :xref:`LaTeX`

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Corey Schafer tutorial <Schafer-Jupyter>`, "Tutorial video on
   :xref:`YouTube`"
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
   :std:doc:`10 min tutorial <pandas:10min>`", "
   :xref:`pandas <codebasics-pandas>`"

The :std:doc:`nb-extensions:index` provide additional functionality

.. csv-table:: :std:doc:`Select extensions <nb-extensions:index>`
   :header: "Extension", "Function"
   :align: center

   :std:doc:`nb-extensions:nbextensions/collapsible_headings/readme`, "Section
   management"
   :std:doc:`nb-extensions:nbextensions/toc2/README`, "Automatic section
   linking"
   :std:doc:`nb-extensions:nbextensions/varInspector/README`, "Data value
   inspection"
   :xref:`live-md-preview`, "Preview equation syntax"
