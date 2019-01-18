.. _tools:


#####
Tools
#####

All the software tools used to create :term:`AAAAAA` are open source:


********
Anaconda
********

:xref:`Anaconda` contains a collection of :xref:`Python` packages that are
free to download and use. The base :xref:`Anaconda` collection has way more
packages than the :term:`AAAAAA` requires, so you can use
:std:doc:`Miniconda<conda:user-guide/install/index>` to acess only the ones
that you need

You can manage these packages using :std:doc:`conda:index`, a command-line
style configurator that automatically checks package dependencies and maintains
compatibility

Some select references:

   .. csv-table::
      :header: "Reference", "Topic"

      :std:doc:`Conda cheatsheet <conda:user-guide/cheatsheet>`, "Common
      :std:doc:`conda:index` commands"
      :xref:`Corey Schafer tutorials <Corey-Schafer-vids>`, "Learn
      :xref:`Python`"
      :xref:`codebasics tutorials <codebasics-pytest-vids>`, "Learn
      :std:doc:`pytest <pytest:index>`"

***
Git
***

:xref:`Git <git-manual>` is used create and track changes to the
:xref:`AAAAAA-repo`. It is a version control system that allows the project
to be updated with :xref:`commits <git-commit>`, which are like
snapshots in time that describe minor changes to the project throughout its
history. The :xref:`git-book` explains all of this and more

A list of common :term:`AAAAAA` usage examples is at
:ref:`Git Procedures <git-procedures>`


*******
VS Code
*******

:xref:`VS-Code` is an integrated development environment that is used to
develop, to document, and to test code. It uses the following extensions:

   .. csv-table::
      :header: "Extension", "Purpose"

      :xref:`Python <VS-Code-Python-ext>`, Developing :xref:`Python`
      :xref:`Bookmarks <VS-Code-bookmarks-ext>`, "Marking and navigating to
      lines of code"
      :xref:`RST preview <RST-preview-ext>` [#]_, "Editing
      :std:doc:`reST <sphinx:usage/restructuredtext/basics>`"
      :xref:`Test explorer UI <Test-explorer-UI>`, "Testing with
      :std:doc:`pytest <pytest:index>`"
      :xref:`GitLens <GitLens>`, "Advanced :xref:`Git <git-manual>`
      functionality"

If you want more information on the use of some particular functionalities:

   .. csv-table::
      :header: "Reference", "Topic"

      :xref:`Python integration <VS-Code-Python-tutorial>`, "Official tutorial
      for :xref:`Python` with :xref:`VS Code <VS-Code>`"
      :xref:`Command palette <command-palette>`, Quickly input user commands
      :xref:`Settings <VS-Code-settings>`, Settings configuration
      :xref:`Integrated terminal <VS-Code-terminal>`, "Run a command line
      inside :xref:`VS Code <VS-Code>`"
      :xref:`VS-Code-unit-testing`, ":std:doc:`pytest <pytest:index>`
      integration setup"

*****
Other
*****

*More explanations coming soon*

#. :std:doc:`pytest <pytest:index>` is for testing :term:`AAAAAA` source code
#. :xref:`Jupyter Notebooks <Jupyter>` enable an interactive style of
   algorithm development, and can quickly render :xref:`LaTeX`
#. :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   is a documentation engine that helped create this website!

   * The webpage theme is brought to you by the
     :std:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`
   * Several :std:doc:`Sphinx extensions <sphinx:usage/extensions/index>`
     provide added functionality

      * :ref:`Intersphinx <intersphinx-linking>`
      * :ref:`xref <xref-linking>`

.. tip::
   See :ref:`references` if you want more information about the above
   extensions

.. rubric:: Footnotes

.. [#] Requires a :xref:`doc8-newline-issue`
