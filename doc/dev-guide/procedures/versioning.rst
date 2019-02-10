.. _versioning-procedures:

##########
Versioning
##########

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :xref:`semver`, Numbering standards
   :ref:`version-list`, :term:`AAAAAA` versions
   :xref:`git-commit-guidelines`, Long version message guidelines

.. contents:: Contents
   :local:

.. _versioning-start-new:


**********************
Starting a new version
**********************

#. Create a new :ref:`development branch <git-branching>` named in accordance
   with :xref:`semantic versioning standards <semver>`:
   ``dev/MAJOR.MINOR.PATCH``
#. Update :ref:`conf.py <tools-sphinx>` version numbers
#. Add an entry to the :ref:`version list <version-list>`

   * Document changes as you go, in language that
     :xref:`tells the codebase what to do <commit-conventions>`


***********************
Releasing a new version
***********************

At this point you should be working on a
:ref:`development branch <versioning-start-new>`

#. Do a :ref:`link check <sphinx-checking-links>`
#. :ref:`Update labels <sphinx-update-labels>`
#. Verify that the :ref:`quickstart <quickstart>` works
#. Finalize any updates to the :ref:`version list <version-list>`
#. :ref:`Commit but do not push <git-committing>`
#. :ref:`Merge <git-merging>` the
   :ref:`development branch <versioning-start-new>` in to the
   :xref:`master branch <git-manual>`
#. :ref:`Tag and push <git-tagging>` with a
   :xref:`long message <git-commit-guidelines>` that describes the release
