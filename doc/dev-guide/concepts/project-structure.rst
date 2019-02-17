.. 0.3.0

.. _concepts-project-structure:


#################
Project structure
#################


******
Access
******

:xref:`source-code` and documentation
:ref:`reST files <tools-restructured-text>` for :term:`AAAAAA` are located at
the :xref:`AAAAAA-repo`, which is hosted by :xref:`GitHub`

.. _concepts-project-dir-tree:


********
Contents
********

Some select demonstrative contents of the :xref:`AAAAAA-repo`:

.. code-block:: none

   AAAAAA/
       src/
           AAAAAA/
               __init__.py
               ledger.py
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
       .vscode/
           settings.json
       .gitignore
       a6.yml
       setup.py
       README.md
       TODO.md

.. csv-table:: Project contents
   :header: Name, Function
   :align: center

   ``AAAAAA/``, Project root :xref:`directory <directory>`
   ``src/`` , :xref:`Source code <source-code>` (in :ref:`tools-Python`)
   ``test/`` , :ref:`pytest test code <tools-pytest>`
   ``doc/`` , :ref:`tools-sphinx` documentation
   ``nbs/`` , :ref:`Jupyter notebooks <tools-jupyter>`
   ``.vscode/`` , :ref:`tools-vs-code` settings
   ``.gitignore`` , :ref:`tools-git` configuration
   ``a6.yml`` , :term:`a6 conda environment <a6>`
   ``setup.py`` , Configuration for :ref:`tools-pytest`
   ``README.md`` , "Reference to :term:`AAAAAA` documentation
   :xref:`website <website>`"
   ``TODO.md`` , :ref:`Task planning <versioning-td3>`
