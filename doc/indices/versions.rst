.. 0.3.0

.. _indices-versions:


########
Versions
########

:xref:`Versions <semver>` of :term:`AAAAAA` are numbered in accordance with
:xref:`semantic versioning standards <semver>`, using
:wiki-pg:`ISO 8601 extended format <ISO_8601>` and
:wiki-pg:`UTC <Coordinated_Universal_Time>` for
:wiki-pg:`time standards <Time_standard>`

.. centered:: ``MAJOR.MINOR.PATCH`` (``YYYY-MM-DD``\ T\ ``HH:MM:SS``\ Z)

:ref:`versions-features` are relevant to both :ref:`users <user-intro>` and
:ref:`developers <dev-intro>` alike, and usually include a relevant
:wiki-pg:`link <URL>` to somewhere in :term:`AAAAAA`. Modifications are
explained in a way that
:xref:`tells the codebase what to do <commit-conventions>`, like in
:ref:`commit messages <git-committing>`

:ref:`versions-stats` help measure the creation of content throughout the
:wiki-pg:`development <Software_development>` of :term:`AAAAAA`

.. contents:: Contents
   :local:

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :xref:`semver`, Numbering standards
   :xref:`git-commit-guidelines`, Long version message guidelines
   :wiki-pg:`ISO 8601<ISO_8601>`, :wiki-pg:`Time standards <Time_standard>`

.. tip::

   If you manage your own :ref:`Python package <python:tut-packages>` and you
   want to know how this is done, see the
   :ref:`versioning procedures <procedures-versioning>`

.. _versions-features:

********
Features
********

* 0.4.0

   * Add to :ref:`toctrees <tools-sphinx>`:

     * :ref:`examples`
     * :ref:`Developer guide intro <dev-intro>`
     * :ref:`Testing section <testing-intro>`
     * :ref:`Distribution section <dist-intro>`
     * :ref:`Documentation distribution guide <dist-doc>`
     * :ref:`concepts-configs`
     * :ref:`Contributing setup <dev-env-contributing>`
     * :term:`AAACCC`
     * :ref:`Version statistics <versions-stats>`
     * :ref:`Indices section <indices-intro>`
     * :ref:`VS Code procedures <procedures-vs-code>`
     * :ref:`Napoleon procedures <procedures-napoleon>`

   * Add to :ref:`tools section <concepts-tools>`:

     * :ref:`tools-google`
     * :ref:`tools-vim`

   * Integrate :ref:`tools-vim` with :ref:`tools-vs-code` and recommend during
     :ref:`developer environment setup <dev-env-intro>`
   * Add :ref:`PDF vs Website explanation <what-next-format>`
   * Add :ref:`tools-extlinks` support and :ref:`procedures <sphinx-extlinks>`
   * Add :term:`checklist` explanation from :ref:`book-checklist-manifesto`
   * Define :wiki-pg:`time standards <Time_standard>` for
     :ref:`versions <indices-versions>`
   * Add :ref:`reST syntax <tools-restructured-text>` to
     :ref:`sample-doc <sample-doc>`
   * Add explanation of :ref:`configs-conf-py` via
     :ref:`napoleon <tools-Napoleon>`, and assorted other
     :ref:`configurations <concepts-configs>`


* 0.3.1 (2019-02-17T19:41:19Z)

   * Fix broken :ref:`tools-read-the-docs` integration

* 0.3.0 (2019-02-17T18:45:27Z)

   * Restructure :ref:`toctrees <tools-sphinx>`
   * Add :ref:`versioning procedures <procedures-versioning>`
   * Add :ref:`BibTeX <tools-bibtex>` to create :xref:`citations <citation>`
     for :ref:`books <references-books>`
   * Add :ref:`tools-sphinx-autobuild` support and associated
     :ref:`procedures <sphinx-autobuilding>`
   * Add :ref:`the spirit of alnoki's apps <zen-spirit>`

* 0.2.0 (2019-02-09T05:24:35Z)

   * Add :wiki-pg:`documentation <Software_documentation>` for
     :py:class:`AAAAAA.ledger.Transaction` via :ref:`napoleon <tools-napoleon>`

* 0.1.0 (2019-01-31T02:57:50Z)

   * Create :xref:`website <website>`, using :ref:`tools-sphinx`, with notes on
     how to make a :xref:`website <website>`, using :ref:`tools-sphinx`!


.. _versions-stats:

**********
Statistics
**********

.. glossary::

   AAA
      Aggregate :term:`Acronym <AAACCC>` Accrual (A\ :superscript:`3`), the
      total count of :term:`alnoki's acks <AAACCC>`, helps measure the creation
      of memory aids in :term:`AAAAAA`

   PPP
      :wiki-pg:`PDF Page <PDF>` Proliferation (P\ :superscript:`3`), the
      number of :wiki-pg:`pages <PDF>` in
      :ref:`auto-generated documentation PDFs <dist-doc-pdf>`, helps
      measure the amount of content in a
      :ref:`version <versions-features>`

.. csv-table:: :ref:`Version <versions-features>` statistics
   :file: ../../nbs/doc/version-stats.csv
   :align: center
   :header-rows: 1
