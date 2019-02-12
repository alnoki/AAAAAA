.. 41bbe32

.. _sphinx-procedures:


######
Sphinx
######

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`tools-sphinx`, :term:`AAAAAA` conceptual explanation
   :xref:`Practical Sphinx presentation <Willing-Sphinx>`, "Common commands"
   :xref:`Project setup screencast <Yusuf-Sphinx-RTD>`, "How projects work"
   :doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`, "Official
   tutorial"

.. contents:: Contents
   :local:

.. _sphinx-building-documentation:


**********************
Building documentation
**********************

Per :xref:`Willing-Sphinx`:

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>` from
   inside the :ref:`documentation root directory<concepts-project-dir-tree>` if
   it is not already :ref:`active <conda:activate-env>`
#. From the :ref:`VS Code integrated terminal <tools-vs-code>`, make a new
   build then start a local server:

   .. code-block:: bash

      make html
      python -m http.server

#. Open http://localhost:8000/_build/html/index.html in a browser to view the
   build
#. You can update the :ref:`.rst files <tools-restructured-text>` and make
   another build, but don't start another server (unless you want an
   :xref:`http-socket-error`):

   .. code-block:: bash

      make html

#. Refresh the browser to see changes
#. Before :ref:`committing <git-committing>`, clear out the build files:

   .. code-block:: bash

      make clean

.. _sphinx-managing-references:


*******************
Managing references
*******************

.. _sphinx-intersphinx:

Using Intersphinx
=================

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`sphinx.ext.intersphinx <sphinx:usage/extensions/intersphinx>`, "
   :std:doc:`Sphinx extension <sphinx:usage/extensions/index>` documentation"
   :xref:`Intersphinx reference syntax <intersphinx-inv-targets>`, "Syntax
   explanation"
   :xref:`Intersphinx inventory parser <intersphinx-inv-parser>`, "For viewing
   large map outputs"

#. Locate the project's
   :std:doc:`objects.inv <sphinx:usage/extensions/intersphinx>`
   mapping, using the :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      python -msphinx.ext.intersphinx http://www.sphinx-doc.org/en/master/objects.inv

   * You may have to experiment with the project root link. Some common
     endings:

      * ``.io/en/latest/``
      * ``.com/en/latest/``

#. Add the project's root to
   :std:doc:`conf.py <sphinx:usage/configuration>`:

   .. code-block:: python

      intersphinx_mapping = {
         'python': ('https://docs.python.org/3', None),
         'sphinx': ('http://www.sphinx-doc.org/en/master/', None),
         'pytest': ('https://docs.pytest.org/en/latest/', None),
         'rtfd': ('https://docs.readthedocs.io/en/latest/', None),
         'rtd-sphinx-theme':
            ('https://sphinx-rtd-theme.readthedocs.io/en/latest/', None),
         ...

#. Inspect the :std:doc:`objects.inv mapping <sphinx:usage/extensions/intersphinx>`

   * For large outputs, consider using a command line program (like
     :program:`Terminal` on a :xref:`Mac`), which can be maximized to full
     screen

#. Locate the desired target in the mapping output and link to it using a
   corresponding :std:doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. csv-table:: Referencing select mapping outputs
      :header: "Category in objects.inv", "Role to use"
      :align: center

      ``std:doc``, ``:doc:``
      ``rst:directive``, ``:rst:dir:``
      ``std:label``, ``:ref:``

#. Documentation pages, under ``std:doc``, are arranged like the project's
   :ref:`table of contents <sphinx:toctree-directive>`, so you can figure
   out the :std:doc:`role target <sphinx:usage/restructuredtext/roles>` from
   the link that a web browser uses to render the documentation page:

   * https://docs.python.org/3/tutorial/introduction.html
     (**tutorial/introduction**) yields

     .. code-block:: rest

        Here is a :std:doc:`tutorial <python:tutorial/introduction>`

#. Add a description of the link to :ref:`links <references-links>`
#. :std:doc:`Add a link role <sphinx:usage/restructuredtext/roles>` to
   documentation using the appropriate
   :ref:`capitalization <concepts-documentation-style>`. For example:

   .. code-block:: rest

      Read about :std:doc:`Sphinx roles <sphinx:usage/restructuredtext/roles>`

.. tip::
   :xref:`intersphinx-numpy-matplotlib` has instructions for referencing
   :std:doc:`NumPy <numpy:about>` and :std:doc:`Matplotlib <matplotlib:index>`


.. _sphinx-xref:

Referencing external links
==========================

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Sphinx xref extension <xref-ext>`, Manages external links
   :ref:`Using a references extension <sublime-with-sphinx:use the external links extension>`, "
   Related configuration and usage"

#. Add a reference to the link in
   :std:doc:`conf.py <sphinx:usage/configuration>`

   * If the link has a common base link, like in a
     :xref:`YouTube video <YouTube>`, add it to the ``url`` mapping
     :ref:`dictionary <python:tut-dictionaries>`:

     .. code-block:: python

        # Base urls used by xrefs extension
        url = {
           'GitHub': 'https://github.com/',
           'YT vid': 'https://www.youtube.com/watch?v=',  # Video
           ...

   * Put new links in the ``xref_links`` mapping
     :ref:`dictionary <python:tut-dictionaries>` below the delimiter
     :ref:`comment <python:comments>`

     .. code-block:: python

        xref_links = {
           'Python': ('Python', 'https://www.python.org'),
           'xref-ext': ("Michael Jones' sphinx-xref repository",
                       url['GitHub'] + 'michaeljones/sphinx-xref'),
           ...
           'AAAAAA-nbs': ("Jupyter Notebook viewer for AAAAAA", 'https://nbviewer.'
                          'jupyter.org/github/alnoki/AAAAAA/tree/master/nbs/'),
           # New links below, sorted links above
           'doc8-newline-issue':
               ("Doc8 newline issue fix", url['GitHub'] + 'vscode-restructuredtext/'
               'vscode-restructuredtext/issues/84'),
           }

#. :std:doc:`Add a link role <sphinx:usage/restructuredtext/roles>` to
   documentation using the appropriate
   :ref:`capitalization <concepts-documentation-style>`. For example:

   .. code-block:: rest

      Read about the :xref:`xref extension <xref-ext>`

#. Add a description of the link to :ref:`links <references-links>`

   * After this step, the link can be moved above the delimiter
     :ref:`comment <python:comments>` in
     :ref:`conf.py <tools-sphinx>`

.. tip::

   * As long as links aren't put above the delimiter
     :ref:`comment <python:comments>` until after they are put
     into :ref:`links <references-links>`, links can be sorted in batches
   * If you put a link in documentation and in :ref:`links <references-links>`
     first, you can bypass the delimiter :ref:`comment <python:comments>` when
     adding to :ref:`conf.py <tools-sphinx>`

.. _sphinx-checking-links:

Checking links
==============

#. With a :ref:`build server running<sphinx-building-documentation>`, use the
   :ref:`integrated terminal <tools-vs-code>` to enter:

   .. code-block:: bash

      make linkcheck

.. _sphinx-update-labels:

Updating labels
===============

#. With an :ref:`active build running <sphinx-building-documentation>`,
   inspect :ref:`labels <ref-role>` using
   :ref:`intersphinx <sphinx-intersphinx>` on ``_build/html/objects.inv``
#. Verify the proper :ref:`label style <concepts-documentation-style>`
#. Update any :ref:`labels <ref-role>` via the
   :ref:`VS code command palette <tools-vs-code>`:
   :guilabel:`Search: Replace in Files`

.. _sphinx-reference-book:

Referencing books
=================

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`tools-bibtex`, :term:`AAAAAA` conceptual explanation
   :xref:`book`, Information source
   :xref:`bibtex`, File format
   :doc:`BibTeX extension <bibtex:index>`, Parses :xref:`bibtex`
   :xref:`ottobib`, :xref:`bibtex` database for :ref:`books <references-books>`
   :xref:`ISBN`, Unique identifier for :ref:`books <references-books>`
   :ref:`refs.bib <concepts-documentation>`, :xref:`bibtex` citation collection
   :xref:`bibtex-syntax`, Syntax specifications
   :xref:`cite-multiple-authors`, Use of ``et. al``

#. Check :xref:`ottobib` for the relevant :xref:`ISBN`
#. Use the :xref:`bibtex` option to add a :xref:`book entry <bibtex-syntax>` to
   :ref:`refs.bib <concepts-documentation>`

   * A ``book`` :xref:`entry <bibtex-syntax>` requires at least ``author`` (or
     ``editor``), ``title``, ``publisher``, and ``year``
     :xref:`fields <bibtex-syntax>`
   * Consider :xref:`et. al conventions <cite-multiple-authors>` for multiple
     authors

#. Add an entry to :ref:`books <references-books>`

   * Use a :ref:`heading <concepts-documentation-example>` so that
     :rst:dir:`toctree` can index the entry

   * Use a :ref:`label <concepts-documentation>` that appends ``book-`` to the
     first line of the :xref:`bibtex` in
     :ref:`refs.bib <concepts-documentation>`

   .. code-block:: rest
      :emphasize-lines: 1, 7

      .. _book-on-managing-yourself:

      ********************
      On Managing Yourself
      ********************

      .. csv-table:: :cite:`on-managing-yourself`
         :header: "Page(s)", "Topic"
         :align: center

   .. code-block:: none
      :emphasize-lines: 1

      @Book{on-managing-yourself,
      author = {Clayton M. Christensen et. al},
      title = {HBR's 10 Must Reads: On Managing Yourself},
      publisher = {Harvard Business Review Press},
      year = {2010},
      address = {Boston, Massachusetts},
      isbn = {978-1-4221-5799-2}
      }

.. tip::

   The :doc:`BibTeX extension <bibtex:index>` is unreceptive to
   :std:doc:`role titles <sphinx:usage/restructuredtext/roles>`


