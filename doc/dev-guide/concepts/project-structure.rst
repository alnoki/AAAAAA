.. 0.3.0

.. _concepts-project-structure:


#################
Project structure
#################


******
Access
******

:xref:`source-code` and :wiki-pg:`documentation <Software_documentation>`
for :term:`AAAAAA` are located at the
:github:`AAAAAA repository <alnoki/AAAAAA>`, which is
:wiki-pg:`hosted <Host_(network)>` by :github:`GitHub <>`

.. _concepts-project-tree:


********
Contents
********

Some select demonstrative contents of the
:github:`AAAAAA repository <alnoki/AAAAAA>`:

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
   :align: center
   :header: Name, Function

   ``AAAAAA/``, Project root :xref:`directory <directory>`
   ``src/`` , :xref:`Source code <source-code>` (in :ref:`tools-Python`)
   ``test/`` , :ref:`pytest test code <tools-pytest>`
   ``doc/`` , ":ref:`tools-sphinx`-style
   :wiki-pg:`documentation <Software_documentation>`"
   ``nbs/`` , :ref:`Jupyter notebooks <tools-jupyter>`
   ``.vscode/`` , :ref:`tools-vs-code` settings
   ``.gitignore`` , :ref:`tools-git` configuration
   ``a6.yml`` , :term:`a6 conda environment <a6>`
   ``setup.py`` , Configuration for :ref:`tools-pytest`
   ``README.md`` , "Contains :wiki-pg:`URL` for
   :wiki-pg:`documentation <Software_documentation>`
   :xref:`website <website>`"
   ``TODO.md`` , :ref:`Task planning <versioning-td3>`
