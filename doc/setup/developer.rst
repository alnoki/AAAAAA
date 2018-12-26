.. _dev_environment:


#######################
Development environment
#######################

Follow the steps in this section to reproduce the environment that
:xref:`alnoki <alnoki-repos>` uses to create :term:`AAAAAA`

.. tip::
   See :ref:`tools` or :ref:`references` if you want more information about
   what is going on in this section


***********
Documenting
***********

#. Install :xref:`VS-Code`
#. Update the :xref:`VS-Code-terminal` ``USER SETTINGS`` in
   :xref:`settings.json <VS-Code-settings>` so that you can use
   :std:doc:`conda:index`

   * On a :xref:`Mac`, add: ``"terminal.integrated.shell.osx": "/bin/bash"``

#. Use the :xref:`command-pallete` to open a new :xref:`VS-Code-terminal` and
   enter the following command to
   :std:doc:`create a new conda environment <conda:user-guide/cheatsheet>`
   (which will be called  ``a6``) that has necessary :ref:`packages <tools>`

   :command:`conda create --name a6 python pep8 sphinx sphinx_rtd_theme`

#. Install the :xref:`VS Code Python extension <VS-Code-Python-ext>` and use
   the :xref:`command-pallete` to
   :xref:`select the intepreter <VS-Code-interpreter>` for ``a6``

   * Equivalently, add a setting for your machine-specific path to
     :xref:`settings.json <VS-Code-settings>`, which will look like
     ``"python.pythonPath": "/Users/alnoki/miniconda3/envs/a6/bin/python"``
   * You can get this path by
     :std:doc:`activating<conda:user-guide/cheatsheet>` ``a6`` then
     typing :command:`which python`

To be continued...

.. Next add Testing section, then Jupyter
