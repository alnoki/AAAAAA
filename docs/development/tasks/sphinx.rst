######
Sphinx
######


*******************
Managing references
*******************

Using Intersphinx
=================

Per :std:doc:`Intershpinx documentation <usage/extensions/intersphinx>`:

#. Add the project's root url to ``conf.py``::

    intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'sphinx': ('http://www.sphinx-doc.org', None)
    }
#. Inspect the ``objects.inv`` mapping, usually located under the root:

   .. code-block:: none

      python -msphinx.ext.intersphinx http://www.sphinx-doc.org/objects.inv

   * Consider an :xref:`intersphinx-inv-parser` for large outputs

#. Locate the desired target in the mapping output, which is arranged like the
   project's table of contents. For example, ``usage/extensions/intersphinx``
   is located in the ``std:doc`` section of the output from the above command

   * See :xref:`intersphinx-inv-targets` for a formatting explanation

#. Link to the reference as desired and (for archival purposes) add a
   description of the link to :ref:`References`

.. Tip::
   To control the display text of the link:

   #. Default text: ``:std:doc:`usage/extensions/intersphinx``` produces
      :std:doc:`usage/extensions/intersphinx`

   #. Custom: ``:std:doc:`Custom <usage/extensions/intersphinx>``` produces
      :std:doc:`Custom <usage/extensions/intersphinx>`

.. Note::
   See :xref:`intersphinx-numpy-matplotlib` instructions for these specific
   cases

Referencing external links
==========================

Per :xref:`xref-ext`:

#. Add an entry to ``xref_links`` in ``conf.py``

   * Put in new links below the delimiter comment::

       # New links below, sorted links above

#. Add a link in documentation:

   * ``:xref:`xref-ext``` makes :xref:`xref-ext`
   * ``:xref:`Custom link <xref-ext>``` makes :xref:`Custom link <xref-ext>`

#. Add a description of the link to :ref:`References`

   * Now the link can be moved above the delimiter comment in ``conf.py``

.. Tip::
   Use a base url from ``url`` in ``conf.py`` for common references like
   YouTube videos

.. Note::
   As long as the delimiter comment is properly used, links can be sorted in
   batches


******************
Project management
******************

Building documentation
======================

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