.. _concepts-configs:


##############
Configurations
##############

.. _concepts-configs-tree:

.. code-block:: none

   AAAAAA/
       a6.yml
       .gitignore
       .vscode/
           settings.json
       doc/
           conf.py
           requirements.txt
           exts/
               xref.py
       setup.py

.. contents:: Contents
   :local:

.. _configs-conda:


*****
Conda
*****

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-anaconda`, Conceptual explanation

a6.yml
======

:ref:`a6.yml <concepts-configs-tree>` specifies a
:ref:`conda environment <tools-anaconda>` that you will need to do
:wiki-pg:`development <Software_development>` for :term:`AAAAAA`. See the
:ref:`conda procedures <procedures-conda>` for more information on how to use
it

.. literalinclude:: ../../../a6.yml
   :language: yaml

.. _configs-git:


***
Git
***

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-git`, Conceptual explanation

.. _configs-gitconfig:

config
======

:xref:`git-config` helps store your :wiki-pg:`identity <User_(computing)>` the
way that you want it to appear in :ref:`the Git log <git-view-project-log>`,
and allows you to :ref:`use Vim <git-setup>`. The
:ref:`Git configuring procedures <git-configuring>` include precise
instructions on how to get started with :xref:`git-config`, which you shouldn't
need that often

.. _configs-gitignore:

.gitignore
==========

:git-doc:`.gitignore <user-manual.html#ignoring-files>` describes which
:wiki-pg:`files <Computer_file>` in the
:ref:`AAAAAA root directory <concepts-configs-tree>` do not need to be tracked
by :ref:`tools-Git`. It contains some
:wiki-pg:`comments <Comment_(computer_programming)>` to help separate content
into sections

.. _configs-vim:


***
Vim
***

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, topic

   :ref:`tools-vim`, Conceptual explanation

:xref:`Vim` is helpful for creating :ref:`commit messages <git-committing>`
from the :ref:`VS Code integrated terminal <tools-vs-code>`, and it comes with
:wiki-pg:`syntax highlighting <Syntax_highlighting>` that helps you figure out
if you are adhering to :xref:`Git commit guidelines <git-commit-guidelines>`.
This functionality is automatically enabled, except on a
:wiki-pg:`Mac <Macintosh_operating_systems>`, so the
:ref:`Git setup procedure <git-setup>` includes instructions to create a
:vim-wiki:`.vimrc file <Open_vimrc_file>` with the appropriate
:vim-wiki:`contents <Turn_on_syntax_coloring_in_Mac_OS_X>` if you are using a
:wiki-pg:`Mac <Macintosh_operating_systems>`

:xref:`Vim` is also
:ref:`recommended as an extension to VS Code <dev-env-contributing>`, and
its :ref:`configuration <concepts-configs>` is described in
:ref:`configs-settings-json`

.. _configs-vs-code:


*******
VS Code
*******

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, topic

   :ref:`tools-vs-code`, Conceptual explanation

.. _configs-settings-json:

settings.json
=============

:ref:`tools-vs-code` has both
:vs-code-doc:`user and workspace settings <getstarted/settings>`. For the most
part, you will only have to modify the
:ref:`AAAAAA workspace settings <concepts-configs-tree>` except for when you
are first :ref:`setting up the development environment <dev-env-intro>`

Workspace
---------

See the :ref:`VS Code procedures <procedures-vs-code>` for more information
about how to view the :ref:`AAAAAA workspace settings <concepts-configs-tree>`
and an interpretation of a few specific options

The :ref:`AAAAAA workspace settings <concepts-configs-tree>` are separated
into categories with :wiki-pg:`comments <Comment_(computer_programming)>`. For
consistency, :wiki-pg:`X11 color names <Web_colors>` are used

User
----

You may have to use the :ref:`developer environment setup <dev-env-intro>` to
get a few key :vs-code-doc:`user settings <getstarted/settings>` correct, but
for the most part they are not needed because they will be
:vs-code-doc:`overrided by workspace settings <getstarted/settings>` if you are
:wiki-pg:`developing <Software_development>` for :term:`AAAAAA`

.. note::

   The :vs-code-ext:`Vim extension <vscodevim.vim>` can change a few
   :vs-code-doc:`user settings <getstarted/settings>` throughout usage if you
   use the ``vim.statusBarColorControl`` option, don't worry about this

.. _configs-sphinx:


******
Sphinx
******

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, topic

   :ref:`tools-sphinx`, Conceptual explanation

.. csv-table:: Select references
   :align: center
   :header: Reference, topic

   :doc:`sphinx-quickstart <sphinx:usage/quickstart>`, Official setup assistant
   :yt-vid:`Quickstart screencast <oJsUvBQyHBs>`, Video walkthrough
   :doc:`conf.py <sphinx:usage/configuration>`, ":ref:`Sphinx <tools-sphinx>`
   settings"

.. _configs-conf-py:

conf.py
=======

If you create a :ref:`Sphinx project <tools-sphinx>` using
:doc:`sphinx-quickstart <sphinx:usage/quickstart>`, you will end up
with a ``conf.py`` :wiki-pg:`file <Computer_file>` in your
:ref:`documentation root directory <concepts-doc-tree>`. For
:term:`AAAAAA`, most of the default
:doc:`Sphinx configuration options <sphinx:usage/configuration>` from
:doc:`sphinx-quickstart <sphinx:usage/quickstart>` are used, but there are some
additions and modifications. The :doc:`conf.py <sphinx:usage/configuration>`
in :term:`AAAAAA` has also been shuffled around a bit so that it can be
logically explained here

Because :doc:`conf.py <sphinx:usage/configuration>` is a ``.py``
(:ref:`Python <tools-python>`) :wiki-pg:`file <Computer_file>`, it can be
explained using the :rst:dir:`literalinclude`
:doc:`directive <sphinx:usage/restructuredtext/directives>` and
:ref:`napoleon <tools-napoleon>`. For the most part,
:doc:`conf.py <sphinx:usage/configuration>` is a collection
of :ref:`module-level global variables <python:tut-modules>`.
Starting from the beginning of the :wiki-pg:`file <Computer_file>`:

.. automodule:: conf
   :no-members:

.. contents:: Contents
   :local:

Extensions
----------

.. literalinclude:: ../../conf.py
   :caption: :wiki-pg:`Path <Path_(computing)>` setup
   :language: python
   :lines: 1-5

Relative to the :ref:`documentation root directory <concepts-doc-tree>`, this
gives :ref:`tools-sphinx` access to the following
:wiki-pg:`paths <Path_(computing)>`:

.. csv-table::
   :align: center
   :header: :wiki-pg:`Path <Path_(computing)>`, Purpose

   ``exts``, Contains :ref:`tools-xref`
   ``../src``, "Where :ref:`napoleon <tools-napoleon>` checks for
   :ref:`source code <concepts-code-tree>`"
   ``.``, "Allows :ref:`napoleon <tools-napoleon>` to access
   :doc:`conf.py <sphinx:usage/configuration>`"

.. autodata:: conf.extensions
   :annotation:

AAAAAA project info
-------------------

.. autodata:: conf.project
.. autodata:: conf.copyright
.. autodata:: conf.author
.. autodata:: conf.version
.. autodata:: conf.release

File handling
-------------

.. autodata:: conf.master_doc
.. autodata:: conf.exclude_patterns
   :annotation:
.. autodata:: conf.html_static_path

Website
-------

.. autodata:: conf.html_theme
.. autodata:: conf.html_theme_options
   :annotation:
.. autodata:: conf.linkcheck_ignore
   :annotation:

Document generation
-------------------

These were created during :doc:`sphinx-quickstart <sphinx:usage/quickstart>`,
and have not been modified. See :ref:`conf.py <concepts-configs-tree>` for the
original :ref:`comments <python:comments>` that were generated by
:doc:`sphinx-quickstart <sphinx:usage/quickstart>`

Per the :ref:`napoleon procedures <procedures-napoleon>`, these have empty
:ref:`docstrings <python:tut-docstrings>`

.. autodata:: conf.htmlhelp_basename
   :annotation:
.. autodata:: conf.latex_elements
   :annotation:
.. autodata:: conf.latex_documents
   :annotation:
.. autodata:: conf.man_pages
   :annotation:
.. autodata:: conf.texinfo_documents
   :annotation:
.. autodata:: conf.epub_title
   :annotation:
.. autodata:: conf.epub_exclude_files
   :annotation:

Link management
---------------

.. autodata:: conf.intersphinx_mapping
   :annotation:
.. autodata:: conf.extlinks
   :annotation:
.. autodata:: conf.xref_links
   :annotation:

.. _configs-read-the-docs:


*************
Read the Docs
*************

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-read-the-docs`,  Conceptual explanation

.. _configs-requirements-txt:

requirements.txt
================

Some of the :ref:`tools-sphinx-extensions` used in :term:`AAAAAA` are not
:doc:`built-in <sphinx:usage/extensions/index>`, so the
:wiki-pg:`remote computer <Host_(network)>` that performs the
:doc:`Read the Docs build process <rtfd:builds>` needs information on how to
use them

Unlike the :term:`a6 conda environment <a6>` which uses
:ref:`conda packages <conda:concept-conda-package>`, the
:doc:`Read the Docs builder <rtfd:builds>` uses a
:ref:`requirements file <pypa:requirements files>` that indicates which
:ref:`PyPI packages <tools-pypi>` to :wiki-pg:`download <Download>`

Because :ref:`tools-xref` is not on the :ref:`tools-pypi`, it is simply
included in the :ref:`exts directory <concepts-configs-tree>` of the
:ref:`documentation root directory <concepts-doc-tree>`. Other
:ref:`Sphinx extensions that are not built-in <tools-sphinx-exts-extra>`,
however, must be specified in :ref:`requirements.txt <concepts-configs-tree>`:

.. literalinclude:: ../../requirements.txt
   :caption: :ref:`requirements.txt <concepts-configs-tree>`

On your :xref:`rtfd-account`, you will need to
:wiki-pg:`navigate <Web_browser>` to
:menuselection:`Projects --> AAAAAA --> Admin --> Advanced Settings` and update
``Requirements file:`` with the :wiki-pg:`path <Path_(computing)>` of
:ref:`requirements.txt <concepts-configs-tree>`

.. _configs-pytest:


******
pytest
******

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-pytest`, Conceptual explanation

.. _configs-pytest-setup-py:

setup.py
========

Per :doc:`official pytest recommendations <pytest:goodpractices>`, the
:ref:`AAAAAA project directory <concepts-project-tree>` contains a
:doc:`setup.py file <pypa-guide:tutorials/packaging-projects>` outside of both
:ref:`source and test code directories <concepts-code-tree>`, with the
:doc:`minimum available content <pytest:goodpractices>`:

.. literalinclude:: ../../../setup.py
   :caption: :ref:`AAAAAA/setup.py <concepts-configs-tree>`
   :language: python

This enables :ref:`pytest discovery <pytest-discover-tests>`
