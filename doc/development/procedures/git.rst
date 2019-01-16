###
Git
###

.. _git-credentials:


*************************
Updating user credentials
*************************

Per the :xref:`git-manual`:

#. Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` to enter
   (adapted for your name and email address):

   .. code-block:: bash

      git config --global user.name 'alnoki'
      git config --global user.email '43892045+alnoki@users.noreply.github.com'

#. To check that the credentials have updated:

   .. code-block:: bash

      git config --global --list

.. _list-committers:


***********************
List project committers
***********************

See

* :xref:`list-git-developers`
* :xref:`git-log-formatting`

#. Inspect unique :xref:`commit credentials <git-manual>` with any of the
   following single commands in the
   :xref:`VS Code integrated terminal <VS-Code-terminal>`:

   .. code-block:: bash

      git log --pretty=format:"Author name: %an" | sort | uniq
      git log --pretty=format:"Author email: %ae" | sort | uniq
      git log --pretty=format:"Committer name: %cn" | sort | uniq
      git log --pretty=format:"Committer email: %ce" | sort | uniq

#. Inspect all of these fields at once, for the entire project history, via:

   .. code-block:: bash

      git log --pretty=format:"%an, %ae, %cn, %ce"

.. _committing:


**********
Committing
**********

Per the :xref:`git-manual`:

#. Verify the state of the project using the
   :xref:`VS Code integrated terminal <VS-Code-terminal>`:

   .. code-block:: bash

      git pull
      git log

#. Save and close any open project files
#. Verify your :ref:`Git user credentials <git-credentials>`, update as needed
#. Use the :xref:`VS Code command palette <command-palette>` to select

   * :guilabel:`View: Open View`
   * :guilabel:`Source Control`

#. Use the :guilabel:`Source Control` interface to
   :xref:`stage changes <git-manual>` and to create a
   :xref:`commit message <git-manual>`
#. In the :xref:`command palette <command-palette>`:
   :guilabel:`Git: Commit Staged`

#. Use the :xref:`VS-Code-terminal` to verify the :xref:`commit <git-manual>`
   looks alright, and that the :ref:`commit identities <list-committers>` are
   okay:

   .. code-block:: bash

      git log
      git log --pretty=format:"%an, %ae, %cn, %ce"

#. In the :xref:`command palette <command-palette>`:
   :guilabel:`Git: Push`
#. Verify results at the :xref:`AAAAAA-repo`

.. _change-commit-credential-history:


********************************
Change commit credential history
********************************

See

* :xref:`github-change-authors`
* :xref:`git-branch-filtering`

#. For the most part, follow :xref:`github-change-authors`. Before you
   :xref:`push the corrected history <github-change-authors>`, check out the
   updated :ref:`commit credential history <list-committers>`:

   .. code-block:: bash

      git log --pretty=format:"%an, %ae, %cn, %ce"

#. If you forget to :ref:`update your user credentials <git-credentials>`
   before :ref:`committing and pushing <committing>` (a whole bunch of times),
   use:

   .. code-block:: bash

      #!/bin/sh

      git filter-branch --env-filter '
      CORRECT_NAME="alnoki"
      CORRECT_EMAIL="43892045+alnoki@users.noreply.github.com"
      if [ "$GIT_AUTHOR_EMAIL" != "$CORRECT_EMAIL" ]
      then
          export GIT_AUTHOR_NAME="$CORRECT_NAME"
          export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
          export GIT_COMMITTER_NAME="$CORRECT_NAME"
          export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
      fi
      ' --tag-name-filter cat -- --branches --tags

   * This will update all :ref:`project commit credentials <list-committers>`
     that were not authored by ``43892045+alnoki@users.noreply.github.com``

#. If you want to get more specific about your selections:

   .. code-block:: bash

      #!/bin/sh

      git filter-branch --env-filter '
      OLD_NAME="Some d00d"
      OLD_NAME2="ikonla"
      OLD_EMAIL="not_alnoki@interweb.com"
      OLD_EMAIL2="d00000000d@l33t.com"
      CORRECT_NAME="alnoki"
      CORRECT_EMAIL="43892045+alnoki@users.noreply.github.com"
      if [ "$GIT_AUTHOR_NAME" = "$OLD_NAME" ] ||
         [ "$GIT_AUTHOR_NAME" = "$OLD_NAME2" ]
      then
          export GIT_AUTHOR_NAME="$CORRECT_NAME"
          export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
      fi
      if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ] ||
         [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL2" ]
      then
          export GIT_COMMITTER_NAME="$CORRECT_NAME"
          export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
      fi
      ' --tag-name-filter cat -- --branches --tags

