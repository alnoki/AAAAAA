.. 0.3.0

.. _conda-procedures:


#####
Conda
#####

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :ref:`tools-anaconda`, :term:`AAAAAA` conceptual explanation
   :doc:`conda:user-guide/tasks/manage-environments`, "Official practical
   reference"

.. attention::

   Most of these instructions assume you have already done the
   :ref:`developer environment setup <dev-env-intro>`, which will help you
   integrate :ref:`conda <tools-anaconda>` with :ref:`tools-vs-code`

.. contents:: Contents
   :local:

.. _conda-tidy-up:


**********
Tidying up
**********

#. :ref:`Start up conda <conda:starting-conda>`
#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`
#. Use :doc:`conda:commands/update` to get the latest
   :ref:`packages <conda:concept-conda-package>`:

   .. code-block:: bash

      conda update --all

   .. tip::

      This will usually get as many
      :ref:`packages <conda:concept-conda-package>`
      as possible from the official
      :ref:`conda channel <conda:channels-glossary>`

#. Use :doc:`conda:commands/clean` to get rid of excess
   :wiki-pg:`files <Computer_file>`:

   .. code-block:: bash

      conda clean --all

#. Use :doc:`conda:commands/list` to inspect the new
   :ref:`conda environment <conda:concept-conda-env>`:

   .. code-block:: bash

      conda list

.. _conda-create-a6:


************************
Creating a6 from scratch
************************

#. Use the :ref:`packages table <concepts-packages-table>` to indentify which
   :ref:`packages <conda:concept-conda-package>` you need
#. :ref:`Start up conda <conda:starting-conda>`, then use
   :doc:`conda:commands/create` to make a new
   :ref:`conda environment <conda:concept-conda-env>` with
   :ref:`packages <conda:concept-conda-package>` from
   the :ref:`conda channel <conda:channels-glossary>`:

   .. code-block:: bash

      conda create -n a6 python conda pep8 sphinx sphinx_rtd_theme jupyter numpy matplotlib pandas pip pytest

   .. note::

      Be sure to :wiki-pg:`copy and paste <Cut,_copy,_and_paste>` the whole
      box! It may :wiki-pg:`scroll <Scroll>` to the right

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`
#. :doc:`Install <conda:commands/install>` the remaining
   :ref:`packages <conda:concept-conda-package>` from :xref:`conda-forge`:

   .. code-block:: bash

      conda install -c conda-forge doc8 sphinxcontrib-bibtex sphinx-autobuild jupyter_contrib_nbextensions

   .. note::

      Be sure to :wiki-pg:`copy and paste <Cut,_copy,_and_paste>` the whole
      box! It may :wiki-pg:`scroll <Scroll>` to the right

#. :ref:`Install AAAAAA for testing <conda-pip-AAAAAA>`
#. :ref:`Tidy up <conda-tidy-up>`

.. _conda-import-a6:


************
Importing a6
************

#. :ref:`Start up conda <conda:starting-conda>` from inside the
   :ref:`AAAAAA project directory <concepts-project-tree>`, then
   :doc:`import <conda:user-guide/tasks/manage-environments>`
   the necessary :ref:`conda packages <concepts-packages-table>`:

   .. code-block:: bash

      conda env create -f a6.yml

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`
#. :ref:`Install AAAAAA for testing <conda-pip-AAAAAA>`
#. :ref:`Tidy up <conda-tidy-up>`

.. _conda-pip-AAAAAA:


*****************************
Installing AAAAAA for testing
*****************************

Per :doc:`pytest integration practices <pytest:goodpractices>`:

#. From inside the :ref:`AAAAAA project directory <concepts-project-tree>`, use
   :term:`a6` from inside the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      pip install -e .

#. :ref:`Tidy up <conda-tidy-up>`

.. _conda-use-new-package:


*******************
Using a new package
*******************

#. Add the :ref:`package <conda:concept-conda-package>` to

   #. The :ref:`packages table <concepts-packages-table>`
   #. The :ref:`a6.yml file <concepts-project-tree>`
   #. The instructions for :ref:`creating a6 from scratch <conda-create-a6>`

      * Here, use the same order for the separate
        :ref:`channels <conda:channels-glossary>` as from top to bottom in the
        :ref:`packages table <concepts-packages-table>`

   #. An installation step somewhere in the
      :ref:`developer environment setup <dev-env-intro>`

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>`
#. :doc:`Install <conda:commands/install>` the desired
   :ref:`package <concepts-packages-table>`
#. :ref:`Tidy up <conda-tidy-up>`
