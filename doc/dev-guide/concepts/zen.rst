.. _zen:


###
Zen
###

.. _zen-aipaip:

*******************************************************************************************
Alnoki's Inspired Philosophies, Adopted and Implemented in Practice (AIP)\ :superscript:`2`
*******************************************************************************************

#. Silly :ref:`acronyms <indices-acronyms>` actually make it easy to remember
   things
#. :ref:`Test <testing-intro>` and :ref:`document <user-intro>` from the
   beginning to prevent massive runtime debug headaches
#. Have DRY (don't repeat yourself) [#]_ :ref:`code <tools-python>`: decompose
   as much as possible
#. :wiki-pg:`Documentation <Software_documentation>` should enable another to
   re-create :ref:`source <user-intro>` and :ref:`test code <testing-intro>`
   [#]_
#. Have STUPID simple :ref:`tests <testing-intro>`. [#]_ Don't recursively
   ":ref:`test <testing-intro>` the :ref:`test code <testing-intro>`"
#. :wiki-pg:`Documenting <Software_documentation>` and
   :ref:`testing <testing-intro>` adds perspective beyond the
   :ref:`development <dev-intro>` of :ref:`source code <user-intro>` alone
#. Consider :wiki-pg:`DO-178B` as a model for :wiki-pg:`software <Software>`
   design assurance [#]_
#. Legacy conventions shant prevent the adoption of a new worthwhile philosopy
#. Play around and "whiteboard" :wiki-pg:`software <Open-source_software>`
   during initial :wiki-pg:`development <Software_development>` [#]_
#. Read :wiki-pg:`documentation <Software_documentation>` out loud [#]_
#. :ref:`Py <tools-python>` like you :ref:`reST <tools-restructured-text>`,
   :ref:`reST <tools-restructured-text>` like you
   :ref:`Py <tools-python>` [#]_
#. "We, the :wiki-pg:`coders <Programmer>`, are foreigners, seeking citizenship
   in the :xref:`computer <computer>`’s locale" [#]_, so respect the house
   rules
#. Your legacy is the :wiki-pg:`documentation <Software_documentation>`
#. Make content for yourself because you like it [#]_
#. :xref:`Quality trumps quantity <quantity-trumps-quality>` when you are
   creating content, so just keep creating


.. _zen-spirit:

***************************
The spirit of alnoki's apps
***************************

#. :wiki-pg:`Open-source <Open-source_software>`, ``d00d``
#. :ref:`concepts-tools` should be :xref:`free <money>`, otherwise,
   make them yourself [#]_
#. When in doubt, :ref:`link <references-links>` (or you might forget later)
#. If you are :ref:`proofreading <writing-proofread>`, enjoy the content and
   *go slow* [#]_
#. Like in life, there are a lot of things :ref:`to do <versioning-td3>`, so
   :term:`OHIO`
#. :pep:`8` provides a repeatable and official means for formatting. Use it!!!
#. Write :doc:`functional programs <python:howto/functional>`, which should be
   easy to understand and test
#. Add content to :ref:`versions <indices-versions>` incrementally, like you
   are making a :xref:`mvp-development`
#. Add an ``index.rst`` in
   :ref:`documentation directories <concepts-doc-tree>` so you can find what
   you are looking for

***************
Further reading
***************

Need some more inspiration? Try::

    import this

.. rubric:: Footnotes

.. [#] Acronym from :yt-pl:`Corey Schafer <-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU>`
.. [#] From :wiki-pg:`Software` Requirements Documents (SWRDs) and
   :wiki-pg:`Software` Design Documents (SDDs) standards at :wiki-pg:`Garmin`
.. [#] From a tip that embedded systems :wiki-pg:`code <Software>` should be
   "stupid simple", given by Daniel Santos, co-founder of :xref:`219-Design`
.. [#] :wiki-pg:`AHRS <Attitude_and_heading_reference_system>` products from
   :wiki-pg:`Garmin` are :wiki-pg:`DO-178B Level A <DO-178B>`
.. [#] From a comment by Brett Glasner, that whiteboarding is the most
   fun part of :wiki-pg:`software <Software>` design
.. [#] Recommeded in
   :yt-vid:`Carol Willing's Practical Sphinx talk from PyCon 2018
   <0ROZRNZkPS8>`
.. [#] Adapted from advice given by Tom C. Bryan of the :xref:`msfc-lab` (*fly
   like you test, test like you fly*) that flight testing and flight operations
   should be identical - to indicate that
   :wiki-pg:`software development <Software_development>` in practice should
   match :ref:`procedural documentation <procedures>`
.. [#] From :xref:`why-poignant-guide`
.. [#] From a :xref:`Corey Schafer interview <schafer-interview>`: *I believe
   the most important lesson I’ve learned is that you should make content for
   yourself*
.. [#] Taken from various elements in a :xref:`torvalds-interview`
.. [#] Mantra of :xref:`caye-caulker`
