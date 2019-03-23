.. _procedures-vs-code:


#######
VS Code
#######

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-vs-code`, Conceptual explanation

.. contents:: Contents
   :local:

.. _vs-code-manage-settings:


*****************
Managing settings
*****************

#. Use the :ref:`Command Palette <tools-vs-code>` to compare
   :ref:`configs-settings-json` against defaults:

   * :guilabel:`Preferences: Open Raw Default Settings`

.. _vs-code-max-screen-estate:


************************
Maximizing screen estate
************************

You may need to :ref:`modify settings <vs-code-manage-settings>` for some of
these to have an effect

#. For :vs-code-doc:`half-screen <getstarted/userinterface>`, use the
   :ref:`VS Code Command Palette <tools-vs-code>` to experiment with the
   following :wiki-pg:`commands <Command_line>`:

   * :guilabel:`View: Toggle Tab Visibility`
   * :guilabel:`View: Toggle Maximized Panel`
   * :guilabel:`View: Toggle Panel`
   * :guilabel:`View: Toggle Activity Bar Visibility`
   * :guilabel:`View: Toggle Side Bar Visibility`
   * :guilabel:`View: Toggle Status Bar Visibility`
   * :guilabel:`View: Toggle Centered Layout`
   * :guilabel:`View: Join All Editor Groups`
   * :guilabel:`View: New Editor Group to the Right`
   * :guilabel:`View: New Editor Group Below`
   * :guilabel:`View: Zoom In` (or ``Out``)
   * :guilabel:`Workspaces: Duplicate Workspace in New Window`
   * :guilabel:`Editor Font Zoom In` (or ``Out``)

#. For :vs-code-doc:`full-screen <getstarted/userinterface>`:

   * :guilabel:`View: Toggle Zen Mode`

.. _vs-code-markdown-headers:


*************************
Managing markdown headers
*************************

#. Use the
   :vs-code-doc:`VS Code symbol input
   <getstarted/userinterface#_command-palette>` to :wiki-pg:`type <Typing>`:

   * :guilabel:`view outline`

#. Use the :ref:`Command Palette <tools-vs-code>`:

   * :guilabel:`Fold level 2`
   * :guilabel:`Fold`

#. Use the :ref:`Vim extension <tools-vim>` to
   :xref:`go to an arbitrary line <Vim-cheatsheet>` and
   :xref:`delete <Vim-cheatsheet>` a
   :github-help:`Markdown heading level <basic-writing-and-formatting-syntax>`,
   then :xref:`put <Vim-cheatsheet>` it elsewhere

.. seealso::

   :ref:`versioning-td3`


********************
Improving efficiency
********************

#. Use the :ref:`VS Code Command Palette <tools-vs-code>` to experiment with
   the following :wiki-pg:`commands <Command_line>`:

   * :guilabel:`Focus Next Terminal`
   * :guilabel:`View: Keep Editor` (from closing)
   * :guilabel:`Bookmarks: Toggle`
   * :guilabel:`Bookmarks: Jump to Next`
   * :guilabel:`Bookmarks: Jump to Previous`
   * :guilabel:`Search: Replace in Files`
   * :guilabel:`Toggle Tab Key Moves Focus`
   * :guilabel:`Python Refactor: Sort Imports`


***************************
Configuring rulers and tabs
***************************

#. Determine the relevant :wiki-pg:`line break <Newline>` rule for your
   :ref:`code style <concepts-code-style>` or
   :ref:`documentation style <concepts-doc-style>`
#. While viewing the :wiki-pg:`filetype <Filename_extension>` in question, use
   the :ref:`Command Palette <tools-vs-code>` for inspection

   * :guilabel:`Change Language Mode`

#. With ``'x'`` corresponding to the :wiki-pg:`filetype <Filename_extension>`
   in question, select

   * :guilabel:`Configure 'x' language based settings...`

#. Update :ref:`configs-settings-json` in accordance with examples therein


***************
Changing colors
***************

.. contents::
   :local:

Basic interface components
==========================

#. Review the
   :vs-code-api:`token color customization <references/theme-color>` for the
   :ref:`setting <configs-settings-json>` you want to modify
#. Choose an :wiki-pg:`X11 color <Web_colors>` and add it to
   :ref:`configs-settings-json` like the rest of the examples therein

Specific syntax components
==========================

#. Use the :ref:`Command Palette <tools-vs-code>` to open the
   :github:`TextMate inspector <Microsoft/vscode/pull/29393>`

   * :guilabel:`Developer: Inspect TM Scopes`

#. :wiki-pg:`Click <Clicking>` on whatever
   :wiki-pg:`string <String_(computer_science)>` you are interested in
#. Update the resultant
   :github:`textMateRules <Microsoft/vscode/pull/29393>` in
   :ref:`configs-settings-json` with your desired
   :wiki-pg:`X11 color <Web_colors>`
