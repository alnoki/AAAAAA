######
Sphinx
######


*******************
Managing references
*******************

.. _intersphinx-linking:

Using Intersphinx
=================

Per :std:doc:`Intersphinx documentation <sphinx:usage/extensions/intersphinx>`:

#. Add the project's root url to
   :std:doc:`conf.py <sphinx:usage/configuration>`::

    intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'sphinx': ('http://www.sphinx-doc.org/en/master/', None),
       'pytest': ('https://docs.pytest.org/en/latest/', None),
       'rtfd': ('https://docs.readthedocs.io/en/latest/', None),
       'rtd-sphinx-theme':
          ('https://sphinx-rtd-theme.readthedocs.io/en/latest/', None),
       ...

#. Inspect the :std:doc:`objects.inv <sphinx:usage/extensions/intersphinx>`
   mapping, usually located under the root, via

   :command:`python -msphinx.ext.intersphinx http://www.sphinx-doc.org/objects.inv`

   * Try this in a terminal that can be maximized to full screen
   * Most times the root will be at ``.io/en/latest/`` or ``.com/en/latest``
   * Consider an :xref:`intersphinx-inv-parser` for large outputs

#. Locate the desired target in the mapping output, which is arranged like the
   project's table of contents. For example, ``usage/extensions/intersphinx``
   is located in the ``std:doc`` section of the output from the above command

   * See :xref:`intersphinx-inv-targets` for a formatting explanation
   * Most documentation pages will be in ``std:doc``

#. Link to the reference using syntax from the
   :std:doc:`Intersphinx documentation <sphinx:usage/extensions/intersphinx>`
   and (for archival purposes) add a description of the link to
   :ref:`references`

   * To use the default text from the reference, rendered as
     :std:doc:`sphinx:usage/extensions/intersphinx`, use:

     .. code-block:: rest

         :std:doc:`sphinx:usage/extensions/intersphinx`

   * To create your own custom text, rendered as
     :std:doc:`Custom <sphinx:usage/extensions/intersphinx>`, use:

     .. code-block:: rest

         :std:doc:`Custom <sphinx:usage/extensions/intersphinx>`

.. Note::
   See :xref:`intersphinx-numpy-matplotlib` instructions for these specific
   cases

.. _xref-linking:

Referencing external links
==========================

The :xref:`Sphinx xref extension <xref-ext>` is installed like other
:std:doc:`built-in Sphinx extensions<sphinx:usage/extensions/index>`, with some
installation tips taken from a related
:ref:`references extension configuration manual <sublime-with-sphinx:use the external links extension>`

Usage instructions are per :xref:`xref-ext`:

#. Add a reference to the link in
   :std:doc:`conf.py <sphinx:usage/configuration>`

   * If the link has a common base link, like in a
     :xref:`YouTube video <YouTube>`, add it too::

       # Base urls used by xrefs extension
       url = {
          'GitHub': 'https://github.com/',
          'YT vid': 'https://www.youtube.com/watch?v=',  # Video
          ...

   * Put in new links below the delimiter comment::

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

#. Link to the reference using syntax similar to the
   :std:doc:`Intersphinx documentation <sphinx:usage/extensions/intersphinx>`

   * To use the default text from the reference, rendered as
     :xref:`xref-ext`, use:

     .. code-block:: rest

         :xref:`xref-ext`

   * To create your own custom text, rendered as
     :xref:`Custom link <xref-ext>`, use:

     .. code-block:: rest

         :xref:`Custom link <xref-ext>`

#. Add a description of the link to :ref:`references`

   * After this step, the link can be moved above the delimiter comment in
     :std:doc:`conf.py <sphinx:usage/configuration>`

.. Tip::
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

   * :command:`make html` to create new documentation files
   * :command:`python -m http.server` to start running a website server
   * Just start one server, lest you incur an :xref:`http-socket-error`

#. Open http://localhost:8000/_build/html/index.html in a browser

   * Refresh after making a new build to load the changes

#. :command:`make clean` to clear out old build files before committing

.. Tip::
   Run :command:`make linkcheck` occasionally to verify that links in the
   project reference valid locations
