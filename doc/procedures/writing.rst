

#######
Writing
#######


*************************
Creating a directory tree
*************************

Adapted from :xref:`directory tree sample code <print-dir-tree>`:

#. Use the :xref:`VS Code command palette <command-palette>` to select
   :guilabel:`File: New Untitled File`

#. Copy-paste the below contents to the new file:

   .. code-block:: python

      import os

      base_indent = 4 * ' '
      branch_symbol = '|-> '
      where_to_start = '/Users/alnoki/Code/AAAAAA'

      for root, dirs, files in os.walk(where_to_start):
          level = root.replace(where_to_start, '').count(os.sep)
          if level > 0:
              indent = base_indent * (level - 1) + branch_symbol
          else:
              indent = ''
          print(f'{indent}{os.path.basename(root)}/')
          subindent = base_indent * (level) + branch_symbol
          for f in files:
              print(f'{subindent}{f}')

#. Modify ``base_indent`` and ``branch_symbol`` to symbols that you would like
   to have in your tree

#. Update ``where_to_start`` to the directory that you would like to write
   about

#. Highlight the text in the scratch file

#. Use the :xref:`command palette <command-palette>` to select
   :guilabel:`Python: Run Selection/Line in Python Terminal` then hit
   :kbd:`enter` from inside the
   :xref:`VS Code integrated terminal <VS-Code-terminal>`
