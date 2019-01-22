.. _procedures-conda:


#####
Conda
#####


************
Importing a6
************

#. :ref:`Start up Conda <conda:starting-conda>` from inside the
   :ref:`project root directory <project-dir-tree>`, then import
   the necessary :ref:`conda packages <anaconda-packages-table>`:

   .. code-block:: bash

      conda env create -f a6.yml

   * By default, this might not download all
     :ref:`packages <anaconda-packages-table>` from the
     :ref:`conda channel <tools-anaconda>`

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`

#. Use :std:doc:`conda:commands/update` to get packages from the
   :ref:`conda channel <tools-anaconda>`

   .. code-block:: bash

      conda update --all

#. Use :std:doc:`conda:commands/clean` to get rid of excess files:

   .. code-block:: bash

      conda clean --all

#. Use :std:doc:`conda:commands/list` to inspect the new
   :ref:`conda environment <conda:concept-conda-env>`:

   .. code-block:: bash

      conda list
