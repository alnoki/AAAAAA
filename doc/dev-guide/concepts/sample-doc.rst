:orphan:

.. 0.3.0

.. _sample-doc:


##########
Part title
##########

Welcome to this :wiki-pg:`file <Computer_file>`! Don't forget the two
:wiki-pg:`blank lines <Line_(text_file)>` above the
:doc:`overlined section heading <sphinx:usage/restructuredtext/basics>`!

You ready for a :doc:`list <sphinx:usage/restructuredtext/basics>`?

#. Item 1 (one :wiki-pg:`space <Whitespace_character>` after ``#.``)
#. Item 2 (no :wiki-pg:`vertical whitespace <Newline>` above)

   * Item 3 (needs :wiki-pg:`vertical whitespace <Newline>` above)
   * Item 4 (one :wiki-pg:`space <Whitespace_character>` after ``*``)

      * Item 5 (:wiki-pg:`indentated <Indentation_(typesetting)>` 3
        :wiki-pg:`spaces <Whitespace_character>`)


*************
Chapter title
*************

Welcome to this
:doc:`chapter <sphinx:usage/restructuredtext/basics>`! Don't forget the two
:wiki-pg:`blank lines <Line_(text_file)>` above the
:doc:`overlined section heading <sphinx:usage/restructuredtext/basics>`! [#]_

.. csv-table:: Reference, Topic example (NOT ``"Reference", "Topic"``)
   :header: Reference, Topic
   :align: center

   :ref:`concepts-doc-example`, "A
   :wiki-pg:`render <Rendering_(computer_graphics)>` of the
   :ref:`reST <tools-restructured-text>` for this :wiki-pg:`webpage <Webpage>`"
   :term:`OHIO`, :wiki-pg:`Development <Software_development>` philosophy [#]_

Section title
=============

Welcome to this :doc:`section <sphinx:usage/restructuredtext/basics>`! Only one
:wiki-pg:`blank line <Line_(text_file)>` needed above the
:doc:`section heading <sphinx:usage/restructuredtext/basics>`! Let's discuss
:ref:`documentation <concepts-doc>` (NOT ``:std:ref:`documentation
<concepts-doc>``) for :term:`AAAAAA`, which is a specific type of
:wiki-pg:`software documentation <Software_documentation>`

.. admonition:: How about this custom :xref:`admonition <admonition>`?

   Check out this :wiki-pg:`blank line <Line_(text_file)>` ^^

#. Item 1
#. Item 2

   .. note::

      Check out this the :wiki-pg:`indentation <Indentation_(typesetting)>`
      for this :doc:`directive <sphinx:usage/restructuredtext/directives>`,
      after a :doc:`list <sphinx:usage/restructuredtext/basics>`

   * Item 3

     .. tip::

        Because there is a ``*`` above, there is one less
        :wiki-pg:`space <Whitespace_character>` of
        :wiki-pg:`indentation <Indentation_(typesetting)>` for this
        :doc:`directive <sphinx:usage/restructuredtext/directives>`

Subsection title
----------------

Welcome to this :doc:`subsection <sphinx:usage/restructuredtext/basics>`! Only
one :wiki-pg:`blank line <Line_(text_file)>` needed above the
:doc:`section heading <sphinx:usage/restructuredtext/basics>`!

.. rubric:: Footnotes

.. [#] A :doc:`footnote <sphinx:usage/restructuredtext/basics>` from above.
   Notice how the :wiki-pg:`indentation <Indentation_(typesetting)>` starts
   after the :wiki-pg:`line break <Newline>`?
.. [#] Oh, so that's how you do multiple
   :doc:`footnotes <sphinx:usage/restructuredtext/basics>`. Check out the
   :wiki-pg:`blank line <Newline>` below
