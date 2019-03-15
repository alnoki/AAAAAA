.. 0.4.0

.. _dev-env-documenting:


###########
Documenting
###########

#. :xref:`Download VS code <VS-Code>` and get ready for some
   :vs-code-doc:`extensions <editor/extension-gallery>`
#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code Bookmarks extension <alefragnani.Bookmarks>`
#. Update the
   :vs-code-doc:`VS Code integrated terminal <editor/integrated-terminal>`
   ``USER SETTINGS`` in :vs-code-doc:`settings.json <getstarted/settings>` so
   that you can use :ref:`conda <conda:starting-conda>`:

   * On a :wiki-pg:`Mac <Macintosh_operating_systems>`, add the following
     options so you can use :linux-die:`bash login mode invocation <bash>`:

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

#. Use the
   :vs-code-doc:`VS Code Command Palette
   <getstarted/userinterface#_command-palette>` to open a new
   :vs-code-doc:`integrated terminal <editor/integrated-terminal>` and
   :xref:`copy and paste <copy-paste>` the following
   :wiki-pg:`command <Command_line>` to
   :doc:`create <conda:commands/create>` a new
   :ref:`conda environment <conda:concept-conda-env>`, called
   :term:`a6`, that has the necessary
   :ref:`packages <conda:concept-conda-package>`:

   .. code-block:: bash

      conda create --name a6 python conda pep8 sphinx sphinx_rtd_theme

#. :ref:`Configure <configs-vs-code>` the
   :vs-code-doc:`integrated terminal <editor/integrated-terminal>` to
   automatically :ref:`activate <conda:activate-env>` the
   :term:`a6 environment <a6>`:

   * On a :wiki-pg:`Mac <Macintosh_operating_systems>`, there is no
     :linux-die:`bash` equivalent to the ``/K``
     :xref:`cmd.exe option <cmd.exe-invocation>`, so the easiest way to
     :ref:`activate <conda:activate-env>` the :term:`a6 environment <a6>` is to
     add the following to :linux-die:`~/.bash_profile <bash>`, which will
     :wiki-pg:`execute <Execution_(computing)>` any time a
     :linux-die:`bash login mode <bash>` session starts (even outside of
     the :vs-code-doc:`integrated terminal <editor/integrated-terminal>`):

     .. code-block:: text

        # Activate a6 conda environment when bash login session starts
        conda activate a6

   * On :wiki-pg:`Windows <Microsoft_Windows>`, append ``"a6"`` to the
     ``"terminal.integrated.shellArgs.windows"``
     :ref:`setting <configs-vs-code>` from above:

     .. code-block:: json
        :emphasize-lines: 4

        {
            "terminal.integrated.shellArgs.windows": ["/K",
                "C:\\Users\\alnoki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat",
                "a6"],
        }

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code Python extension <ms-python.python>` and
   use the
   :vs-code-doc:`Command Palette <getstarted/userinterface#_command-palette>`
   to
   :vs-code-doc:`select the intepreter
   <python/environments#_select-and-activate-an-environment>` for :term:`a6`

   * This should add a :ref:`setting <configs-vs-code>` for your
     :wiki-pg:`computer <Computer>`-specific
     :wiki-pg:`path <Path_(computing)>` to
     :ref:`settings.json <configs-vs-code>`. If it is  added to
     ``WORKSPACE SETTINGS`` in :ref:`settings.json <configs-vs-code>`, make
     sure to put it in ``USER SETTINGS`` instead

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

   * You can also get this :wiki-pg:`path <Path_(computing)>` by
     :ref:`activating <conda:activate-env>` the :term:`a6 evironment <a6>` then
     :wiki-pg:`typing <Typing>` :command:`which python`

#. Use the :vs-code-doc:`integrated terminal <editor/integrated-terminal>` to
   :doc:`install <conda:commands/install>` a few more
   :ref:`packages <conda:concept-conda-package>` that come from the
   :ref:`conda-forge <tools-anaconda>`:

   .. code-block:: bash

      conda install -c conda-forge doc8 sphinxcontrib-bibtex sphinx-autobuild

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code reStructuredText extension
   <lextudio.restructuredtext>`
#. If you don't already have it, :git-scm:`download Git <downloads>`

   * To figure out if you have it, open the
     :vs-code-doc:`integrated terminal <editor/integrated-terminal>` and
     :wiki-pg:`type <Typing>`:

     .. code-block:: bash

        git --version

#. :wiki-pg:`Install <Installation_(computer_programs)>` the
   :vs-code-ext:`VS Code GitLens extension <eamodio.gitlens>`
#. Use the
   :vs-code-doc:`Command Palette <getstarted/userinterface#_command-palette>`
   to :git-doc:`git-clone` the :github:`AAAAAA repository <alnoki/AAAAAA>`

   * This will include all of the
     :ref:`VS Code settings <configs-vs-code>` that :github:`alnoki` uses

#. At this point you should be able to
   :ref:`build the documentation <sphinx-building-doc>` and play around with
   the :ref:`reference management <sphinx-managing-references>` features

Congratulations!!!
