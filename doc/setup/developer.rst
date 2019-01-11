.. _dev-environment:


##############
For developers
##############

If you have already
:std:doc:`downloaded Miniconda <conda:user-guide/install/download>`, then
follow the steps in this section to reproduce the environment that
:xref:`alnoki <alnoki-repos>` uses to create :term:`AAAAAA`


***********
Documenting
***********

#. Install :xref:`VS-Code`
#. Update the :xref:`VS-Code-terminal` ``USER SETTINGS`` in
   :xref:`settings.json <VS-Code-settings>` so that you can use
   :std:doc:`conda:index`

   * On a :xref:`Mac`, add:

     .. code-block:: json

        {
            "terminal.integrated.shell.osx": "/bin/bash"
        }

   * On :xref:`Windows`, add (adapted for your username and machine):

     .. code-block:: json

        {
            "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
            "terminal.integrated.shellArgs.windows": ["/K",
                 "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat"],
        }

#. Use the :xref:`command-pallete` to open a new :xref:`VS-Code-terminal` and
   enter the following command to
   :std:doc:`create a new conda environment <conda:user-guide/cheatsheet>`,
   ``a6``, that has the necessary :ref:`packages <tools>`

   .. code-block:: bash

      conda create --name a6 python pep8 sphinx sphinx_rtd_theme

#. Configure the :xref:`VS-Code-terminal` to automatically
   :std:doc:`activate <conda:user-guide/cheatsheet>` ``a6``

    * On :xref:`Windows`, append ``"a6"`` to the
      ``"terminal.integrated.shellArgs.windows"`` setting from above:

      .. code-block:: json
         :emphasize-lines: 4

         {
             "terminal.integrated.shellArgs.windows": ["/K",
                 "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat",
                 "a6"],
         }

#. Install the :xref:`VS Code Python extension <VS-Code-Python-ext>`

#. If, for some reason, you don't want the :xref:`VS-Code-terminal` to
   automatically :std:doc:`activate <conda:user-guide/cheatsheet>` ``a6``, use
   the :xref:`command-pallete` to
   :xref:`select the intepreter <VS-Code-interpreter>` for ``a6``

   * This should add a setting for your machine-specific path to
     :xref:`settings.json <VS-Code-settings>`. If it is added to ``WORKSPACE
     SETTINGS`` in :xref:`settings.json <VS-Code-settings>`, make sure to
     put it in ``USER SETTINGS`` instead

    * On a :xref:`Mac`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "/Users/alnoki/miniconda3/envs/a6/bin/python"
        }

    * On :xref:`Windows`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\envs\\a6\\python.exe",
        }

   * You can also get this path by
     :std:doc:`activating<conda:user-guide/cheatsheet>` ``a6`` then
     typing :command:`which python`

To be continued...

.. tip::
   See :ref:`tools` or :ref:`references` if you want more information about
   the topics in this section

.. Next add Testing section, then Jupyter
