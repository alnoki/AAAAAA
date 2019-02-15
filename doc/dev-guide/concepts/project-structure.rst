.. 5863379

.. _concepts-project-structure:

#################
Project structure
#################


******
Access
******

:term:`AAAAAA` source code and documentation is available at the
:xref:`AAAAAA-repo`, which is hosted by :xref:`GitHub`

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
   :header: "Name", "Function"
   :align: center

   ``AAAAAA/``, Project root :xref:`directory <directory>`
   ``src/`` , :xref:`Source code <open-source>`
   ``test/`` , :ref:`tools-pytest` code
   ``doc/`` , :ref:`tools-sphinx` documentation
   ``nbs/`` , :ref:`tools-jupyter` notebooks
   ``.vscode/`` , :ref:`tools-vs-code` settings
   ``.gitignore`` , :ref:`tools-git` configuration
   ``a6.yml`` , Specifies the :term:`a6 environment <a6>`
   ``setup.py`` , Configuration for :ref:`tools-pytest`
   ``README.md`` , Points to :term:`AAAAAA` homepage
   ``TODO.md`` , Development :ref:`task planning <versioning-td3>`
