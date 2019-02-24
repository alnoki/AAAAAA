.. _concepts-configs:


##############
Configurations
##############

.. contents:: Contents
   :local:

.. _configs-git:


***
Git
***

.. _configs-gitconfig:

config
======

.. _configs-git-vim:

Vim
===

.. _configs-gitignore:

.gitignore
==========

.. _configs-sphinx:


******
Sphinx
******

.. _configs-conf-py:

conf.py
=======

.. csv-table:: Select references
   :header: Reference, topic
   :align: center

   :ref:`Sphinx <tools-sphinx>`, :term:`AAAAAA` conceptual explanation
   :ref:`tools-sphinx-extensions`, :term:`AAAAAA` functionality
   :doc:`sphinx-quickstart <sphinx:usage/quickstart>`, Official setup assistant
   :yt-vid:`Quickstart screencast <oJsUvBQyHBs>`, Video walkthrough
   :doc:`conf.py <sphinx:usage/configuration>`, ":ref:`Sphinx <tools-sphinx>`
   settings"

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
.. autodata:: conf.html_static_path

Website options
---------------

.. autodata:: conf.html_theme
.. autodata:: conf.html_theme_options

.. _configs-rtfd:


*************
Read the Docs
*************


.. _configs-requirements-txt:

requirements.txt
================

.. _configs-vs-code:


*******
VS Code
*******

.. _configs-settings-json:

settings.json
=============

.. _configs-pytest:


******
pytest
******

.. _configs-pytest-setup-py:

setup.py
========
