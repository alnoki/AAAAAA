:orphan:

.. 0.3.0

.. _sample-doc:


##########
Part title
##########

Welcome to this :wiki-pg:`file <Computer_file>`! Don't forget the two
:wiki-pg:`blank lines <Line_(text_file)>` above the overline!

#. Item 1 (one space after '#.')
#. Item 2 (no vertical whitespace above)

   * Item 3 (needs vertical whitespace above)
   * Item 4 (one space after '*')

      * Item 5 (indented 3 spaces)


*************
Chapter title
*************

Welcome to this section! Don't forget the two
:wiki-pg:`blank lines <Line_(text_file)>` above the overline!! [#]_

.. csv-table:: Reference, Topic example (NOT "Reference", "Topic")
   :header: Reference, Topic
   :align: center

   :ref:`concepts-documentation-example`, This example
   :term:`OHIO`, Task management philosophy [#]_

Section title
=============

Welcome to this section. No double overline needed here! Let's talk about
:ref:`documentation <concepts-documentation>`
(NOT :std:ref:`documentation <concepts-documentation>`)

.. admonition:: How about this nice custom admonition?

   Check out this blank line ^^

#. Item 1
#. Item 2

   .. note::

      Check out this list directive indentation

   * Item 3

     .. tip::

        More list directive indentation

Subsection title
----------------

Welcome to this subsection. No double overline needed here!

.. rubric:: Footnotes

.. [#] Footnote from above. Notice how the
   indentation starts after the line break?
.. [#] Oh, so that's how you do multiple footnotes. Blank line down below
