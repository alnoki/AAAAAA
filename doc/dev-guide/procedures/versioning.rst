.. 0.3.0

.. _versioning-procedures:


##########
Versioning
##########

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`version-list`, :term:`AAAAAA` conceptual explanation
   :xref:`semver`, Numbering standards
   :xref:`git-commit-guidelines`, Long version message guidelines
   :ref:`tools-read-the-docs`, Automated :ref:`version <version-list>` support
   :ref:`tools-git`, :ref:`Version <version-list>` identification

.. contents:: Contents
   :local:

.. _versioning-td3:

***************************************************
Top-down to-do task deferral (TD)\ :superscript:`3`
***************************************************

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-vs-code`, Task management environment
   :ref:`concepts-project-dir-tree`, :term:`AAAAAA` project structure
   :xref:`Markdown`, Syntax specification
   :term:`OHIO`, Task management philosophy

.. tip::

   Chant :term:`OHIO` while doing this

#. Open :ref:`TODO.md <concepts-project-dir-tree>` in :ref:`tools-vs-code`
#. From the :ref:`command palette <tools-vs-code>`:

   * :guilabel:`View: Open View`
   * :guilabel:`Outline`

   .. csv-table:: :xref:`Markdown headers <Markdown>`
      :header: Level, Meaning
      :align: center

      ``#``, :ref:`Versions <version-list>`
      ``##``, Topic
      ``1.``, Item

#. Identify if the planned topic set is too much for one
   :ref:`version <version-list>`
#. Starting with the topmost topic for the current
   :ref:`version <version-list>`:

   * Either defer the topic to the next :ref:`version <version-list>` or
     move it to the bottom of the set for the current
     :ref:`version <version-list>`
   * Repeat until the topic that you started with is back at the top of the set
     for the current :ref:`version <version-list>`

#. Re-order the topics in a logically progressive
   :wiki-pg:`development <Software_development>` sequence
#. :wiki-pg:`Develop <Software_development>` with a similar treatment of
   items/topics

   * Start at the top and work your way down
   * Re-ordering shouldn't be necessary
   * Either defer the item to a future :ref:`version <version-list>` or
     complete it before moving on

.. _versioning-start-new:


**********************
Starting a new version
**********************

#. Create a new :ref:`development branch <git-branching>` named in accordance
   with :xref:`semantic versioning standards <semver>`:
   ``dev/MAJOR.MINOR.PATCH``
#. In :ref:`conf.py <concepts-documentation-structure>`, update
   :ref:`version numbers <version-list>` (and potentially copyright year)
#. Add an entry to the :ref:`version list <version-list>`

   * :wiki-pg:`Document <Software_documentation>` changes as you go, in a way
     that :xref:`tells the codebase what to do <commit-conventions>`

#. :ref:`Tidy up conda <conda-tidy-up>`
#. :ref:`versioning-td3`

.. _versioning-releasing:


***********************
Releasing a new version
***********************

At this point you should be working on a
:ref:`development branch <versioning-start-new>`

#. :ref:`Update labels <sphinx-update-labels>`
#. Do a :ref:`link check <sphinx-checking-links>`
#. Verify that the :ref:`quickstart <quickstart>` works
#. Verify and :ref:`update directory trees <writing-make-dir-tree>`

   * :ref:`AAAAAA <concepts-project-dir-tree>`
   * :ref:`Documentation <concepts-documentation-structure>`
   * :ref:`Jupyter Notebooks <concepts-jupyter-nbs-structure>`
   * :ref:`Code <concepts-code-structure>`

#. Finalize feature additions in the :ref:`version list <version-list>`
#. :ref:`Isolate and proofread changes <writing-isolate-changes>` against the
   most recent :ref:`release <version-list>`

   * :term:`OHIO` from the first :ref:`.rst file <tools-restructured-text>` to
     the last, editing only the
     :ref:`.rst file <tools-restructured-text>` you are on
   * Feel free to add some :ref:`to-dos <versioning-td3>` for later, though

#. Update the ``YYYY-MM-DD`` on the :ref:`version list <version-list>`
#. :ref:`Commit and push <git-committing>`, making sure to verify
   :ref:`version tag comments <writing-proofread-new>` when
   :ref:`staging changes <git-committing>`
#. :ref:`Merge <git-merging>` the
   :ref:`development branch <versioning-start-new>` in to the
   :xref:`master branch <git-manual>`
#. :ref:`Tag and push <git-tagging>` with a
   :xref:`long message <git-commit-guidelines>` that describes the
   :ref:`version <version-list>`
#. In :doc:`Read the Docs<rtfd:index>`:

   * :menuselection:`Projects --> AAAAAA --> Versions --> Inactive Versions
     --> MAJOR.MINOR.PATCH --> Edit --> Active`
