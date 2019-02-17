.. 0.3.0

.. _dev-env-analyzing:


#########
Analyzing
#########

#. Use the :xref:`VS Code integrated terminal <VS-Code-terminal>` to
   :doc:`install <conda:commands/install>` some more
   :ref:`conda packages <conda:concept-conda-package>` for :term:`a6`:

   .. code-block:: bash

      conda install jupyter numpy matplotlib pandas

#. Install the :doc:`nb-extensions:index`:

   .. code-block:: bash

      conda install -c conda-forge jupyter_contrib_nbextensions

#. Open a :ref:`Jupyter Notebook <tools-jupyter>`:

   .. code-block:: bash

      jupyter notebook

#. Use :guilabel:`New` to open a new :guilabel:`Python 3`
   :ref:`Jupyter Notebook <tools-jupyter>`
#. Use :guilabel:`Edit`, then :guilabel:`nbextensions config`
   to enable the following :doc:`extensions <nb-extensions:index>`:

   #. :doc:`Collapsible Headings <nb-extensions:nbextensions/collapsible_headings/readme>`
   #. :doc:`nb-extensions:nbextensions/toc2/README`
   #. :doc:`nb-extensions:nbextensions/varInspector/README`
   #. :xref:`live-md-preview`

Congratulations!!!
