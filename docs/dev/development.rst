###########
Development
###########

.. tip::
   The AAAAAA ``README``, at the bottom of the :xref:`AAAAAA-repo`, contains
   some additional links that are commonly referenced during development as
   well as some philosophies and directory structure notes


.. toctree::
   :caption: Contents
   :maxdepth: -1

   zen
   code


*****
Tools
*****

All the software tools used to create the AAAAAA are open source:

* :xref:`Anaconda` helps manage Python packages used in the AAAAAA
* `pytest <https://docs.pytest.org/en/latest/>`_ is used to create tests for the AAAAAA source code
* `Jupyter Notebooks <http://jupyter.org>`_ are used for interactive development documentation
* `Read the Dox with Sphinx <https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html>`_ is used to document code via `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ (``reST``)

  * This documentation is built using the `Read the Docs Sphinx Theme <https://sphinx-rtd-theme.readthedocs.io/en/latest/>`_

* `VS Code <https://code.visualstudio.com>`_ is the preferred integrated development environment used to edit code and documentation. Extensions used:

  * `Python  <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
  * `RST preview <https://marketplace.visualstudio.com/items?itemName=tht13.rst-vscode>`_ for editing  ``reST``
  * `Test Explorer UI <https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter>`_ for visualising ``pytest`` tests during development

Common tasks
============

Building documentation
^^^^^^^^^^^^^^^^^^^^^^

Per :xref:`Willing-Sphinx`:

#. Change working directory to documentation root directory
#. From command line:

   #. ``make html`` to create new ``.html`` files
   #. ``python -m http.server`` to start running an ``html`` server

      * Leave this process running even when rebuilding

#. Open http://localhost:8000/_build/html/index.html in a browser
#. ``make clean`` to clear out old ``.html`` files before committing

.. Tip::
   If a server is already running, make a new build and refresh the browser
   window to view changes

.. Note::
   Run ``make linkcheck`` occasionally to verify that links in the project
   reference valid locations

Referencing external links
^^^^^^^^^^^^^^^^^^^^^^^^^^

Per :xref:`xref-ext`:

#. Add an entry to ``xref_links`` in ``conf.py``

   * Put in new links below the delimiter comment::

     # New links below, sorted links above

#. Add a link in documentation via ``:xref:`reference-name```
#. Add a description of the link to :ref:`References`

   * Now the link can be moved above the delimiter comment in ``conf.py``

.. Note::
   As long as the delimiter comment is properly used, links can be sorted in
   batches

.. Tip::
   Use a base url from ``url`` in ``conf.py`` for common references like
   YouTube videos


*************
Documentation
*************
Documentation is written primarily according to the ``Python developer's guide``
and secondarily according to:
`Style guide for Sphinx-based documentations <https://documentation-style-guide-sphinx.readthedocs.io/en/latest/index.html>`_

Thus, 3 spaces are used for indentation and sections ``H1`` and ``H2`` are
preceded by two blank lines

*****************
Jupyter Notebooks
*****************
`Jupyter Notebooks <http://jupyter.org>`_ are used for some analyses, and
alnoki's notebooks for the AAAAAA can be accessed
`here <https://nbviewer.jupyter.org/github/alnoki/AAAAAA/tree/master/nbs/>`_.
References to specific notebooks should be found throughout the
AAAAAA documentation, but the above link is for the highest-level notebook
directory