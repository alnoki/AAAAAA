.. _procedures-git:


###
Git
###

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: Center
   :header: Reference, Topic

   :ref:`tools-git`, Conceptual explanation

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :git-doc:`Git manual <user-manual>`, Quick practical reference
   :git-scm:`Git book <book/en/v2>`, In-depth conceptual explanations
   :xref:`git-commit-guidelines`, Official message guidelines
   :xref:`commit-conventions`, Tell the :xref:`codebase <software>` what to do

.. contents:: Contents
   :local:

.. _git-configuring:


***********
Configuring
***********

.. contents::
   :local:

.. csv-table:: Learning :ref:`tools-vim`
   :align: center
   :header: Reference, Topic

   :xref:`Vim-tutorial`, Learn minimum necessary :xref:`Vim <Vim>`
   :xref:`Vim-cheatsheet`, Common :wiki-pg:`commands <Command_line>`
   :ref:`Vim configuration <configs-vim>`, "
   :ref:`Configuration <concepts-configs>` for :term:`AAAAAA`"

.. _git-setup:

Setting up
==========

Use the :ref:`VS Code integrated terminal <tools-vs-code>` for first-time
:xref:`git-setup`:

#. Configure your :wiki-pg:`identity <User_(computing)>`:

   .. code-block:: bash

      git config --global user.name alnoki
      git config --global user.email 43892045+alnoki@users.noreply.github.com

#. Indicate :ref:`tools-vim` as the :xref:`default editor <git-setup>` and use
   it to verify your :wiki-pg:`identity <User_(computing)>`:

   .. code-block:: bash

      git config --global core.editor Vim
      git config --global -e

#. At this point, you will be in :ref:`tools-vim`. If you your
   :wiki-pg:`identity <User_(computing)>` looks right, you can
   :xref:`exit without saving <Vim-cheatsheet>` by
   :wiki-pg:`typing <Typing>` ``:q!`` then :kbd:`return`

#. :ref:`tools-vim` comes with
   :wiki-pg:`syntax highlighting <Syntax_highlighting>` for
   :ref:`commit messages <git-committing>`, but if you are using a
   :wiki-pg:`Mac <Macintosh_operating_systems>` you may have to
   :vim-wiki:`enable it <Turn_on_syntax_coloring_in_Mac_OS_X>`, by creating a
   :vim-wiki:`.vimrc file <Open_vimrc_file>` at ``~/.vimrc`` with the
   following:

   .. code-block:: none

      filetype plugin indent on
      syntax on

#. If you are using a :wiki-pg:`Mac <Macintosh_operating_systems>`, you should
   also :xref:`enable key repeats <mac-key-repeats>`

.. _git-credentials:

Updating user credentials
=========================

Per :git-doc:`git-config`:

#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to edit
   :git-doc:`git-config` using :ref:`tools-vim`:

   .. code-block:: bash

      git config --global -e

#. :wiki-pg:`Type <Typing>` ``i`` then :kbd:`return` to get into
   :xref:`insert mode <Vim-cheatsheet>`, then make your changes:

   .. code-block:: none
      :emphasize-lines: 2-3

      [user]
           name = alnoki
           email = 43892045+alnoki@users.noreply.github.com
      [core]
           editor = Vim

#. :wiki-pg:`Type <Typing>` :kbd:`Esc`, then ``:x``, then :kbd:`return`, to
   :xref:`save and close <Vim-cheatsheet>`
#. To check that the :wiki-pg:`user credentials <User_(computing)>` have
   updated:

   .. code-block:: bash

      git config --global --list

.. _git-inspect-history:


******************
Inspecting history
******************

.. contents::
   :local:

.. csv-table:: Core :xref:`less commands <less-pager>`
   :align: center
   :header: Key, Function

   :kbd:`return`, scroll
   ``q``, exit
   ``h``, help

.. _git-view-project-log:

Viewing the project log
=======================

Per :git-doc:`git-log`:

#. In the :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git log

#. This will open the :xref:`less-pager`

#. A condensed version:

   .. code-block:: bash

      git log --oneline

   * Also (This might only work on a
     :wiki-pg:`Mac <Macintosh_operating_systems>`):

     .. code-block:: bash

        git lg

.. _git-list-committers:

Listing project committers
==========================

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :git-doc:`git-log`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>`
   reference"
   :xref:`list-git-developers`, Sorting unique instances
   :xref:`git-log-formatting`, "Practical
   :wiki-pg:`syntax <Syntax_(programming_languages)>` examples"

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

.. _git-get-commit-stats:

Get commit statistics
=====================

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :git-doc:`git-show`, :wiki-pg:`Time` inspection
   :git-doc:`git-rev-list`, :ref:`Commit <tools-git>` number inspection
   :xref:`dencode`, Convert :wiki-pg:`time standards <Time_standard>`

Typically you will do this once a :git-doc:`tag <git-tag>` has already been
made

#. In the :ref:`VS Code integrated terminal <tools-vs-code>`, use
   :git-doc:`git-show` to extract the :wiki-pg:`IS0 8601<ISO_8601>`-formatted
   :wiki-pg:`time <Time>`:

   .. code-block:: bash

      git show -s --format=%cI 0.4.0

#. On :xref:`dencode`, convert using
   :wiki-pg:`UTC <Coordinated_Universal_Time>` and
   :wiki-pg:`ISO8601 Date (Extend) <ISO_8601>`
#. To see the number of :ref:`commits <tools-git>`:

   .. code-block:: bash

      git rev-list --count HEAD
      git rev-list --count 0.4.0

.. _git-dev-tasks:


*****************
Development tasks
*****************

.. contents::
   :local:

.. _git-committing:

Committing
==========

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :git-doc:`git-add`, Prepare changes
   :git-doc:`git-commit`, Create snapshot of project changes
   :git-doc:`git-push`, :wiki-pg:`Upload` changes to :github:`GitHub <>`
   :xref:`git-commit-guidelines`, Official message guidelines

#. Verify the state of the project using the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git pull
      git log

#. :vs-code-doc:`Save and close <getstarted/userinterface>` any
   :wiki-pg:`open files <Computer_file>`
#. :ref:`Update your Git credentials <git-credentials>` and verify as needed
#. Use the
   :vs-code-doc:`VS Code symbol input
   <getstarted/userinterface#_command-palette>` to :wiki-pg:`type <Typing>`:

   * :guilabel:`view source control`

#. Use the :guilabel:`Source Control` interface to
   :git-doc:`stage changes <git-add>`

   * Consider using the :ref:`Command Palette <tools-vs-code>` to select

     * :guilabel:`Git: Stage All Changes`

   * Or, equivalently:

     .. code-block:: bash

        git add -A

#. In the :ref:`integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git commit

   .. Note::

      This will open :ref:`tools-vim`

#. Compose a message that
   :xref:`tells the codebase what to do <commit-conventions>`

#. Use the :ref:`integrated terminal <tools-vs-code>` to verify the
   :git-doc:`commit <git-commit>` looks alright and that the
   :ref:`commit identities <git-list-committers>` are okay

   .. code-block:: bash

      git log

#. If you want complete redundancy, recall the
   :ref:`listing committers procedure <git-list-committers>`:

   .. code-block:: bash

      git log --pretty="%an, %ae, %cn, %ce"

#. Use the :ref:`integrated terminal <tools-vs-code>` to
   :git-doc:`push <git-push>` and verify

   .. code-block:: bash

      git push
      git log

#. Optionally verify results at the :github:`AAAAAA repository <alnoki/AAAAAA>`

.. _git-committing-fixes:

Quick fixes
-----------

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :git-doc:`git-reset`, Fix mistakes
   :stack-q:`Vim 325 error <45489008/vim-opening-file-e325-attention-error>`, "
   If you :ref:`commit <git-committing>` incorrectly"

#. If you made a mistake in your :git-doc:`commit <git-commit>` but you haven't
   :git-doc:`pushed yet <git-push>`, you can try again via
   :git-doc:`git-reset`:

   .. code-block:: bash

      git reset --soft HEAD^

#. If you are experiencing a
   :stack-q:`Vim 325 error <45489008/vim-opening-file-e325-attention-error>`,
   you may need to :wiki-pg:`delete <Computer_file>` (if it exists)
   :ref:`AAAAAA/.git/COMMIT_MSG.swp <configs-vim>`

.. _git-tagging:

Tagging
=======

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`git-tag`, "Assign a unique identifier to a
   :git-doc:`commit <git-commit>`"
   :xref:`Message style <commit-conventions>`, "Tell the
   :xref:`codebase <software>` what to do"
   :git-doc:`git-push`, :wiki-pg:`Upload` changes to :github:`GitHub <>`
   :xref:`git-commit-guidelines`, Long message guidelines

#. :ref:`View the project log <git-view-project-log>` to verify the
   :git-doc:`commit <git-commit>` in question
#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to view existing
   :xref:`tags <git-tag>`

   .. code-block:: bash

      git tag

#. Create an :xref:`annotated tag <git-tag>`:

   .. code-block:: bash

      git tag -a 0.3.0

   .. Note::

      This will open :ref:`tools-vim`

#. Compose a message that
   :xref:`tells the codebase what to do <commit-conventions>` and includes
   a :xref:`lengthier description <git-commit-guidelines>` if appropriate
#. Verify by :ref:`viewing the project log <git-view-project-log>`
#. :git-doc:`Push with tag following <git-push>`:

   .. code-block:: bash

      git push --follow-tags

#. Verify results at the :github:`AAAAAA repository <alnoki/AAAAAA>`

.. _git-branching:

Branching
=========

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`git-branch`, "Manage independent
   :git-doc:`commit <git-commit>` sequences"
   :xref:`git-checkout`, Switch :xref:`branches <git-branch>`
   :git-doc:`git-fetch`, "Get :git-doc:`branches <git-branch>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>`"

#. :ref:`View the project log <git-view-project-log>` to verify the
   :git-doc:`commit <git-commit>` in question
#. Inspect :xref:`all branches <git-branch>` using the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      git branch -a

#. :xref:`Create and check out <git-checkout>` a new
   :xref:`tracked branch <git-branch>`:

   .. code-block:: bash

      git checkout -b dev/0.4.0

#. Verify:

   .. code-block:: bash

      git branch

#. The first time you :ref:`commit <git-committing>` a new
   :xref:`branch <git-branch>` to the
   :github:`AAAAAA repository <alnoki/AAAAAA>`, make sure to
   :git-doc:`set upstream tracking <git-push>`:

   .. code-block:: bash

      git push -u origin dev/0.4.0

#. To :xref:`check out <git-checkout>` a :xref:`branch <git-branch>` from the
   :github:`AAAAAA repository <alnoki/AAAAAA>` for the first time:

   .. code-block:: bash

      git fetch
      git checkout --track origin/dev/0.4.0

.. _git-merging:

Merging
=======

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`git-branch`, "Manage independent :git-doc:`commit <git-commit>`
   sequences"
   :git-doc:`git-checkout`, Switch :git-doc:`branches <git-branch>`
   :git-doc:`git-merge`, Combine :git-doc:`branches <git-branch>`

#. Use the :ref:`VS Code integrated terminal <tools-vs-code>` to
   :xref:`view available branches <git-branch>`:

   .. code-block:: bash

      git branch

#. :xref:`Checkout <git-checkout>` the appropriate :xref:`branch <git-branch>`:

   .. code-block:: bash

      git checkout master

#. :xref:`Merge <git-merge>` the desired :xref:`branch <git-branch>`

   .. code-block:: bash

      git merge dev/0.4.0

#. :ref:`Verify the project log <git-view-project-log>`

.. _git-change-commit-history:


**********************************
Changing commit credential history
**********************************

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`Change author history <github-change-authors>`, ":github:`GitHub <>`
   instructions"
   :xref:`git-branch-filtering`, "Advanced
   :wiki-pg:`syntax <Syntax_(programming_languages)>`"

If you are learning :ref:`tools-git` and you forget to either
:ref:`set up <git-setup>` your :wiki-pg:`identity <User_(computing)>` and/or
:ref:`update your credentials <git-credentials>` when using different
:wiki-pg:`computers <Computer>`, your
:ref:`committer list <git-list-committers>` can end up looking like total
nonsense. This is how you fix it

You should only need to do this once, then you will have (hopefully) learned
your lesson

.. warning::

   You can break things if you are not careful with this

#. For the most part, follow :xref:`github-change-authors`

   * Before you :xref:`push the corrected history <github-change-authors>`,
     check out the :ref:`unique project committers <git-list-committers>`

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

   * This example will update all
     :ref:`project commit credentials <git-list-committers>` that do not have
     ``43892045+alnoki@users.noreply.github.com`` as the
     :ref:`author email <git-list-committers>`

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
