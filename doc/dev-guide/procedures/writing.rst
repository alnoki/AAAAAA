.. 0.3.0

.. _procedures-writing:


#######
Writing
#######

.. _writing-make-dir-tree:


*************************
Creating a directory tree
*************************

Adapted from :xref:`directory tree sample code <print-dir-tree>`, to create the
:ref:`AAAAAA project tree <concepts-project-tree>`:

#. Use the :ref:`VS Code Command Palette <tools-vs-code>` to select
   :guilabel:`File: New Untitled File`
#. :wiki-pg:`Copy and paste <Cut,_copy,_and_paste>` the below contents to the
   new :wiki-pg:`file <Computer_file>`:

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
   to have in your :ref:`tree <concepts-project-tree>`
#. Update ``where_to_start`` to the :xref:`directory <directory>` that you
   would like to write about
#. Select all the :wiki-pg:`line <Line_(text_file)>` in the
   :wiki-pg:`file <Computer_file>`
#. Use the :ref:`Command Palette <tools-vs-code>` to select
   :guilabel:`Python: Run Selection/Line in Python Terminal` then
   :wiki-pg:`type <Typing>` :kbd:`enter` from inside the
   :ref:`VS Code integrated terminal <tools-vs-code>`

.. _writing-new-topic:


***********************
Documenting a new topic
***********************

#. :ref:`Gather necessary references <sphinx-managing-references>` first,
   preferably in a batch

   * These should be concentrated at a centralized :term:`AAAAAA` conceptual
     explanation, usually at :ref:`tools <concepts-tools>`
   * Use 2 :ref:`csv-tables <sphinx:table-directives>` of
     :ref:`references <references>` at the central conceptual explanation

     * The first containing :wiki-pg:`links <URL>` within :term:`AAAAAA`

       * See :ref:`tools-sphinx` for sample priority and nomenclature

     * The second containing other :ref:`references <references>`

     .. code-block:: rest

        .. csv-table:: Select references within :term:`AAAAAA`
           :align: center
           :header: Reference, Topic

           :ref:`Developer environment <dev-env-intro>`, Setup
           :ref:`Sphinx configuration <configs-sphinx>`, Options
           :ref:`Sphinx procedures <procedures-sphinx>`, Usage
           ...

        .. csv-table:: Select references
           :align: center
           :header: Reference, Topic

           :doc:`Sphinx <sphinx:intro>`, "Official
           :wiki-pg:`documentation <Software_documentation>`"
           ...

#. Use a :ref:`reference label <concepts-doc-style>` in
   :ref:`.rst files <tools-restructured-text>` to refer to the core conceptual
   explanation
#. Update any relevant ``index.rst`` :ref:`toctree <sphinx:toctree-directive>`
   descriptions, and potentially the :ref:`what next? <what-next>` section

.. tip::

   Avoid creating identical :wiki-pg:`documentation <Software_documentation>`
   in several places that must be multiply maintained

Tools satellite topics
======================

#. Any new :ref:`tools <concepts-tools>` satellite topics, like
   :ref:`configurations <concepts-configs>` or :ref:`procedures <procedures>`,
   should be reciprocally cross-referenced with a conceptual explanation, using
   :ref:`reference tables <writing-new-topic>`
#. The new satellite topic should have at least a
   :ref:`reference table <writing-new-topic>` with one :wiki-pg:`link <URL>`
   to a conceptual description in :term:`AAAAAA`

   .. code-block:: rest

      .. csv-table:: Select reference within :term:`AAAAAA`
         :align: center
         :header: Reference, Topic

         :ref:`tools-vs-code`, Conceptual explanation

#. If including other :ref:`references <references>` outside of :term:`AAAAAA`,
   add a :ref:`second references table <writing-new-topic>` to the satellite
   topic
#. At the :ref:`tools section <concepts-tools>`, add a :wiki-pg:`link <URL>`
   to the satellite topic
#. :ref:`Add a new conda package <conda-use-new-package>` or update the
   :ref:`Sphinx extension table <tools-sphinx-extensions>`, for example, if it
   makes sense for your new topic

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

#. Use the :ref:`VS Code Command Palette <tools-vs-code>` to
   :guilabel:`GitLens: Compare Working Tree with Branch or Tag...`
#. Select the :ref:`tag <git-tagging>` of the relevant
   :ref:`version <indices-versions>` to compare against
#. Proofread :ref:`new documents <writing-proofread-new>` and
   :ref:`changed documents <writing-proofread-changed>`

      * Even if you have moved an :ref:`.rst file <tools-restructured-text>`,
        :ref:`GitLens <tools-vs-code>` is often able to identify that it is in
        a new :xref:`directory <directory>` and will only display changes to
        the :wiki-pg:`file <Computer_file>` (rather than classify it as new)

.. _writing-proofread-new:

New documents
=============

See :ref:`documentation style <concepts-doc-style>` for a list of things to
watch out for

#. Put a :doc:`comment <usage/restructuredtext/basics>` at the top
   of the :ref:`.rst file <tools-restructured-text>`, to note the
   :ref:`current development branch version number <versioning-start-new>`

   .. code-block:: rest

      .. 0.3.0

      .. _doc-label:


      ###############
      Document header
      ###############

#. Open an :ref:`autobuild <sphinx-autobuilding>` in a
   :xref:`browser <web-browser>` alongside :ref:`tools-vs-code` with
   :ref:`maximum half-screen estate <vs-code-max-screen-estate>`, so you can
   make edits immediately
#. Go through one :ref:`minor section <concepts-doc-example>` at a time

   #. :wiki-pg:`Clear your browser history <Web_browsing_history>` so you can
      tell which :wiki-pg:`URLs <URL>` to :wiki-pg:`click <Point_and_click>`
   #. Read, :ref:`out loud <zen-aipaip>`, the :wiki-pg:`webpage <Webpage>` that
      is :wiki-pg:`rendered <Rendering_(computer_graphics)>` by your
      :xref:`browser <web-browser>` and make any corrections in
      :ref:`tools-vs-code`
   #. Verify each :xref:`link <URL>` in the section by
      :wiki-pg:`clicking <Point_and_click>` on it
   #. Review parts of the :ref:`.rst file <tools-restructured-text>` that do
      not show up as :wiki-pg:`white <Web_colors>` in the
      :ref:`RST preview extension <tools-vs-code>`
   #. When you see :term:`AAAAAA` in the :wiki-pg:`webpage <Webpage>`, read it
      :ref:`out loud <zen-aipaip>` as *alnoki's apps*:

      .. csv-table:: Grammar
         :align: center
         :header: Yes, NO!!!

         :term:`AAAAAA` **are** splendid, :term:`AAAAAA` **is** doomed

.. _writing-proofread-changed:

Changes to a document
=====================

#. Use :ref:`GitLens <tools-vs-code>` to inspect the history of the
   file: :guilabel:`GitLens: Show File History`
#. The :ref:`version comment <concepts-doc-example>` at the top of the
   :wiki-pg:`file <Computer_file>` should identify the
   :wiki-pg:`most-recent <Time>` :ref:`version <indices-versions>` for which
   the :wiki-pg:`file <Computer_file>` was reviewed. Thus:

   #. Use the :guilabel:`GitLens: Show File History`
      view to :guilabel:`Choose from Branch or Tag History...`
   #. Select the :ref:`tag <git-tagging>` that corresponds to the
      :ref:`version comment <concepts-doc-example>`
   #. Select the first :ref:`commit <tools-git>` in the list
   #. :guilabel:`Open Changes with Working File`

   .. tip::

      If there is a warning that the :wiki-pg:`file <Computer_file>` did not
      exist for that :ref:`tag <git-tagging>`, then the
      :wiki-pg:`file <Computer_file>` was probably moved

#. Follow the steps for
   :ref:`proofreading new documents <writing-proofread-new>`, but only review
   *changes* to the :wiki-pg:`file <Computer_file>`:

      * Use the :ref:`VS Code Command Palette <tools-vs-code>` to select
        :guilabel:`Move to Next Change`
