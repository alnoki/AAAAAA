.. 0.3.0

.. _writing-procedures:


#######
Writing
#######

.. csv-table:: Select references
   :header: Reference, Topic
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
   * :guilabel:`View: New Editor Group to the Right`
   * :guilabel:`View: New Editor Group Below`
   * :guilabel:`View: Zoom In`
   * :guilabel:`View: Zoom Out`
   * :guilabel:`Workspaces: Duplicate Workspace in New Window`

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
   to have in your :ref:`tree <concepts-project-dir-tree>`
#. Update ``where_to_start`` to the :xref:`directory <directory>` that you
   would like to write about
#. Highlight the whole file
#. Use the :ref:`command palette <tools-vs-code>` to select
   :guilabel:`Python: Run Selection/Line in Python Terminal` then hit
   :kbd:`enter` from inside the
   :ref:`VS Code integrated terminal <tools-vs-code>`

.. _writing-new-topic:


***********************
Documenting a new topic
***********************

#. :ref:`Gather necessary references <sphinx-managing-references>` first,
   preferably in a batch

   * These should be concentrated at a centralized :term:`AAAAAA` conceptual
     explanation, usually at :ref:`tools <concepts-tools>`
   * Use a :ref:`csv-table <sphinx:table-directives>` of
     :ref:`references <references>` at the central conceptual explanation:

     .. code-block:: rest

        .. csv-table:: Select references
           :header: Reference, Topic
           :align: center

           :ref:`tools-vs-code`, Task management environment
           :ref:`concepts-project-dir-tree`, :term:`AAAAAA` project structure
           :xref:`Markdown`, Syntax specification
           :term:`OHIO`, Task management philosophy

#. Use a :ref:`reference label <concepts-documentation-style>` in
   documentation to refer to the core conceptual explanation

.. tip::

   Avoid creating identical documentation in several places that must be
   multiply maintained

Procedures
==========

#. Any new :ref:`procedures <procedures>` should be reciprocally
   cross-referenced with a conceptual explanation, using
   :ref:`reference tables <writing-new-topic>`

   #. The first row of the :ref:`reference table <writing-new-topic>` in the
      :ref:`procedure <procedures>` should be a
      :ref:`reference label <concepts-documentation-style>` for the conceptual
      explanation

      * Because the conceptual explanation should be the primary source of
        information when attempting the :ref:`procedure <procedures>`
      * The :ref:`topic column <writing-new-topic>` should say say
        ":term:`AAAAAA` conceptual explanation"

   #. The last row of the :ref:`reference table <writing-new-topic>` in the
      conceptual explanation should be a
      :ref:`reference label <concepts-documentation-style>` for the
      :ref:`procedure <procedures>`

      * Because :ref:`procedures <procedures>` should be attempted only after
        grasping conceptual explanations
      * The topic should say ":term:`AAAAAA` usage"

   .. csv-table:: Cross-referencing examples
      :header: :ref:`Procedure <procedures>`, Conceptual explanation
      :align: center

      :ref:`Git procedures <git-procedures>`, :ref:`Tools: Git <tools-git>`
      :ref:`Versioning procedures <versioning-procedures>`, :ref:`version-list`

#. :ref:`Add a new conda package <conda-use-new-package>` or update the
   :ref:`Sphinx extension table <tools-sphinx>`, for example, if it makes sense
   for your new :ref:`procedure <procedures>`

.. _writing-proofread:


**************************
Proofreading documentation
**************************

.. tip::

   :ref:`Read out loud <zen-aipaip>` in a marginally silly voice (to enhance
   your :ref:`enjoyment of the content <zen-spirit>`), and
   :ref:`go slow <zen-spirit>`

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

      * Even if you have moved an :ref:`.rst <tools-restructured-text>`
        document, :ref:`GitLens <tools-vs-code>` is
        often able to identify that it is in a new
        :xref:`directory <directory>` and will only display changes to the
        document (rather than classifying the document as new)

.. _writing-proofread-new:

New documents
=============

See :ref:`documentation style <concepts-documentation-style>` for a list of
things to watch out for

#. Put a :doc:`comment <usage/restructuredtext/basics>` at the top
   of the :ref:`.rst <tools-restructured-text>` document, to note the
   :ref:`current development branch version number <versioning-start-new>`

   .. code-block:: rest

      .. 0.3.0

      .. _doc-label:


      ###############
      Document header
      ###############

#. Open an :ref:`autobuild <sphinx-autobuilding>` in a
   :xref:`browser <web-browser>` alongside :ref:`tools-vs-code` with
   :ref:`maximum half-screen estate <writing-max-screen-estate>`, so you can
   make edits immediately
#. Go through one :ref:`minor section <concepts-documentation-example>` at a
   time

   #. Read the :xref:`browser <web-browser>`-rendered text
      :ref:`out loud <zen-aipaip>` and make any corrections in
      :ref:`tools-vs-code`
   #. Verify each :xref:`link <URL>` in the section by clicking on it

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
