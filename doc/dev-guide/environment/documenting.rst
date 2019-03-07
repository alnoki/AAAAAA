.. 0.3.0

.. _dev-env-documenting:


###########
Documenting
###########

#. :xref:`Download VS code <VS-Code>` and get ready for some
   :vs-code-doc:`extensions <editor/extension-gallery>`
#. :wiki-pg:`Install` the :xref:`VS-Code-bookmarks-ext`
#. Update the :xref:`VS-Code-terminal` ``USER SETTINGS`` in
   :vs-code-doc:`settings.json <getstarted/settings>` so that you can use
   :ref:`Conda <conda:starting-conda>`:

   * On a :wiki-pg:`Mac <Macintosh_operating_systems>`, add the following
     options so you can use :xref:`bash login mode invocation<bash-man-page>`:

     .. code-block:: json

        {
            "terminal.integrated.shell.osx": "/bin/bash",
            "terminal.integrated.shellArgs.osx": [ "-l" ],
        }

   * On :wiki-pg:`Windows <Microsoft_Windows>`, use the ``/K``
     :xref:`cmd.exe option <cmd.exe-invocation>` so you can use
     :ref:`Anaconda Prompt <conda:starting-conda>` (adapted for your
     :wiki-pg:`username <User_(computing)>` and
     :wiki-pg:`computer <Computer>`):

     .. code-block:: json

        {
            "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
            "terminal.integrated.shellArgs.windows": ["/K",
                "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat"],
        }

     .. note::

        Be sure to :xref:`copy and paste <copy-paste>` the whole box! It may
        :wiki-pg:`scroll <Scrolling>` to the right

#. Use the :xref:`command-palette` to open a new :xref:`VS-Code-terminal` and
   :xref:`copy and paste <copy-paste>` the following
   :wiki-pg:`command <Command_line>` to
   :doc:`create <conda:commands/create>` a new
   :ref:`conda environment <conda:concept-conda-env>`, called
   :term:`a6`, that has the necessary
   :ref:`packages <conda:concept-conda-package>`:

   .. code-block:: bash

      conda create --name a6 python conda pep8 sphinx sphinx_rtd_theme

#. Configure the :xref:`VS-Code-terminal` to automatically
   :ref:`activate <conda:activate-env>` the :term:`a6 evironment <a6>`:

   * On a :wiki-pg:`Mac <Macintosh_operating_systems>`, there is no
     :xref:`bash <bash-man-page>` equivalent to the ``/K``
     :xref:`cmd.exe option <cmd.exe-invocation>`, so the easiest way to
     :ref:`activate <conda:activate-env>` the :term:`a6 environment <a6>` is to
     add the following line to :xref:`~/.bash_profile <bash-man-page>`, which
     will :wiki-pg:`execute <Execution_(computing)>` any time a
     :xref:`bash login mode <bash-man-page>` session starts (even outside of
     the :xref:`VS Code integrated terminal <VS-Code-terminal>`):

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

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code Python extension <ms-python.python>` and
   use the :xref:`command-palette` to
   :xref:`select the intepreter <VS-Code-interpreter>` for :term:`a6`

   * This should add a setting for your :wiki-pg:`computer <Computer>`-specific
     :wiki-pg:`path <Path_(computing)>` to
     :vs-code-doc:`settings.json <getstarted/settings>`. If it is added to
     ``WORKSPACE SETTINGS`` in
     :vs-code-doc:`settings.json <getstarted/settings>`, make sure to put it in
     ``USER SETTINGS`` instead
   * On a :wiki-pg:`Mac <Macintosh_operating_systems>`, this should look like:

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
     :wiki-pg:`typing <Typing>` :command:`which python`

#. Use the :xref:`VS-Code-terminal` to
   :doc:`install <conda:commands/install>` a few more
   :ref:`packages <conda:concept-conda-package>` that come from the
   :ref:`conda-forge <tools-anaconda>`:

   .. code-block:: bash

      conda install -c conda-forge doc8 sphinxcontrib-bibtex sphinx-autobuild

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code reStructuredText extension
   <lextudio.restructuredtext>`
#. If you don't already have it, :xref:`download Git <git-download>`

   * To figure out if you have it, open the :xref:`VS-Code-terminal` and type:

     .. code-block:: bash

        git --version

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`GitLens extension <eamodio.gitlens>`
#. Use the :xref:`command-palette` to :git-doc:`git-clone` the
   :github:`AAAAAA repository <alnoki/AAAAAA>`

   * This will include all of the
     :vs-code-doc:`VS Code settings <getstarted/settings>` that
     :github:`alnoki` uses

#. At this point you should be able to
   :ref:`build the documentation <sphinx-building-doc>` and play around with
   the :ref:`reference management <sphinx-managing-references>` features

Congratulations!!!
