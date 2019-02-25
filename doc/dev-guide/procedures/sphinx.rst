.. 0.3.0

.. _sphinx-procedures:


######
Sphinx
######

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-sphinx`, :term:`AAAAAA` conceptual explanation
   :yt-vid:`Practical Sphinx presentation <0ROZRNZkPS8>`, Common usage
   :yt-vid:`Project setup screencast <oJsUvBQyHBs>`, Start a project
   :doc:`Sphinx quickstart tutorial <sphinx:usage/quickstart>`, "Official
   tutorial"

.. contents:: Contents
   :local:

.. _sphinx-building-doc:


**********************
Building documentation
**********************

.. _sphinx-building-manually:

Manually
========

Per
:yt-vid:`Carol Willing's Practical Sphinx talk from PyCon 2018 <0ROZRNZkPS8>`:

#. :ref:`Activate <conda:activate-env>` the :term:`a6 environment <a6>` from
   inside the :ref:`documentation root directory<concepts-project-tree>` if it
   is not already :ref:`active <conda:activate-env>`
#. From the :ref:`VS Code integrated terminal <tools-vs-code>`, make the
   :wiki-pg:`HTML` for :wiki-pg:`documentation <Software_documentation>` then
   start a :doc:`server <python:library/http.server>`

   .. code-block:: bash

      make html
      python -m http.server

#. Open http://localhost:8000/_build/html/index.html in a
   :xref:`web browser <web-browser>` to view the :xref:`website <website>` for
   :wiki-pg:`documentation <Software_documentation>`
#. You can update the :ref:`.rst files <tools-restructured-text>` and repeat
   the process, but don't start another
   :doc:`server <python:library/http.server>` (unless you want an
   :xref:`http-socket-error`):

   .. code-block:: bash

      make html

#. Refresh the :xref:`browser <web-browser>` to see changes
#. Before :ref:`committing <git-committing>`, clear out the build:

   .. code-block:: bash

      make clean

.. tip::

   You can :ref:`automate this process <sphinx-autobuilding>` if you want quick
   updates, like if you are
   :ref:`proofreading documentation <writing-proofread>`

.. _sphinx-autobuilding:

Automatically
=============

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-sphinx-autobuild`, :term:`AAAAAA` conceptual description
   :xref:`sphinx-autobuild`, Official :wiki-pg:`user <User_(computing)>` manual

#. Like in the :ref:`manual build procedure <sphinx-building-manually>`,
   use the :term:`a6 environment <a6>` inside the
   :ref:`documentation root directory<concepts-project-tree>` via the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      sphinx-autobuild sphinx-autobuild . _build/html -B -s 1

   :xref:`sphinx-autobuild options <sphinx-autobuild>`:

      -B    Automatically open :xref:`browser <web-browser>`
      -s    :wiki-pg:`Delay <Time>` [#]_ before opening
            :xref:`browser <web-browser>`

   * This should automatically open a :xref:`web browser <web-browser>`
   * The :doc:`server <python:library/http.server>` should be at
     http://127.0.0.1:8000

#. Use :kbd:`control-c` to stop the :doc:`server <python:library/http.server>`
#. Keep in mind:

   * Once the :doc:`server <python:library/http.server>` is running,
     :wiki-pg:`saved <Computer_file>` changes to any
     :ref:`.rst files <tools-restructured-text>` should cause your
     :xref:`web browser <web-browser>` to update whatever part of the
     :xref:`website <website>` you are viewing
   * You will still need to manually navigate to the :xref:`webpage <webpage>`
     you want to view
   * If your :wiki-pg:`web browser <Web_browser>` is set to a :wiki-pg:`URL`
     that ends with ``.html``, the :xref:`webpage <webpage>` will
     :wiki-pg:`refresh <Web_browser>` in the same
     :wiki-pg:`vertical position <Scrolling>`, but you may not be granted this
     luxury if the :wiki-pg:`URL` ends with something like
     ``.html#a-heading-you-clicked-on``
   * For some reason, at least on a
     :wiki-pg:`Mac <Macintosh_operating_systems>`, you may need to
     :wiki-pg:`quit <Exit_status>` your :wiki-pg:`web browser <Web_browser>`,
     stop :ref:`tools-sphinx-autobuild` via :kbd:`control-c` and then re-do
     the above before the auto-:wiki-pg:`refresh <Web_browser>` behavior will
     work

.. rubric:: Footnotes

.. [#] If you try to use no :wiki-pg:`delay <Time>` at all, ``-s 0``, the
   :xref:`browser <web-browser>` might not open

.. _sphinx-managing-references:


*******************
Managing references
*******************

.. contents:: Contents
   :local:

.. _sphinx-intersphinx:

Using Intersphinx
=================

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-intersphinx`, :term:`AAAAAA` conceptual explanation
   :doc:`sphinx.ext.intersphinx <sphinx:usage/extensions/intersphinx>`, "
   Official :wiki-pg:`documentation <Software_documentation>`"
   ":stack-q:`Intersphinx reference syntax
   <45699577/how-to-link-to-root-page-in-intersphinx>`", "
   :wiki-pg:`Syntax <Syntax_(programming_languages)>` explanation"
   ":stack-q:`Intersphinx inventory parser
   <30939867/how-to-properly-write-cross-references-to-external-\
   documentation-with-intersphin>`", "For :ref:`linking <references-links>`
   to large projects"

#. Locate the project's
   :doc:`objects.inv <sphinx:usage/extensions/intersphinx>`
   mapping, using the :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      python -msphinx.ext.intersphinx http://www.sphinx-doc.org/en/master/objects.inv

   * You may have to experiment with the project base :xref:`URL <URL>`. Some
     common endings:

      * ``org/en/master/``
      * ``.io/en/latest/``
      * ``.com/en/latest/``

#. Add the project's base :xref:`URL <URL>` to the
   :py:data:`~conf.intersphinx_mapping`
   :ref:`dictionary <python:tut-dictionaries>` in
   :ref:`conf.py <tools-sphinx>`:

   .. code-block:: python

      intersphinx_mapping = {
         'python': ('https://docs.python.org/3', None),
         'sphinx': ('http://www.sphinx-doc.org/en/master/', None),
         'pytest': ('https://docs.pytest.org/en/latest/', None),
         'rtfd': ('https://docs.readthedocs.io/en/latest/', None),
         'rtd-sphinx-theme':
            ('https://sphinx-rtd-theme.readthedocs.io/en/latest/', None),
         ...

#. Inspect the :doc:`objects.inv mapping <sphinx:usage/extensions/intersphinx>`
   from the project in question

   * For large outputs, consider using a :xref:`command line <command-line>`
     instead of the :ref:`VS Code integrated terminal <tools-vs-code>` (but
     make sure to use :term:`a6`)

#. Locate the desired target in the output and :ref:`link <references-links>`
   to it using a corresponding
   :doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. csv-table:: Referencing select outputs
      :header: Category in objects.inv, Role to use
      :align: center

      ``std:doc``, ``:doc:``
      ``rst:directive``, ``:rst:dir:``
      ``std:label``, ``:ref:``

#. :xref:`Webpages <webpage>` of
   :wiki-pg:`documentation <Software_documentation>`, under ``std:doc``, are
   arranged like the project's
   :ref:`table of contents <sphinx:toctree-directive>`, so you can figure out
   the :doc:`role target <sphinx:usage/restructuredtext/roles>` from
   the :xref:`URL <URL>` that a :xref:`browser <web-browser>` displays for the
   particular :xref:`webpage <webpage>`. Consider
   https://docs.python.org/3/tutorial/introduction.html:

   .. csv-table:: :xref:`URL <URL>` decomposition
      :header: Portion, Interpretation, In role target
      :align: center

      ``https://docs.python.org/3/``, Base :wiki-pg:`URL`, ``python:``
      ``tutorial/introduction.html``, Desired :xref:`webpage <webpage>`, "
      ``tutorial/introduction``"

#. You can optionally define your own
   :doc:`role title <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest
      :caption: :doc:`python:tutorial/introduction`

      :doc:`python:tutorial/introduction`

   .. code-block:: rest
      :caption: :doc:`A most beauteous tutorial <python:tutorial/introduction>`

      :doc:`A most beauteous tutorial <python:tutorial/introduction>`

#. Add a description of the :xref:`link <URL>` to
   :ref:`links <references-links>`
#. Add a :doc:`role <sphinx:usage/restructuredtext/roles>` to
   :wiki-pg:`documentation <Software_documentation>` using the appropriate
   :ref:`capitalization <concepts-doc-style>`. For example:

   .. code-block:: rest

      Read about :doc:`Sphinx roles <sphinx:usage/restructuredtext/roles>`

.. note::

   When possible, use ``:ref:`` instead of ``:doc:``, because the project's
   :ref:`toctree <sphinx:toctree-directive>` may change

.. seealso::

   :stack-q:`Intersphinx with NumPy/Matplotlib
   <21538983/specifying-targets-for-intersphinx-links-to-numpy-scipy-and-\
   matplotlib>` has instructions for referencing
   :doc:`NumPy <numpy:about>` and :doc:`Matplotlib <matplotlib:index>`, though
   standard procedures from above are usually sufficient for :term:`AAAAAA`

.. _sphinx-reference-urls:

Referencing external links
==========================

For :ref:`links <references-links>` that can not be managed with
:ref:`Intersphinx <sphinx-intersphinx>`, use either :ref:`sphinx-xref` or
:ref:`sphinx-extlinks`. In general you can use :ref:`sphinx-xref`, but if the
:wiki-pg:`webpage <Webpage>` you want to :wiki-pg:`cite <Citation>` comes
from a :wiki-pg:`website <Website>` that you often use, it makes sense to use
:ref:`sphinx-extlinks`:

#. :wiki-pg:`Wikipedia articles <Wikipedia>`, like
   https://en.wikipedia.org/wiki/Download:

   .. code-block:: rest
      :caption: Resultant :doc:`role <sphinx:usage/restructuredtext/roles>`

      :wiki-pg:`Download`

#. :real-py:`RealPython tutorials <>`, like
   https://realpython.com/python-type-checking:

   .. code-block:: rest
      :caption: Resultant :doc:`role <sphinx:usage/restructuredtext/roles>`

      :real-py:`python-type-checking`

#. Even :xref:`Stack Overflow questions <stack-overflow>`, like
   :stack-q:`https://stackoverflow.com/questions/1441010/the-shortest-possible\
   -output-from-git-log-containing-author-and-date
   <1441010/the-shortest-possible-output-from-git-log-containing-author-and-\
   date>`:

   .. code-block:: rest
      :caption: Resultant :doc:`role <sphinx:usage/restructuredtext/roles>`

      :stack-q:`https://stackoverflow.com/questions/1441010/the-shortest-possible\
      -output-from-git-log-containing-author-and-date
      <1441010/the-shortest-possible-output-from-git-log-containing-author-and-\
      date>`

   * Note that this works, but there may not be
     :wiki-pg:`syntax highlighting <Syntax_highlighting>` in the above
     :rst:dir:`code-block` because of the ``\``-:wiki-pg:`escapes <Delimiter>`
     for :wiki-pg:`new lines <Newline>`
   * This is still in compliance with
     :ref:`line breaking standards <concepts-doc-whitespace>`

.. _sphinx-xref:

xref
----

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-xref`, :term:`AAAAAA` conceptual explanation
   :github:`Sphinx xref extension <michaeljones/sphinx-xref>`, "
   :wiki-pg:`User <User_(computing)>` manual"

#. Add your :xref:`URL <URL>` to the :py:data:`~conf.xref_links`
   :ref:`dictionary <python:tut-dictionaries>` in
   :ref:`conf.py <concepts-doc-tree>`, below the
   :wiki-pg:`delimeter <Delimiter>`-style :ref:`comment <python:comments>`
   that reads ``New links below, sorted links above``

     .. code-block:: python

        xref_links = {
            'Python': ('Python', 'https://www.python.org'),
            ...
            'semver': ("Semantic Versioning", 'https://semver.org/'),
            # New links below, sorted links above
            'ottobib': ('OttoBib', 'https://www.ottobib.com'),
        }

#. Add a :doc:`link role <sphinx:usage/restructuredtext/roles>` to
   :ref:`.rst files <tools-restructured-text>` using the appropriate
   :ref:`capitalization <concepts-doc-style>` and an optional
   :doc:`role title <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest
      :caption: :xref:`Python`

      :xref:`Python`

   .. code-block:: rest
      :caption: :xref:`Python.org <Python>`

      :xref:`Python.org <Python>`

#. Add a description of the :wiki-pg:`URL` to :ref:`links <references-links>`

   * After this step, the :xref:`URL <URL>` can be moved above the
     :wiki-pg:`delimiter <Delimiter>`-stye :ref:`comment <python:comments>`
     from :doc:`conf.py <sphinx:usage/configuration>`

.. admonition:: Optimality considerations

   * As long as :xref:`URLs <URL>` aren't put above the
     :wiki-pg:`delimiter <Delimiter>`-stye :ref:`comment <python:comments>`
     until after they are put into :ref:`links <references-links>`,
     :xref:`URLs <URL>` can be sorted in **reasonably sized** batches
   * If you put a :ref:`link <references-links>` in
     :ref:`.rst files <tools-restructured-text>` and in
     :ref:`links <references-links>` first, you can bypass the
     :wiki-pg:`delimiter <Delimiter>`-stye :ref:`comment <python:comments>`
     altogether when adding to :ref:`conf.py <tools-sphinx>`

.. _sphinx-extlinks:

extlinks
--------

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-extlinks`, :term:`AAAAAA` conceptual explanation
   :doc:`extlinks <sphinx:usage/extensions/extlinks>`, "Official
   :wiki-pg:`documentation <Software_documentation>`"
   ":ref:`Using a references extension
   <sublime-with-sphinx:use the external links extension>`", "
   Related :ref:`configuration <configs-conf-py>` and usage"

#. Add your base :wiki-pg:`URL` to the :py:data:`~conf.extlinks`
   :ref:`dictionary <python:tut-dictionaries>` in
   :ref:`conf.py <concepts-doc-tree>`, with a ``%s`` at the end:

   .. code-block:: python

      extlinks = {
          'wiki-pg': ('https://en.wikipedia.org/wiki/%s', ''),
          'real-py': ('https://realpython.com/%s', ''),
          ...
      }

#. After you have added the base :wiki-pg:`URL`, you will then have access to
   a new custom :doc:`role <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest
      :caption: Yields :wiki-pg:`Internet`

      :wiki-pg:`Internet`

   .. code-block:: rest
      :caption: Yields :wiki-pg:`download <Download>`

      :wiki-pg:`download <Download>`

   .. note::

      The :ref:`link checker <sphinx-checking-links>` is particular about
      capitalization for :wiki-pg:`Wikipedia`, so make sure to use
      the exact :wiki-pg:`string <String_(computer_science)>` from the end of
      the :wiki-pg:`URL`: ``Download``, not ``download``

#. For most :wiki-pg:`websites <Website>` other than :wiki-pg:`Wikipedia`, you
   will want to add in a
   :doc:`role title <sphinx:usage/restructuredtext/roles>`:

   .. code-block:: rest
      :caption: Yields :real-py:`python-type-checking`

      :real-py:`python-type-checking`

   .. code-block:: rest
      :caption: Yields :real-py:`type checking guide <python-type-checking>`

      :real-py:`type checking guide <python-type-checking>`

#. Add a description of the :wiki-pg:`URL` to :ref:`links <references-links>`,
   then add your custom :doc:`role <sphinx:usage/restructuredtext/roles>` to
   :wiki-pg:`documentation <Software_documentation>` using the appropriate
   :ref:`capitalization <concepts-doc-style>`

.. tip::

   Although you could use :ref:`sphinx-extlinks` to create a :wiki-pg:`URL`
   that is not actually associated with a :wiki-pg:`webpage <Webpage>`, the
   :ref:`link checking procedure <sphinx-checking-links>` will identify such
   errors

.. _sphinx-checking-links:

Checking links
==============

Per
:yt-vid:`Carol Willing's Practical Sphinx talk from PyCon 2018 <0ROZRNZkPS8>`:

#. From inside the
   :ref:`documentation root directory <concepts-doc-tree>`, use the
   :ref:`VS Code integrated terminal <tools-vs-code>`:

   .. code-block:: bash

      make linkcheck

.. _sphinx-update-labels:

Updating labels
===============

#. With an :ref:`active build running <sphinx-building-doc>`, open the
   :ref:`VS Code integrated terminal <tools-vs-code>` from inside the
   :ref:`documentation root directory <concepts-project-tree>`
#. Use :ref:`intersphinx <sphinx-intersphinx>` on ``_build/html/objects.inv``
   to inspect inspect :ref:`labels <sphinx:ref-role>` for :term:`AAAAAA`
#. Verify the proper :ref:`label style <concepts-doc-style>`
#. Update any :ref:`labels <sphinx:ref-role>` via the
   :ref:`VS code command palette <tools-vs-code>`:
   :guilabel:`Search: Replace in Files`

.. _sphinx-reference-book:

Referencing books
=================

.. csv-table:: Select references
   :header: Reference, Topic
   :align: center

   :ref:`tools-bibtex`, :term:`AAAAAA` conceptual explanation
   :xref:`book`, Information source
   :xref:`bibtex`, :xref:`citation` format
   :doc:`BibTeX extension <bibtex:index>`, Converts :xref:`bibtex`
   :xref:`ottobib`, "Get :xref:`bibtex` for your
   :ref:`book <references-books>`"
   :xref:`ISBN`, Unique identifier for :ref:`books <references-books>`
   :ref:`refs.bib <concepts-doc>`, "Collection of :xref:`bibtex`-style
   :xref:`citations <citation>`"
   :xref:`bibtex-syntax`, ":wiki-pg:`Syntax <Syntax_(programming_languages)>`
   specifications"
   :xref:`cite-multiple-authors`, Use of ``et. al``

#. Check :xref:`ottobib` for your :xref:`ISBN` and
   :xref:`copy-paste <copy-paste>` the :xref:`bibtex` option into
   :ref:`refs.bib <concepts-doc>`
#. Verify that you added a :xref:`book entry <bibtex-syntax>` in
   :ref:`refs.bib <concepts-doc-tree>`

   * A ``book`` :xref:`entry <bibtex-syntax>` requires at least ``author`` (or
     ``editor``), ``title``, ``publisher``, and ``year``
     :xref:`fields <bibtex-syntax>`
   * Consider
     :xref:`et. al conventions for multiple authors<cite-multiple-authors>`

#. Add a :ref:`role <sphinx:ref-role>` to :ref:`books <references-books>` via
   ``:cite:`bib-book-name```

   * Use a :ref:`heading <concepts-doc-example>` so that :rst:dir:`toctree` can
     index the entry

   * Use a :ref:`label <concepts-doc-style>` that starts with ``book-`` in
     :ref:`books <references-books>`, and with ``bib-`` in
     :ref:`refs.bib <concepts-doc-tree>`

   .. code-block:: rest
      :emphasize-lines: 1, 8

      .. _book-on-managing-yourself:


      ********************
      On Managing Yourself
      ********************

      .. csv-table:: :cite:`bib-on-managing-yourself`
         :header: Page(s), Topic
         :align: center

   .. code-block:: none
      :emphasize-lines: 1

      @Book{bib-on-managing-yourself,
       author = {Clayton M. Christensen et. al},
       title = {HBR's 10 Must Reads: On Managing Yourself},
       publisher = {Harvard Business Review Press},
       year = {2010},
       address = {Boston, Massachusetts},
       isbn = {978-1-4221-5799-2}
       }

.. tip::

   The :doc:`BibTeX extension <bibtex:index>` is unreceptive to
   :doc:`role titles <sphinx:usage/restructuredtext/roles>`
