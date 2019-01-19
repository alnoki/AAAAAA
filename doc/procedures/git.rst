.. _git-procedures:


###
Git
###

   .. csv-table:: Select references
      :header: "Reference", "Topic"
      :align: center

      :xref:`git-manual`, Quick practical reference
      :xref:`git-book`, In-depth conceptual explanations

.. contents::

.. _git-setup:


*****
Setup
*****

Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` for first-time
:xref:`git-setup`:

#. Configure your identity:

   .. code-block:: bash

      git config --global user.name alnoki
      git config --global user.email 43892045+alnoki@users.noreply.github.com

#. Set :xref:`Vim` as the default editor and use it to verify your identity:

   .. code-block:: bash

      git config --global core.editor Vim
      git config --global -e

#. At this point, you will be in the :xref:`Vim`. If you your identity looks
   right, you can :xref:`exit without saving <Vim-cheatsheet>` by typing
   ``:q!`` then :kbd:`return`

.. csv-table:: Learning :xref:`Vim`
   :header: "Reference", "Topic"
   :align: center

   :xref:`Vim-tutorial`, Learn :xref:`Vim` quickly
   :xref:`Vim-cheatsheet`, Common commands

.. _git-credentials:


*************************
Updating user credentials
*************************

Per :xref:`git-config`:

#. Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` to edit
   :xref:`git-config` using :xref:`Vim`:

   .. code-block:: bash

      git config --global -e

#. Type ``i`` then :kbd:`return` to get into
   :xref:`insert mode <Vim-cheatsheet>`, then make your changes:

   .. code-block:: none
      :emphasize-lines: 2-3

      [user]
           name = alnoki
           email = 43892045+alnoki@users.noreply.github.com
      [core]
           editor = Vim

#. Type :kbd:`Esc`, then ``:x!``, then :kbd:`return`, to
   :xref:`save and close <Vim-cheatsheet>`

#. To check that the credentials have updated:

   .. code-block:: bash

      git config --global --list


.. _git-view-project-log:

****************
View project log
****************

Per :xref:`git-log`:

#. In the :xref:`VS Code integrated terminal <VS-Code-terminal>`:

   .. code-block:: bash

      git log

#. This will open the :xref:`less-pager` for text navigation

   .. csv-table:: Core :xref:`less commands <less-pager>`
      :header: "Key", "Function"
      :align: center

      :kbd:`return`, scroll
      ``q``, exit
      ``h``, show help

#. A condensed version:

   .. code-block:: bash

      git log --oneline

.. _list-committers:


***********************
List project committers
***********************

Use :xref:`git log --pretty <git-log>` options, explained per:

   * :xref:`list-git-developers`
   * :xref:`git-log-formatting`

#. In the :xref:`VS Code integrated terminal <VS-Code-terminal>`, isolate all
   unique instances of a field:

   .. code-block:: bash

      git log --pretty="Author name: %an" | sort | uniq
      git log --pretty="Author email: %ae" | sort | uniq
      git log --pretty="Committer name: %cn" | sort | uniq
      git log --pretty="Committer email: %ce" | sort | uniq

#. Inspect all of these fields at once, for the entire project history:

   .. code-block:: bash

      git log --pretty="%an, %ae, %cn, %ce"

.. _committing:


**********
Committing
**********

Per :xref:`git-commit` and :xref:`git-push`:

#. Verify the state of the project using the
   :xref:`VS Code integrated terminal <VS-Code-terminal>`:

   .. code-block:: bash

      git pull
      git log

#. Save and close any open project files
#. Update and verify your :ref:`Git user credentials <git-credentials>` as
   needed
#. Use the :xref:`VS Code command palette <command-palette>` to select

   * :guilabel:`View: Open View`
   * :guilabel:`Source Control`

#. Use the :guilabel:`Source Control` interface to
   :xref:`stage changes <git-commit>`
#. In the :xref:`VS-Code-terminal`:

   .. code-block:: bash

      git commit

   * This will open :xref:`Vim`, which you can use to generate your
     :xref:`commit message <git-commit>`
   * See :ref:`git-credentials` for the :xref:`save and close <Vim-cheatsheet>`
     procedure

#. In the :xref:`command palette <command-palette>`:
   :guilabel:`Git: Commit Staged`

#. Use the :xref:`VS-Code-terminal` to verify the :xref:`commit <git-commit>`
   looks alright and that the :ref:`commit identities <list-committers>` are
   okay

   .. code-block:: bash

      git log
      git log --pretty="%an, %ae, %cn, %ce"

#. Use the :xref:`VS-Code-terminal` to :xref:`push <git-push>`

   .. code-block:: bash

      git push

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

      git log --pretty="%an, %ae, %cn, %ce"

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

