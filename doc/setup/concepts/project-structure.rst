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

.. code-block:: none
   :caption: Select contents of the :xref:`AAAAAA-repo`

   AAAAAA/
       src/
           AAAAAA/
               __init__.py
               ledger.py
               utilities.py
       test/
           test_ledger.py
           test_utilities.py
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
       .vscode/
           settings.json
       .gitignore
       a6.yml
       setup.py
       README.md
       TODO.md

.. csv-table:: Project contents
   :header: "Name", "Function"
   :align: center

   ``src/`` , Source code
   ``test/`` , :ref:`tools-pytest` code
   ``doc/`` , :ref:`tools-sphinx` documentation
   ``nbs/`` , :ref:`tools-jupyter` notebooks
   ``.vscode/`` , :ref:`tools-VS-Code` settings
   ``.gitignore`` , :ref:`tools-git` configuration
   ``a6.yml`` , Specifies the :term:`a6 environment <a6>`
   ``setup.py`` , Configuration for :ref:`tools-pytest`
   ``README.md`` , Renders at the :xref:`AAAAAA-repo`
   ``TODO.md`` , Planned development tasks
