###
Git
###

.. _git-credentials:


*************************
Updating user credentials
*************************

Per the :xref:`git-manual`:

#. If you are not :xref:`alnoki <alnoki-repos>`, use the
   :xref:`VS-Code-terminal` to enter the following (adapted for your name and
   email address):

   .. code-block:: bash

      git config --global user.name 'not alnoki'
      git config --global user.email 'not_alnoki@interweb.com'

#. To check that the credentials have updated:

   .. code-block:: bash

      git config --global --list

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

#. Verify everything looks alright in the :xref:`VS-Code-terminal`:

   .. code-block:: bash

      git log

#. In the :xref:`command palette <command-palette>`:
   :guilabel:`Git: Push`
#. Check out the :xref:`AAAAAA-repo`
