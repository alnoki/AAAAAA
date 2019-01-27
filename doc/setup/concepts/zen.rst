.. 5863379


###
Zen
###


*******************************************************************************************
Alnoki's Inspired Philosophies, Adopted and Implemented in Practice (AIP)\ :superscript:`2`
*******************************************************************************************

#. Silly acronyms actually help with remembering things
#. Testing and documenting up front prevents massive runtime debug headaches
#. Have DRY (don't repeat yourself) [#]_ code: decompose as much as possible
#. Documentation should enable another to re-write source and test code [#]_
#. Have STUPID simple tests. [#]_ Don't recursively "test the test code"
#. Documenting & testing adds perspective beyond source code development alone
#. Consider :xref:`DO-178B` as a model for software design assurance [#]_
#. :pep:`8` provides a repeatable and official means for formatting. Use it!!!
#. Legacy conventions shant prevent the adoption of a new worthwhile philosopy
#. Play around and "whiteboard" code during initial stages [#]_
#. Read documentation out loud [#]_
#. :xref:`Py <Python>` like you :ref:`reST <tools-restructured-text>`,
   :ref:`reST <tools-restructured-text>` like you :xref:`Py <Python>` [#]_


***************
Further reading
***************

Need some more inspiration? Try::

    import this

.. rubric:: Footnotes

.. [#] Acronym from :xref:`Corey Schafer <Corey-Schafer-vids>`
.. [#] From Software Requirements Documents (SWRDs) and Software Design
   Documents (SDDs) standards at :xref:`Garmin`
.. [#] From a tip that embedded systems code should be "stupid simple", given
   by Daniel Santos, co-founder of :xref:`219-Design`
.. [#] :xref:`AHRS` products from :xref:`Garmin` are
   :xref:`DO-178B Level A<DO-178B>`
.. [#] From a comment by Brett Glasner, that whiteboarding is the most
   fun part of software design
.. [#] Recommeded in :xref:`Willing-Sphinx`
.. [#] Adapted from Tom C. Bryan's suggestion (fly like you test, test like you
   fly) that flight testing and flight operations should be identical, to
   indicate that software development in practice should match procedural
   documentation
