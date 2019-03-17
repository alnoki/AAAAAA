.. _dev-env-testing:


#######
Testing
#######

#. Use the
   :vs-code-doc:`VS Code integrated terminal <editor/integrated-terminal>` to
   :doc:`install <conda:commands/install>` some more
   :ref:`conda packages <conda:concept-conda-package>` for :term:`a6`:

   .. code-block:: bash

      conda install pip pytest

#. From inside the :ref:`AAAAAA project directory <concepts-project-tree>`,
   configure :doc:`pytest discovery <pytest:goodpractices>` for
   :term:`AAAAAA`:

   .. code-block:: bash

      pip install -e .

#. Install the
   :vs-code-ext:`Python Test Explorer for VS Code
   <LittleFoxTeam.vscode-python-test-adapter>`
#. :ref:`Tidy up <conda-tidy-up>`:

   .. code-block:: bash

      conda update --all
      conda clean --all
      conda list

   .. note::

      :xref:`Copy-paste <copy-paste>` this one
      :wiki-pg:`line <Command-line_interface>` at a time

#. Try out :ref:`tools-pytest` from inside the
   :ref:`AAAAAA root directory <concepts-project-tree>`:

   .. code-block:: bash

      pytest

Congratulations!!!
