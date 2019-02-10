.. 41bbe32

.. _writing-procedures:

#######
Writing
#######

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`tools-vs-code`, :term:`AAAAAA` conceptual explanation

.. contents:: Contents
   :local:

.. _writing-max-screen-estate:


************************
Maximizing screen estate
************************

#. For half-screen, use the :ref:`VS Code command palette <tools-vs-code>`
   to experiment with the following commands:

   * :guilabel:`View: Toggle Tab Visibility`
   * :guilabel:`View: Toggle Maximized Panel`
   * :guilabel:`View: Toggle Panel`
   * :guilabel:`View: Toggle Activity Bar Visibility`
   * :guilabel:`View: Toggle Side Bar Visibility`
   * :guilabel:`View: Toggle Status Bar Visibility`
   * :guilabel:`View: Toggle Centered Layout`
   * :guilabel:`View: Join All Editor Groups`

#. For full-screen:

   * :guilabel:`View: Toggle Zen Mode`

.. _writing-make-dir-tree:


*************************
Creating a directory tree
*************************

Adapted from :xref:`directory tree sample code <print-dir-tree>`, to create the
:ref:`AAAAAA project tree <concepts-project-dir-tree>`:

#. Use the :ref:`VS Code command palette <tools-vs-code>` to select
   :guilabel:`File: New Untitled File`
#. Copy-paste the below contents to the new file:

   .. code-block:: python

      import os

      base_indent = 4 * ' '
      branch_symbol = '|-> '
      where_to_start = '/Users/alnoki/Code/AAAAAA'

      for root, dirs, files in os.walk(where_to_start):
          level = root.replace(where_to_start, '').count(os.sep)
          if level > 0:
              indent = base_indent * (level - 1) + branch_symbol
          else:
              indent = ''
          print(f'{indent}{os.path.basename(root)}/')
          subindent = base_indent * (level) + branch_symbol
          for f in files:
              print(f'{subindent}{f}')

#. Modify ``base_indent`` and ``branch_symbol`` to symbols that you would like
   to have in your tree
#. Update ``where_to_start`` to the :xref:`directory <directory>` that you
   would like to write about
#. Highlight the text in the scratch file
#. Use the :ref:`command palette <tools-vs-code>` to select
   :guilabel:`Python: Run Selection/Line in Python Terminal` then hit
   :kbd:`enter` from inside the
   :ref:`VS Code integrated terminal <tools-vs-code>`


***********************
Documenting a new topic
***********************

#. Gather :ref:`references <sphinx-managing-references>` first, preferably in a
   batch
#. Add a descripion of any :ref:`links <references-links>` or
   :ref:`books <references-books>` to :ref:`references <references>`
#. Use the new :ref:`reference <references>` in documentation
#. When appropriate, link to :ref:`tools <concepts-tools>` or other similar
   documentation pages that have already been created rather than creating a
   new :ref:`link <references-links>` outside of :term:`AAAAAA`

.. tip::

   Avoid creating identical documentation in several places that must be
   multiply maintained

.. _writing-proofread:


**************************
Proofreading documentation
**************************

.. _writing-isolate-changes:

Isolating changes
=================

This is typically done right before
:ref:`releasing a version <versioning-releasing>`

#. Use the :ref:`VS Code command palette <tools-vs-code>` to
   :guilabel:`GitLens: Compare Working Tree with Branch or Tag...`
#. Select the :ref:`tag <git-tagging>` of the relevant
   :ref:`version <version-list>` to compare against
#. Proofread :ref:`new documents <writing-proofread-new>` and
   :ref:`changed documents <writing-proofread-changed>`

.. tip::

   Even if you have moved a document, :ref:`GitLens <tools-vs-code>` is often
   able to identify that it is in a new :xref:`directory <directory>` and will
   only display changes to the document (rather than classifying the document
   as new)

.. _writing-proofread-new:

New documents
=============

See :ref:`documentation style <concepts-documentation-style>` for a list of
things to watch out for

#. Open a :ref:`live build <sphinx-building-documentation>` in a browser
   alongside :ref:`tools-vs-code` with
   :ref:`maximum half-screen estate <writing-max-screen-estate>`, so you can
   make edits immediately
#. Go through one :ref:`minor section <concepts-documentation-example>` at a
   time

   #. Read the browser-rendered text out loud and make any corrections in
      :ref:`tools-vs-code`, then try a
      :ref:`new build <sphinx-building-documentation>`
   #. Verify each link in the section by clicking on it

#. Do a :ref:`linkcheck <sphinx-checking-links>`
#. When done proofreading an :ref:`.rst file <tools-restructured-text>`, tag
   the top with a :doc:`comment <usage/restructuredtext/basics>` that matches
   the :ref:`current development branch version number <versioning-start-new>`

   .. code-block:: rest

      .. 0.3.0

      .. _doc-label:


      ###############
      Document header
      ###############

.. _writing-proofread-changed:

Changes to a document
=====================

#. Use :ref:`GitLens <tools-vs-code>` to inspect the history of the
   file: :guilabel:`GitLens: Show File History`
#. The :ref:`version comment <concepts-documentation-example>` at the top of
   the file should identify the most-recent :ref:`version <version-list>` for
   which the document was reviewed. Thus:

   #. Use the :guilabel:`GitLens: Show File History`
      view to :guilabel:`Choose from Branch or Tag History...`
   #. Select the :ref:`tag <git-tagging>` that corresponds to the
      :ref:`version comment <concepts-documentation-example>`
   #. Select the first :ref:`commit <tools-git>` in the list
   #. :guilabel:`Open Changes with Working File`

   .. tip::

      If there is a warning that the document did not exist for that
      :ref:`tag <git-tagging>`, then the document was probably moved

#. Follow the steps for
   :ref:`proofreading new documents <writing-proofread-new>`, but only review
   *changes* to the document:

      * Use the :ref:`VS Code command palette <tools-vs-code>` to select
        :guilabel:`Move to Next Change`
