.. _procedures-conda:


#####
Conda
#####

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :std:doc:`conda:user-guide/tasks/manage-environments`, Practical reference
   :ref:`tools-anaconda`, :term:`AAAAAA` explanation

.. contents:: Contents
   :local:

.. _conda-tidy-up:


**********
Tidying up
**********

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`

#. Use :std:doc:`conda:commands/update` to get the latest
   :ref:`packages <conda:concept-conda-package>`:

   .. code-block:: bash

      conda update --all

   .. tip::
      This will usually get as many
      :ref:`packages <conda:concept-conda-package>`
      as possible from the official
      :ref:`conda channel <conda:channels-glossary>`

#. Use :std:doc:`conda:commands/clean` to get rid of excess files:

   .. code-block:: bash

      conda clean --all

#. Use :std:doc:`conda:commands/list` to inspect the new
   :ref:`conda environment <conda:concept-conda-env>`:

   .. code-block:: bash

      conda list

.. _conda-create-a6:


************************
Creating a6 from scratch
************************

#. Use the :ref:`packages table <anaconda-packages-table>` to indentify which
   :ref:`packages <anaconda-packages-table>` you need

#. :ref:`Start up conda <conda:starting-conda>`, then use
   :std:doc:`conda:commands/create` to make a new
   :ref:`conda environment <conda:concept-conda-env>` with
   :ref:`packages <conda:concept-conda-package>` from
   the :ref:`conda channel <conda:channels-glossary>`:

   .. code-block:: bash

      conda create -n a6 python conda pep8 sphinx sphinx_rtd_theme jupyter numpy matplotlib pandas pytest

   .. note::
      Be sure to copy and paste the whole box! It may scroll to the right on
      your screen

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`

#. :std:doc:`Install <conda:commands/install>` the remaining
   :ref:`packages <conda:concept-conda-package>` from :xref:`conda-forge`:

   .. code-block:: bash

      conda install -c conda-forge doc8 jupyter_contrib_nbextensions

#. :ref:`Install AAAAAA for testing <conda-pip-AAAAAA>`

#. :ref:`Tidy up <conda-tidy-up>`

.. _conda-import-a6:


************
Importing a6
************

#. :ref:`Start up conda <conda:starting-conda>` from inside the
   :ref:`project root directory <project-dir-tree>`, then
   :std:doc:`import <conda:user-guide/tasks/manage-environments>`
   the necessary :ref:`conda packages <anaconda-packages-table>`:

   .. code-block:: bash

      conda env create -f a6.yml

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`

#. :ref:`Install AAAAAA for testing <conda-pip-AAAAAA>`

#. :ref:`Tidy up <conda-tidy-up>`

.. _conda-pip-AAAAAA:


*****************************
Installing AAAAAA for testing
*****************************

Per :std:doc:`pytest integration practices <pytest:goodpractices>`:

#. From inside the :ref:`AAAAAA project directory <project-dir-tree>`, use
   :term:`a6` from inside the
   :ref:`VS Code integrated terminal <tools-VS-Code>`:

   .. code-block:: bash

      pip install -e .

#. :ref:`Tidy up <conda-tidy-up>`


*******************
Using a new package
*******************

#. Add the :ref:`package <conda:concept-conda-package>` to

   #. The :ref:`packages table <anaconda-packages-table>`
   #. The :ref:`a6.yml file <project-dir-tree>`
   #. The instructions for :ref:`creating a6 <conda-create-a6>`
   #. An installation step somewhere in the
      :ref:`developer setup <dev-environment>`

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`

#. :std:doc:`Install <conda:commands/install>` the desired
   :ref:`package <anaconda-packages-table>`

#. :ref:`Tidy up <conda-tidy-up>`
