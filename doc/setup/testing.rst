.. _setup-testing:

#######
Testing
#######

#. Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` to
   :std:doc:`install <conda:commands/install>` some more
   :ref:`conda packages <conda:concept-conda-package>` for :term:`a6`:

   .. code-block:: bash

      conda install pip pytest

#. From inside the :ref:`AAAAAA project directory <project-dir-tree>`,
   configure :std:doc:`pytest discovery <pytest:goodpractices>` for
   :term:`AAAAAA`

   .. code-block:: bash

      pip install -e .

#. Install the :xref:`Python Test Explorer for VS Code <Test-explorer-UI>`

#. :ref:`Tidy up <conda-tidy-up>`:

   .. code-block:: bash

      conda update --all
      conda clean --all
      conda list

   .. tip::
      Enter these one at a time, instead of copy-pasting

#. Try out :ref:`tools-pytest`:

   .. code-block:: bash

      pytest

Congratulations!!!
