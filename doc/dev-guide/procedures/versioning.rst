.. _procedures-versioning:


##########
Versioning
##########

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`indices-versions`, Conceptual explanation
   :ref:`tools-git`, :ref:`Version <indices-versions>` identification
   :ref:`tools-read-the-docs`, "Automated
   :ref:`version <indices-versions>` support"
   :ref:`Distributing documentation <dist-doc>`, Walkthrough


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

.. tip::

   Chant :term:`OHIO` while doing this

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, topic

   :term:`OHIO`, Task management philosophy
   :ref:`tools-vs-code`, Task management environment
   :ref:`Project structure <concepts-project-tree>`, Layout
   :ref:`vs-code-markdown-headers`, "
   :ref:`VS Code procedure <procedures-vs-code>`"

.. csv-table::
   :github-help:`Markdown headers <basic-writing-and-formatting-syntax>` in
      :ref:`TODO.md <concepts-project-tree>`
   :align: center
   :header: Level, Meaning

   ``#``, :ref:`Versions <indices-versions>`
   ``##``, ``Topic``
   ``*``, ``Item``

#. Open :ref:`TODO.md <concepts-project-tree>` in :ref:`tools-vs-code`
#. Identify if the planned ``topic`` set is too much for one
   :ref:`version <indices-versions>`
#. Starting with the topmost ``topic`` for the current
   :ref:`version <indices-versions>`:

   * Either defer the ``topic`` to the next :ref:`version <indices-versions>`
     or move it to the bottom of the set for the current
     :ref:`version <indices-versions>`
   * Repeat until the ``topic`` that you started with is back at the top of the
     set for the current :ref:`version <indices-versions>`

#. Re-order the ``topics`` in a logically progressive
   :wiki-pg:`development <Software_development>` sequence
#. :wiki-pg:`Develop <Software_development>` with a similar treatment of
   ``items``/``topics``

   * Start at the top and work your way down
   * Re-ordering shouldn't be necessary
   * Either defer the ``item`` to a future :ref:`version <indices-versions>` or
     complete it before moving on

.. _versioning-start-new:


**********************
Starting a new version
**********************

#. Create a new :ref:`development branch <git-branching>` named in accordance
   with :xref:`semantic versioning standards <semver>`:
   ``dev/MAJOR.MINOR.PATCH``
#. In :ref:`conf.py <configs-conf-py>`, update
   :ref:`version numbers <indices-versions>` (and potentially
   :wiki-pg:`copyright <Copyright>`)
#. Add an entry to the :ref:`version feature list <versions-features>`

   * :wiki-pg:`Document <Software_documentation>` changes as you go, in a way
     that :xref:`tells the codebase what to do <commit-conventions>`

#. Update the :ref:`commit statistics <git-get-commit-stats>` and other data
   for the :ref:`version <versions-features>` that was just
   :ref:`released <versioning-releasing>` at:

   * The :wiki-pg:`UTC <Coordinated_Universal_Time>` on the
     :ref:`version feature list <versions-features>`
   * :ref:`version-stats.ipynb <concepts-nbs-tree>`
   * Verify the :ref:`version statistics <versions-stats>`

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

#. Verify that the :ref:`quickstart <quickstart>` works
#. Verify and :ref:`update directory trees <writing-make-dir-tree>`

   * :ref:`AAAAAA <concepts-project-tree>`
   * :ref:`Documentation <concepts-doc-tree>`
   * :ref:`Jupyter Notebooks <concepts-nbs-tree>`
   * :ref:`Code <concepts-code-tree>`
   * :ref:`Configurations <concepts-configs-tree>`
#. Update descriptions of any modified :ref:`configurations <concepts-configs>`
#. :ref:`Update labels <sphinx-update-labels>`
#. Organize :ref:`links <references-links>` so there are at most 10
   :wiki-pg:`URLs <URL>` per
   :doc:`list <sphinx:usage/restructuredtext/basics>`
#. Finalize :ref:`version feature additions <versions-features>`
#. :ref:`Isolate and proofread changes <writing-isolate-changes>` against the
   most recent :ref:`release <indices-versions>`

   * :term:`OHIO` from the first :ref:`.rst file <tools-restructured-text>` to
     the last in the order specified by :guilabel:`next`

#. Do a :ref:`link check <sphinx-checking-links>`
#. :ref:`git-get-commit-stats` and update:

   * The :wiki-pg:`date and time <Time>` on the
     :ref:`version feature list <versions-features>` with ``00:00:00Z``
   * Data for the :ref:`version <versions-features>` at
     :ref:`version-stats.ipynb <concepts-nbs-tree>`

     * Increment the :ref:`commit number <git-get-commit-stats>` from the
       :ref:`commit statistics <git-get-commit-stats>` by 1
     * :menuselection:`Kernel -> Restart & Run All`
     * Verify the :ref:`version statistics <versions-stats>`

#. :ref:`Commit and push <git-committing>`
#. Verify the :ref:`build passes <dist-doc-monitor-builds>` on your
   :xref:`rtfd-account`
#. :ref:`Merge <git-merging>` the
   :ref:`development branch <versioning-start-new>` in to the
   :git-doc:`master branch <user-manual>`
#. :ref:`Tag and push <git-tagging>` with a
   :xref:`long message <git-commit-guidelines>` that describes the
   :ref:`version list additions <indices-versions>`
#. Use your :xref:`rtfd-account` to :ref:`disable <dist-doc-versions>` the
   :ref:`development branch <git-branching>` and
   :ref:`enable <dist-doc-versions>` the new :ref:`tag <git-tagging>`
