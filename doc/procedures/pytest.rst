######
pytest
######


*****************
Discovering tests
*****************

#. Verify that you can run :std:doc:`pytest <pytest:index>` in the
   :xref:`VS Code integrated terminal <VS-Code-terminal>` from inside the
   :ref:`root directory <project-dir-tree>` of :term:`AAAAAA`

   .. code-block:: bash

      pytest

   * This should yield output that looks like the
     :std:doc:`pytest documentation <pytest:index>`

#. Use the :xref:`VS Code command palette <command-palette>` to select
   :guilabel:`Python: Discover Unit Tests`

#. If this fails, you may be experiencing a :xref:`pytest-discovery-issue`
   that is associated with a new :std:doc:`pytest <pytest:index>` release. You
   can either:

   #. Use the :xref:`VS Code Insider Edition <VS-Code-insiders>`, if a fix has
      recently been made available
   #. Temporarily use an older version of
      :std:doc:`pytest documentation <pytest:index>`. For
      example, :ref:`activate <conda:activate-env>` the
      :term:`a6 environment <a6>`, then use
      :std:doc:`conda:commands/install` with the appropriate version number
      syntax from the
      :std:doc:`conda cheatsheet <conda:user-guide/cheatsheet>`:

      .. code-block:: bash

         conda install "pytest<=4.0.0"

#. Check out the :xref:`Test-explorer-UI` to see if tests are showing up
