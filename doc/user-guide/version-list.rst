.. 0.3.0

.. _version-list:


############
Version list
############

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :xref:`semver`, Numbering standards
   :xref:`git-commit-guidelines`, Long version message guidelines
   :wiki-pg:`ISO 8601<ISO_8601>`, :wiki-pg:`Time standards <Time_standard>`
   :ref:`versioning-procedures`, :term:`AAAAAA` usage

Below is a list of versions of :term:`AAAAAA`, numbered in accordance with
:xref:`semantic versioning standards <semver>`. :wiki-pg:`Times <Time>` are
described using :wiki-pg:`ISO 8601 extended format <ISO_8601>` and
:wiki-pg:`UTC <Coordinated_Universal_Time>`, two common
:wiki-pg:`time standards <Time_standard>`:

.. centered:: ``MAJOR.MINOR.PATCH`` (``YYYY-MM-DD``\ T\ ``HH:MM:SS``\ Z)

Features below are relevant to both :ref:`users <user-intro>` and
:ref:`developers <dev-intro>` alike, and usually include a relevant
:wiki-pg:`link <URL>` to somewhere in :term:`AAAAAA`. Modifications are
explained in a way that
:xref:`tells the codebase what to do <commit-conventions>`, like in
:ref:`commit messages <git-committing>`

.. tip::

   If you manage your own :ref:`Python package <python:tut-packages>` and you
   want to know how this is done, see the
   :ref:`versioning procedures <versioning-procedures>`

* 0.4.0

   * Add to :ref:`toctrees <tools-sphinx>`: :ref:`examples <examples>`,
     :ref:`developer guide intro <dev-intro>`,
     :ref:`testing intro <testing-intro>`,
     :ref:`distribution intro <dist-intro>`
   * Add :ref:`tools-extlinks` support and :ref:`procedures <sphinx-extlinks>`
   * Add :term:`checklist` explanation from :ref:`book-checklist-manifesto`
   * Define :wiki-pg:`time standards <Time_standard>` for
     :ref:`versions <version-list>`
   * Add :ref:`reST syntax <tools-restructured-text>` to
     :ref:`sample-doc <sample-doc>`

* 0.3.1 (2019-02-17T19:41:19Z)

   * Fix broken :ref:`tools-read-the-docs` integration

* 0.3.0 (2019-02-17T18:45:27Z)

   * Restructure :ref:`toctrees <tools-sphinx>`
   * Add :ref:`versioning procedures <versioning-procedures>`
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
