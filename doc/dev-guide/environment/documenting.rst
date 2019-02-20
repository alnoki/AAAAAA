.. 0.3.0

.. _dev-env-documenting:


###########
Documenting
###########

#. Install :xref:`VS-Code` and the :xref:`VS-Code-bookmarks-ext`
#. Update the :xref:`VS-Code-terminal` ``USER SETTINGS`` in
   :xref:`settings.json <VS-Code-settings>` so that you can use
   :ref:`Conda <conda:starting-conda>`:

   * On a :xref:`Mac`, add the following options to configure
     :xref:`bash login mode invocation<bash-man-page>`:

     .. code-block:: json

        {
            "terminal.integrated.shell.osx": "/bin/bash",
            "terminal.integrated.shellArgs.osx": [ "-l" ],
        }

   * On :wiki-pg:`Windows <Microsoft_Windows>`, use the ``/K``
     :xref:`cmd.exe option <cmd.exe-invocation>` to run
     :ref:`Anaconda Prompt <conda:starting-conda>` (adapted for your username
     and :xref:`computer <computer>`):

     .. code-block:: json

        {
            "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
            "terminal.integrated.shellArgs.windows": ["/K",
                "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat"],
        }

     .. note::

        Be sure to :xref:`copy and paste <copy-paste>` the whole box! It may
        scroll to the right

#. Use the :xref:`command-palette` to open a new :xref:`VS-Code-terminal` and
   enter the following command to
   :doc:`create <conda:commands/create>` a new
   :ref:`conda environment <conda:concept-conda-env>`, called
   :term:`a6`, that has the necessary
   :ref:`packages <conda:concept-conda-package>`:

   .. code-block:: bash

      conda create --name a6 python conda pep8 sphinx sphinx_rtd_theme

#. Configure the :xref:`VS-Code-terminal` to automatically
   :ref:`activate <conda:activate-env>` the :term:`a6 evironment <a6>`:

   * On a :xref:`Mac`, there is no :xref:`bash <bash-man-page>` equivalent to
     the ``/K`` :xref:`cmd.exe option <cmd.exe-invocation>`, so the easiest
     way to :ref:`activate <conda:activate-env>` the
     :term:`a6 environment <a6>` is to add
     the following line to :xref:`~/.bash_profile <bash-man-page>`, which will
     execute any time a :xref:`bash login mode <bash-man-page>` session starts
     (even outside of the
     :xref:`VS Code integrated terminal <VS-Code-terminal>`):

     .. code-block:: text

        # Activate a6 conda environment when bash login session starts
        conda activate a6

   * On :wiki-pg:`Windows <Microsoft_Windows>`, append ``"a6"`` to the
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
   :xref:`select the intepreter <VS-Code-interpreter>` for :term:`a6`

   * This should add a setting for your machine-specific path to
     :xref:`settings.json <VS-Code-settings>`. If it is added to ``WORKSPACE
     SETTINGS`` in :xref:`settings.json <VS-Code-settings>`, make sure to
     put it in ``USER SETTINGS`` instead
   * On a :xref:`Mac`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "~/miniconda3/envs/a6/bin/python"
        }

   * On :wiki-pg:`Windows <Microsoft_Windows>`, this should look like:

     .. code-block:: json

        {
            "python.pythonPath": "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\envs\\a6\\python.exe",
        }

   * You can also get this path by
     :ref:`activating <conda:activate-env>` the :term:`a6 evironment <a6>` then
     typing :command:`which python`

#. Use the :xref:`VS-Code-terminal` to
   :doc:`install <conda:commands/install>` a few more
   :ref:`packages <conda:concept-conda-package>` that come from the
   :ref:`conda-forge <tools-anaconda>`:

   .. code-block:: bash

      conda install -c conda-forge doc8 sphinxcontrib-bibtex sphinx-autobuild

#. Install the :xref:`RST-preview-ext`
#. If you don't already have it, :xref:`download Git <git-download>`

   * To figure out if you have it, open the :xref:`VS-Code-terminal` and type:

     .. code-block:: bash

        git --version

#. Install the :xref:`GitLens`
#. Use the :xref:`command-palette` to :xref:`clone <git-clone>` the
   :xref:`AAAAAA-repo`

   * This will include all of the
     :xref:`VS Code settings<VS-Code-settings>` that
     :xref:`alnoki <alnoki-repos>` uses

#. At this point you should be able to
   :ref:`build the documentation <sphinx-building-documentation>` and play
   around with the :ref:`reference management <sphinx-managing-references>`
   features

Congratulations!!!
