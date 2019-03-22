.. _procedures-napoleon:


########
Napoleon
########

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: Center
   :header: Reference, Topic

   :ref:`tools-napoleon`, Conceptual explanation

.. contents:: Contents
   :local:


*******************
Adding a new module
*******************

#. The first time you add a new :ref:`module <python:tut-modules>`, make sure
   to use :rst:dir:`automodule`, even if you don't want to describe everything
   it contains:

   .. code-block:: rest
      :caption: :py:mod:`AAAAAA.ledger`

      .. automodule:: AAAAAA.ledger
         :members: Transaction


   .. code-block:: rest
      :caption: :py:mod:`conf`

      .. automodule:: conf
         :no-members:

#. This way, the :ref:`module index <modindex>` will include the new
   :ref:`module <python:tut-modules>`


*****************************
Referencing Python components
*****************************

#. Use the :ref:`Python domain <sphinx:python-roles>` to create references:

   .. code-block:: rest
      :caption: :py:class:`AAAAAA.ledger.Transaction`

      :py:class:`AAAAAA.ledger.Transaction`

   .. code-block:: rest
      :caption: :py:data:`conf.html_theme_options`

      :py:data:`conf.html_theme_options`



*********************
Documenting variables
*********************

#. Use  :rst:dir:`autodata` to create :ref:`concepts-code-e4s` for
   :ref:`variables <python:tut-scopes>`, but make sure to use an empty
   ``annotation``
   :doc:`directive option <sphinx:usage/restructuredtext/basics>` if the
   :ref:`attribute <python:tut-scopes>` has a lot of
   :wiki-pg:`characters <Character_(computing)>` in the
   :wiki-pg:`source code <Source_code>`:

   .. code-block:: rest
      :emphasize-lines: 3
      :caption: Compare :py:data:`conf.html_theme` and
         :py:data:`conf.html_theme_options`

      .. autodata:: conf.html_theme
      .. autodata:: conf.html_theme_options
         :annotation:

   * This will prevent :wiki-pg:`rendering <Rendering_(computer_graphics)>`
     problems in the :ref:`PDF version <dist-doc-PDF>`

.. note::

   Make sure the :ref:`variable <python:tut-scopes>` has a
   :ref:`docstring <python:tut-docstrings>`, even if it is empty, otherwise
   you will get a :wiki-pg:`rendering <Rendering_(computer_graphics)>` problem
