.. _versioning-procedures:

##########
Versioning
##########

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`version-list`, :term:`AAAAAA` versions
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

#. Re-order the topics in a logically progressive development sequence
#. Develop with a similar treatment of items/topics

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
#. In :ref:`conf.py <tools-sphinx>` update
   :ref:`version numbers <version-list>` numbers (and potentially copyright)
#. Add an entry to the :ref:`version list <version-list>`

   * Document changes as you go, in a way that
     :xref:`tells the codebase what to do <commit-conventions>`

.. _versioning-releasing:


***********************
Releasing a new version
***********************

At this point you should be working on a
:ref:`development branch <versioning-start-new>`

#. :ref:`Update labels <sphinx-update-labels>`
#. Do a :ref:`link check <sphinx-checking-links>`

   * :ref:`End the active autobuild <sphinx-autobuilding>`
     (which should leave ghost content at its particular :xref:`URL <URL>`),
     then :ref:`serve a manual build <sphinx-building-manually>` for this,
     since each process has an associated :xref:`URL <URL>` that must be
     checked

#. Verify that the :ref:`quickstart <quickstart>` works
#. Verify and :ref:`update directory trees <writing-make-dir-tree>`

   * :ref:`AAAAAA <concepts-project-dir-tree>`
   * :ref:`Documentation <concepts-documentation-structure>`
   * :ref:`Jupyter Notebooks <concepts-jupyter-nbs-structure>`
   * :ref:`Code <concepts-code-structure>`

#. Finalize any updates to the :ref:`version list <version-list>`
#. :ref:`Isolate and proofread changes <writing-isolate-changes>` against the
   most recent :ref:`release <version-list>`

   * Once you start, go through from the first
     :ref:`.rst file <tools-restructured-text>` to the last, only making edits
     for the current :ref:`.rst file <tools-restructured-text>` you are on

#. Update the ``YYYY-MM-DD`` on the :ref:`version list <version-list>`
#. :ref:`Commit but do not push <git-committing>`
#. :ref:`Merge <git-merging>` the
   :ref:`development branch <versioning-start-new>` in to the
   :xref:`master branch <git-manual>`
#. :ref:`Tag and push <git-tagging>` with a
   :xref:`long message <git-commit-guidelines>` that describes the release
#. On your :doc:`Read the Docs<rtfd:index>` account:

   * :menuselection:`Projects --> AAAAAA --> Versions --> Inactive Versions --> X.Y.Z --> Edit --> Active`
