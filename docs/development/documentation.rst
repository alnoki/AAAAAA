#############
Documentation
#############


***************
Sphinx and reST
***************

Sphinx?
=======

:std:doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
is a documentation engine that helped create this website. See
:ref:`references` for more help on Sphinx

This :xref:`reST-cheatsheet` is a helpful quick syntax reference

Style
=====

Documentation is written primarily according to the
:std:doc:`Python Developer's Guide to Documenting Python <py-dev-guide:documenting>`
, and secondarily according to an
:std:doc:`Unofficial Read the Docs style guide for Sphinx <rtfd-style-guide:index>`
, with emphasis on:

   * Indent 3 spaces
   * Lines should be a maximum length of 79 characters
   * 2-line whitespace for the two top-level titles:

      .. code-block:: rest

          .. _reference-handle:


          ##############
          Document title
          ##############

          Welcome to this document!


          *******
          Section
          *******

          Welcome to this section!

          Subsection
          ==========

*****************
Jupyter Notebooks
*****************
:xref:`Jupyter Notebooks <Jupyter>` are used for an interactive style of
development and may be referenced throughout the documentation via direct links

This :xref:`AAAAAA-nbs` can render any :xref:`Jupyter Notebook<Jupyter>` from
:xref:`alnoki's AAAAAA repository <AAAAAA-repo>` in a web browser, and contains
a directory of all notebook in the project
