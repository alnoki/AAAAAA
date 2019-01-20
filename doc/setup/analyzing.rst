.. _analyzing:


#########
Analyzing
#########

#. Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` to
   :std:doc:`install <conda:commands/conda-install>` some more
   :ref:`conda packages <conda:concept-conda-package>` for :term:`a6`:

   .. code-block:: bash

      conda install jupyter numpy matplotlib pandas

#. Install the :std:doc:`nb-extensions:index`:

   .. code-block:: bash

      conda install -c conda-forge jupyter_contrib_nbextensions

#. Open a :xref:`Jupyter Notebook <Jupyter>`

   .. code-block:: bash

      jupyter notebook

#. Use the :guilabel:`New` button to open a new :guilabel:`Python 3`
   :xref:`Jupyter Notebook <Jupyter>`

#. Hit the :guilabel:`Edit` button, then the :guilabel:`nbextensions config`
   button to enable the following :std:doc:`extensions <nb-extensions:index>`:

   #. :std:doc:`Collapsible Headings <nb-extensions:nbextensions/collapsible_headings/readme>`
   #. :std:doc:`nb-extensions:nbextensions/toc2/README`
   #. :std:doc:`nb-extensions:nbextensions/varInspector/README`
   #. :xref:`live-md-preview`