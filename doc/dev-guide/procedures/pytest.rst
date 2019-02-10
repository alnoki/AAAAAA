.. 5863379

.. _pytest-procedures:

######
pytest
######

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`tools-pytest`, :term:`AAAAAA` conceptual explanation
   :std:doc:`pytest:index`, Official documentation


*****************
Discovering tests
*****************

#. Verify that you can run :ref:`tools-pytest` in the
   :ref:`VS Code integrated terminal <tools-vs-code>` from inside the
   :ref:`AAAAAA project root directory <concepts-project-dir-tree>`

   .. code-block:: bash

      pytest

   * This should yield output that looks like the
     :std:doc:`pytest documentation <pytest:index>`

#. Use the :ref:`VS Code command palette <tools-vs-code>` to select
   :guilabel:`Python: Discover Unit Tests`
#. If this fails, you may be experiencing a :xref:`pytest-discovery-issue`
   that is associated with a new :ref:`tools-pytest` release. You can either:

   #. Use the :xref:`VS Code Insider Edition <VS-Code-insiders>`, if a fix has
      recently been made available
   #. Temporarily use an older :ref:`package <conda:concept-conda-package>`
      version for :ref:`tools-pytest`

      #. :ref:`activate <conda:activate-env>` the :term:`a6 environment <a6>`
      #. Use :std:doc:`conda:commands/install` with the appropriate version
         number syntax from the
         :std:doc:`conda cheatsheet <conda:user-guide/cheatsheet>`. For
         example:

         .. code-block:: bash

            conda install "pytest<=4.0.0"

#. Use the :ref:`VS Code command palette <tools-vs-code>` to select
   :guilabel:`Python: Discover Unit Tests`
#. Check out the
   :ref:`VS Code Test Explorer Extension <tools-vs-code>` to see if tests are
   showing up
