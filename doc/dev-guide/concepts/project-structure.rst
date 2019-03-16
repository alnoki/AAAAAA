.. 0.4.0

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
           src/
               ledger.ipynb
           doc/
               version-stats.ipynb
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

   ``AAAAAA/``, Project :xref:`root directory <directory>`
   ``src/`` , :ref:`Python source code <tools-Python>`
   ``test/`` , :ref:`pytest test code <tools-pytest>`
   ``doc/`` , ":ref:`tools-sphinx`-style
   :wiki-pg:`documentation <Software_documentation>`"
   ``nbs/`` , :ref:`Jupyter notebooks <tools-jupyter>`
   ``.vscode/`` , :ref:`VS Code settings <tools-vs-code>`
   ``.gitignore`` , :ref:`Git configuration <configs-git>`
   ``a6.yml`` , :term:`a6 conda environment <a6>`
   ``setup.py`` , :ref:`pytest configuration <configs-pytest>`
   ``README.md`` , "Has :wiki-pg:`URL` for
   :wiki-pg:`documentation <Software_documentation>`
   :xref:`website <website>`"
   ``TODO.md`` , :ref:`Task planning <versioning-td3>`
