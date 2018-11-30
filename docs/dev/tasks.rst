############
Common tasks
############


*************
Documentation
*************

Building Sphinx documentation
=============================

Per :xref:`Willing-Sphinx`:

#. Change working directory to documentation root directory
#. From command line:

   #. :command:`make html` to create new ``.html`` files
   #. :command:`python -m http.server` to start running an ``html`` server

      * Leave this process running even when rebuilding

#. Open http://localhost:8000/_build/html/index.html in a browser
#. :command:`make clean` to clear out old ``.html`` files before committing

.. Tip::
   If a server is already running, make a new build and refresh the browser
   window to view changes

.. Note::
   Run :command:`make linkcheck` occasionally to verify that links in the project
   reference valid locations

Referencing external links
==========================

Per :xref:`xref-ext`:

#. Add an entry to ``xref_links`` in ``conf.py``

   * Put in new links below the delimiter comment::

     # New links below, sorted links above

#. Add a link in documentation via ``:xref:`reference-name```
#. Add a description of the link to :ref:`References`

   * Now the link can be moved above the delimiter comment in ``conf.py``

.. Tip::
   Use a base url from ``url`` in ``conf.py`` for common references like
   YouTube videos

.. Note::
   As long as the delimiter comment is properly used, links can be sorted in
   batches

