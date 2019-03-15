.. 0.3.0

.. _procedures-pytest:

######
pytest
######

.. csv-table:: Select reference within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-pytest`, Conceptual explanation

.. _pytest-discover-tests:

*****************
Discovering tests
*****************

#. Verify that you can use :ref:`tools-pytest` in the
   :ref:`VS Code integrated terminal <tools-vs-code>` from inside the
   :ref:`AAAAAA project root directory <concepts-project-tree>`, using
   :term:`a6`

   .. code-block:: bash

      pytest

   * This should yield output that looks like the
     :doc:`pytest documentation <pytest:index>`

#. Use the :ref:`VS Code Command Palette <tools-vs-code>` to select
   :guilabel:`Python: Discover Unit Tests`

   #. If this fails, you may be experiencing a :xref:`pytest-discovery-issue`
      that is associated with a new :ref:`version <indices-versions>` of
      :ref:`tools-pytest`. You can either:

      #. Use the :xref:`VS Code Insider Edition <VS-Code-insiders>`, if a fix
         has recently been made available
      #. Temporarily use an older :term:`pop`:

         .. glossary::

            pop
               :term:`package <a6>`-o-:ref:`tools-pytest`, colloquially known
               as a *pop*

         #. :ref:`Activate <conda:activate-env>` the
            :term:`a6 environment <a6>`
         #. Use :doc:`conda:commands/install` with the appropriate
            :wiki-pg:`syntax <Syntax_(programming_languages)>` for the
            :ref:`version number <indices-versions>`, from the
            :doc:`conda cheatsheet <conda:user-guide/cheatsheet>`. For
            example:

            .. code-block:: bash

               conda install "pytest<=4.0.0"

#. Use the :ref:`VS Code Command Palette <tools-vs-code>` to select
   :guilabel:`Python: Discover Unit Tests`
#. Check out the
   :ref:`VS Code Test Explorer Extension <tools-vs-code>` to see if tests are
   showing up

