.. _sphinx-procedures:


######
Sphinx
######

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Practical Sphinx presentation <Willing-Sphinx>`, "Common commands"
   :xref:`Project setup screencast <Yusuf-Sphinx-RTD>`, "How projects work"
   :std:doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`, "
   Official tutorial"

.. contents::

.. _building-documentation:


**********************
Building documentation
**********************

Per :xref:`Willing-Sphinx`:

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>` from
   inside the :ref:`documentation root directory<project-dir-tree>` if it is
   not already :ref:`active <conda:activate-env>`
#. From the :ref:`integrated terminal <tools-VS-Code>`, make a new build then
   start a local server:

   .. code-block:: bash

      make html
      python -m http.server

#. Open http://localhost:8000/_build/html/index.html in a browser to view the
   build
#. You can update the :ref:`.rst files <concepts-documentation>` and make
   another build, but don't start another server (unless you want an
   :xref:`http-socket-error`):

   .. code-block:: bash

      make html

#. Refresh the browser to see changes

#. Before :ref:`committing <committing>`, clear out the build files:

   .. code-block:: bash

      make clean

.. _managing-references:


*******************
Managing references
*******************

.. _intersphinx-linking:

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
   mapping, using the :ref:`VS Code integrated terminal <tools-VS-Code>`:

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
     :program:`terminal.app` on a :xref:`Mac`), which can be maximized to full
     screen

#. Locate the desired target in the mapping output and link to it using a
   corresponding :std:doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. csv-table:: Referencing mapping outputs
      :header: "Category in objects.inv", "Role to use"
      :align: center

      ``std:doc``, ``:std:doc:``
      ``rst:directive``, ``:rst:dir:``
      ``std:label``, ``:ref:``

#. Documentation pages, under ``std:doc``, are arranged like the project's
   :ref:`table of contents <sphinx:toctree-directive>`, so you can figure
   out the :std:doc:`role target <sphinx:usage/restructuredtext/roles>` from
   the link that a web browser uses to render the documentation page:

   * https://docs.python.org/3/tutorial/introduction.html
     (**tutorial/introduction**) yields

     .. code-block:: rest

        Here is a description about :std:doc:`comments <python:tutorial/introduction>`

#. Add a description of the link to :ref:`links <links>`
#. :std:doc:`Add a link role <sphinx:usage/restructuredtext/roles>` to
   documentation using the appropriate
   :ref:`capitalization <documentation-style>`. For example:

   .. code-block:: rest

      Read about :std:doc:`Sphinx roles <sphinx:usage/restructuredtext/roles>`

.. tip::
   :xref:`intersphinx-numpy-matplotlib` has instructions for referencing
   :std:doc:`Numpy <numpy:about>` and :std:doc:`Matplotlib <matplotlib:index>`


.. _xref-linking:

Referencing external links
==========================

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`Sphinx xref extension <xref-ext>`, Manages external links
   :ref:`Using references extension <sublime-with-sphinx:use the external links extension>`, "
   Additional configuration and usage"

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
     :std:doc:`comment <python:tutorial/introduction>`

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
   :ref:`capitalization <documentation-style>`. For example:

   .. code-block:: rest

      Read about the :xref:`xref extension <xref-ext>`

#. Add a description of the link to :ref:`links <references>`

   * After this step, the link can be moved above the delimiter
     :std:doc:`comment <python:tutorial/introduction>` in
     :std:doc:`conf.py <sphinx:usage/configuration>`

.. Tip::
   As links aren't put above the delimiter
   :std:doc:`comment <python:tutorial/introduction>` until after they are put
   into :ref:`links <links>`, links can be sorted in batches

Checking links
==============

#. With a :ref:`server running<building-documentation>`, use the
   :ref:`integrated terminal <tools-VS-Code>` to enter:

   .. code-block:: bash

      make linkcheck
