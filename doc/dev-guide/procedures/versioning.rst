.. 0.3.0

.. _versioning-procedures:


##########
Versioning
##########

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`version-list`, Conceptual explanation
   :ref:`tools-git`, :ref:`Version <version-list>` identification
   :ref:`tools-read-the-docs`, Automated :ref:`version <version-list>` support


.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`semver`, Numbering standards
   :xref:`git-commit-guidelines`, Long version message guidelines

.. contents:: Contents
   :local:

.. _versioning-td3:

***************************************************
Top-down to-do task deferral (TD)\ :superscript:`3`
***************************************************

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, topic

   :term:`OHIO`, Task management philosophy
   :ref:`tools-vs-code`, Task management environment
   :ref:`Project structure <concepts-project-tree>`, Layout

.. csv-table:: Select reference
   :align: center
   :header: Reference, Topic

   :github-help:`Markdown <basic-writing-and-formatting-syntax>`, "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` specification"

.. tip::

   Chant :term:`OHIO` while doing this

#. Open :ref:`TODO.md <concepts-project-tree>` in :ref:`tools-vs-code`
#. From the :ref:`command palette <tools-vs-code>`:

   * :guilabel:`View: Open View`
   * :guilabel:`Outline`

   .. csv-table::
      :github-help:`Markdown headers <basic-writing-and-formatting-syntax>`
      :align: center
      :header: Level, Meaning

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
#. In :ref:`conf.py <configs-conf-py>`, update
   :ref:`version numbers <version-list>` (and potentially
   :wiki-pg:`copyright <Copyright>`)
#. Add an entry to the :ref:`version list <version-list>`

   * :wiki-pg:`Document <Software_documentation>` changes as you go, in a way
     that :xref:`tells the codebase what to do <commit-conventions>`

#. :ref:`Tidy up conda <conda-tidy-up>`
#. :ref:`versioning-td3`
#. After you :ref:`push <git-committing>`, :ref:`enable <dist-doc-versions>`
   the :ref:`development branch <git-branching>` on your :xref:`rtfd-account`

.. _versioning-releasing:


***********************
Releasing a new version
***********************

At this point you should be working on a
:ref:`development branch <versioning-start-new>`

#. Update descriptions of any modified :ref:`configurations <concepts-configs>`
#. :ref:`Update labels <sphinx-update-labels>`
#. Do a :ref:`link check <sphinx-checking-links>`
#. Verify that the :ref:`quickstart <quickstart>` works
#. Verify and :ref:`update directory trees <writing-make-dir-tree>`

   * :ref:`AAAAAA <concepts-project-tree>`
   * :ref:`Documentation <concepts-doc-tree>`
   * :ref:`Jupyter Notebooks <concepts-jupyter-nbs-tree>`
   * :ref:`Code <concepts-code-tree>`
   * :ref:`Configurations <concepts-configs-tree>`

#. Finalize feature additions in the :ref:`version list <version-list>`
#. :ref:`Isolate and proofread changes <writing-isolate-changes>` against the
   most recent :ref:`release <version-list>`

   * :term:`OHIO` from the first :ref:`.rst file <tools-restructured-text>` to
     the last, editing only the
     :ref:`.rst file <tools-restructured-text>` you are on
   * Feel free to add some :ref:`to-dos <versioning-td3>` for later, though

#. Update the :wiki-pg:`time <Time>` on the :ref:`version list <version-list>`
#. :ref:`Commit and push <git-committing>`, making sure to verify
   :ref:`version tag comments <writing-proofread-new>` when
   :ref:`staging changes <git-committing>`
#. Verify the :ref:`build passes <dist-doc-monitor-builds>` on your
   :xref:`rtfd-account`
#. :ref:`Merge <git-merging>` the
   :ref:`development branch <versioning-start-new>` in to the
   :xref:`master branch <git-manual>`
#. :ref:`Tag and push <git-tagging>` with a
   :xref:`long message <git-commit-guidelines>` that describes the
   :ref:`version list additions <version-list>`
#. Use your :xref:`rtfd-account` to :ref:`disable <dist-doc-versions>` the
   :ref:`development branch <git-branching>` and
   :ref:`enable <dist-doc-versions>` the new :ref:`tag <git-tagging>`
