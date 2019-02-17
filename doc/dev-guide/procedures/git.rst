.. 0.3.0

.. _git-procedures:


###
Git
###

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-manual`, Quick practical reference
   :xref:`git-book`, In-depth conceptual explanations
   :xref:`commit-conventions`, Tell the :xref:`codebase <software>` what to do
   :xref:`git-commit-guidelines`, Long message guidelines

.. contents:: Contents
   :local:

.. _git-setup:


**********
Setting up
**********

Use the :ref:`VS Code integrated terminal <tools-vs-code>` for first-time
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
   :header: Reference, Topic
   :align: center

   :xref:`Vim-tutorial`, Learn minimum necessary :xref:`Vim <Vim>`
   :xref:`Vim-cheatsheet`, Common commands

.. _git-credentials:


*************************
Updating user credentials
*************************

Per :xref:`git-config`:

#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to edit
   :xref:`git-config` using :xref:`Vim <Vim>`:

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

#. Type :kbd:`Esc`, then ``:x``, then :kbd:`return`, to
   :xref:`save and close <Vim-cheatsheet>`
#. To check that the credentials have updated:

   .. code-block:: bash

      git config --global --list

.. _git-view-project-log:


***********************
Viewing the project log
***********************

Per :xref:`git-log`:

#. In the :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git log

#. This will open the :xref:`less-pager` for text navigation

   .. csv-table:: Core :xref:`less commands <less-pager>`
      :header: Key, Function
      :align: center

      :kbd:`return`, scroll
      ``q``, exit
      ``h``, show help

.. tip::

   A condensed version:

      .. code-block:: bash

         git log --oneline

.. _git-list-committers:


**************************
Listing project committers
**************************

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-log`, Syntax reference
   :xref:`list-git-developers`, Sorting unique instances
   :xref:`git-log-formatting`, Practical syntax examples

#. In the :ref:`VS Code integrated terminal <tools-vs-code>`, isolate all
   unique instances of a field:

   .. code-block:: bash

      git log --pretty="Author name: %an" | sort | uniq
      git log --pretty="Author email: %ae" | sort | uniq
      git log --pretty="Committer name: %cn" | sort | uniq
      git log --pretty="Committer email: %ce" | sort | uniq

#. Inspect all of these fields at once, for the entire project history:

   .. code-block:: bash

      git log --pretty="%an, %ae, %cn, %ce"

.. _git-committing:


**********
Committing
**********

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-commit`, Create snapshot of project changes
   :xref:`git-push`, Upload changes to :xref:`GitHub`
   :xref:`Message conventions <commit-conventions>`, "Tell the
   :xref:`codebase <software>` what to do"

#. Verify the state of the project using the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git pull
      git log

#. Save and close any open project files
#. :ref:`Update your Git credentials <git-credentials>` and verify as needed
#. Use the :ref:`VS Code command palette <tools-vs-code>` to select:

   * :guilabel:`View: Open View`
   * :guilabel:`Source Control`

#. Use the :guilabel:`Source Control` interface to
   :xref:`stage changes <git-commit>`

   * You may consider using the :ref:`command palette <tools-vs-code>` to
     select :guilabel:`Git: Stage All Changes`


#. In the :ref:`integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git commit

   .. Note::

      This will open :xref:`Vim <Vim>`, which you can use to generate your
      :xref:`commit message <git-commit>` per the
      :xref:`save and close <Vim-cheatsheet>` procedure used to
      :ref:`update Git credentials <git-credentials>`

#. Compose a message that
   :xref:`tells the codebase what to do <commit-conventions>`

#. Use the :ref:`integrated terminal <tools-vs-code>` to verify the
   :xref:`commit <git-commit>` looks alright and that the
   :ref:`commit identities <git-list-committers>` are okay

   .. code-block:: bash

      git log

#. If you want complete redundancy, recall the
   :ref:`listing committers procedure <git-list-committers>`:

   .. code-block:: bash

      git log --pretty="%an, %ae, %cn, %ce"

#. Use the :ref:`integrated terminal <tools-vs-code>` to
   :xref:`push <git-push>` and verify

   .. code-block:: bash

      git push
      git log

#. Verify results at the :xref:`AAAAAA-repo`


.. _git-tagging:


*******
Tagging
*******

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-tag`, Assign a unique identifier to a :xref:`commit <git-commit>`
   :xref:`Message style <commit-conventions>`, "Tell the
   :xref:`codebase <software>` what to do"
   :xref:`git-push`, Upload changes to :xref:`GitHub`
   :xref:`git-commit-guidelines`, Long message guidelines


#. :ref:`View the project log <git-view-project-log>` to verify the
   :xref:`commit <git-commit>` in question
#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to view existing
   :xref:`tags <git-tag>`

   .. code-block:: bash

      git tag

#. Create an :xref:`annotated tag <git-tag>`:

   .. code-block:: bash

      git tag -a 0.3.0

   .. Note::

      This will open :xref:`Vim <Vim>`, which you can use to generate your
      :xref:`commit message <git-commit>` per the
      :xref:`save and close <Vim-cheatsheet>` procedure used to
      :ref:`update Git credentials <git-credentials>`

#. Compose a message that
   :xref:`tells the codebase what to do <commit-conventions>` and includes
   a :xref:`lengthier description <git-commit-guidelines>` if appropriate
#. Verify by :ref:`viewing the project log <git-view-project-log>`
#. :xref:`Push <git-push>`:

   .. code-block:: bash

      git push 0.3.0

#. Verify results at the :xref:`AAAAAA-repo`

.. _git-branching:


*********
Branching
*********

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-branch`, Manage independent :xref:`commit <git-commit>` sequences
   :xref:`git-checkout`, Switch :xref:`branches <git-branch>`

#. :ref:`View the project log <git-view-project-log>` to verify the
   :xref:`commit <git-commit>` in question
#. Inspect :xref:`all branches <git-branch>` in the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git branch -a

#. :xref:`Create and check out <git-checkout>` a new
   :xref:`tracked branch <git-branch>`:

   .. code-block:: bash

      git checkout -b dev/0.3.0

#. Verify:

   .. code-block:: bash

      git branch


.. tip::

   The first time you :ref:`commit <git-committing>` a new
   :xref:`branch <git-branch>` to the :xref:`AAAAAA-repo`, make sure to
   :xref:`set upstream tracking <git-push>`:

   .. code-block:: bash

      git push -u origin dev/0.3.0

.. _git-merging:


*******
Merging
*******

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`git-branch`, Manage independent :xref:`commit <git-commit>` sequences
   :xref:`git-checkout`, Switch :xref:`branches <git-branch>`
   :xref:`git-merge`, Combine :xref:`branches <git-branch>`

#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to
   :xref:`view available branches <git-branch>`:

   .. code-block:: bash

      git branch

#. :xref:`Checkout <git-checkout>` the appropriate :xref:`branch <git-branch>`:

   .. code-block:: bash

      git checkout master

#. :xref:`Merge <git-merge>` the desired :xref:`branch <git-branch>`

   .. code-block:: bash

      git merge dev/0.3.0

#. :ref:`Verify the project log <git-view-project-log>`

.. _git-change-commit-history:


**********************************
Changing commit credential history
**********************************

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-git`, :term:`AAAAAA` conceptual explanation
   :xref:`Change author history <github-change-authors>`, "
   :xref:`GitHub` instructions"
   :xref:`git-branch-filtering`, Advanced syntax

.. warning::

   This can totally mess stuff up if you are not careful

#. For the most part, follow :xref:`github-change-authors`. Before you
   :xref:`push the corrected history <github-change-authors>`, check out the
   updated :ref:`commit credential history <git-list-committers>`:

   .. code-block:: bash

      git log --pretty="%an, %ae, %cn, %ce"

#. If you forget to :ref:`update your user credentials <git-credentials>`
   before :ref:`committing and pushing <git-committing>` (a whole bunch of
   times),
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

   * This will update all
     :ref:`project commit credentials <git-list-committers>`
     that were not authored by ``43892045+alnoki@users.noreply.github.com``

#. If you want to get more specific about your selections, play around with
   some more options:

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
