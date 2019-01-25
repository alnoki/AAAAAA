#################
Project structure
#################


******
Access
******

:term:`AAAAAA` source code and documentation is available at the
:xref:`AAAAAA-repo`, which is hosted by :xref:`GitHub`

.. _project-dir-tree:


********
Contents
********

.. csv-table:: Select references
   :header: "Reference", "Topic"
   :align: center

   :ref:`python:tut-packages`, Explains directory structuring
   :std:doc:`pytest:goodpractices`, Structure for testing code

.. code-block:: none
   :caption: Select contents of the :xref:`AAAAAA-repo`

   AAAAAA/
       src/
           AAAAAA/
               __init__.py
               ledger.py
               utilities.py
       test/
           test_utilities.py
           test_ledger.py
       doc/
           index.rst
           conf.py
           make.bat
       nbs/
           dev/
               ledger.ipynb
           src/
               ledger.ipynb
               utilities.ipynb
       a6.yml
       TODO.md
       README.md
       setup.py
       .gitignore
       .vscode/
           settings.json

The :xref:`AAAAAA-repo` has several top-level directories of particular
importance:

#. ``src``: Source code
#. ``test``: :std:doc:`pytest <pytest:index>` modules for testing source code
#. ``doc``: Documentation created via
   :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
#. ``nbs``: :xref:`Jupyter Notebook <Jupyter>` documentation of ``src`` and
   ``dev`` (nbs = ``notebooks``)

   * ``dev`` includes walkthroughs done during experimental code creation
   * ``src`` includes some documentation created before the use of
     :std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
     was adopted

Additional contents of the :xref:`AAAAAA-repo`, which can be manipulated in
:ref:`tools-VS-Code` :

#. ``.vscode`` directory contains development
   :xref:`settings <VS-Code-settings>`
#. ``.gitignore`` is for :ref:`git <tools-git>`
#. ``README.md`` contains references to :term:`AAAAAA` documentation
#. ``TODO.md`` contains planned development tasks
#. ``a6.yml`` specifies the :term:`a6 conda environment <a6>`