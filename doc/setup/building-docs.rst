######################
Building documentation
######################

#. Install :xref:`VS-Code` and the :xref:`VS-Code-bookmarks-ext`

#. Update the :xref:`VS-Code-terminal` ``USER SETTINGS`` in
   :xref:`settings.json <VS-Code-settings>` so that you can use
   :ref:`Conda <conda:starting-conda>`

   * On a :xref:`Mac`, add the following options to configure
     :xref:`bash login mode invocation<bash-man-page>`:

     .. code-block:: json

        {
            "terminal.integrated.shell.osx": "/bin/bash",
            "terminal.integrated.shellArgs.osx": [ "-l" ],
        }

   * On :xref:`Windows`, use the ``/K``
     :xref:`cmd.exe option <cmd.exe-invocation>` to run
     :ref:`Anaconda Prompt <conda:starting-conda>` (adapted for your username
     and machine):

     .. code-block:: json

        {
            "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
            "terminal.integrated.shellArgs.windows": ["/K",
                 "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat"],
        }

#. Use the :xref:`command-palette` to open a new :xref:`VS-Code-terminal` and
   enter the following command to
   :std:doc:`create a new conda environment <conda:user-guide/cheatsheet>`,
   ``a6``, that has the necessary :ref:`packages <tools>`

   .. code-block:: bash

      conda create --name a6 python conda pep8 sphinx sphinx_rtd_theme

#. Configure the :xref:`VS-Code-terminal` to automatically
   :std:doc:`activate <conda:user-guide/cheatsheet>` ``a6``

   * On a :xref:`Mac`, there is no :xref:`bash <bash-man-page>` equivalent to
     the ``/K`` :xref:`cmd.exe option <cmd.exe-invocation>`, so the easiest
     way to :std:doc:`activate <conda:user-guide/cheatsheet>` ``a6`` is to add
     the following line to :xref:`~/.bash_profile <bash-man-page>`, which will
     execute any time a :xref:`bash login mode <bash-man-page>` session starts
     (even outside of the
     :xref:`VS Code integrated terminal <VS-Code-terminal>`):

     .. code-block:: text

        # Activate a6 conda environment when bash login session starts
        source activate a6

   * On :xref:`Windows`, append ``"a6"`` to the
     ``"terminal.integrated.shellArgs.windows"`` setting from above:

     .. code-block:: json
        :emphasize-lines: 4

        {
            "terminal.integrated.shellArgs.windows": ["/K",
                "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat",
                "a6"],
        }


#. Install the :xref:`VS Code Python extension <VS-Code-Python-ext>` and use
   the :xref:`command-palette` to
   :xref:`select the intepreter <VS-Code-interpreter>` for ``a6``

   * This should add a setting for your machine-specific path to
     :xref:`settings.json <VS-Code-settings>`. If it is added to ``WORKSPACE
     SETTINGS`` in :xref:`settings.json <VS-Code-settings>`, make sure to
     put it in ``USER SETTINGS`` instead

   * On a :xref:`Mac`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "~/miniconda3/envs/a6/bin/python"
        }

   * On :xref:`Windows`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\envs\\a6\\python.exe",
        }

   * You can also get this path by
     :std:doc:`activating<conda:user-guide/cheatsheet>` ``a6`` then
     typing :command:`which python`

#. Use the :xref:`VS-Code-terminal` to install the :xref:`Doc8`:

   .. code-block:: bash

      conda install -c conda-forge doc8

#. Install the :xref:`RST-preview-ext` for :xref:`VS-Code`

#. If you don't already have it, :xref:`download Git <git-download>`

   * To figure out if you have it, open the :xref:`VS-Code-terminal` and type:

   .. code-block:: bash

      git --version

#. Install the :xref:`GitLens` for :xref:`VS-Code`

#. Use the :xref:`command-palette` to :xref:`clone <git-manual>` the
   :xref:`AAAAAA-repo`

   * This will include all of the
     :xref:`VS Code settings<VS-Code-settings>` that
     :xref:`alnoki <alnoki-repos>` uses

#. At this point you should be able to
   :ref:`build the documentaion <building-documentation>` and play around
   with the :ref:`reference management <managing-references>` features

Congratulations!!!