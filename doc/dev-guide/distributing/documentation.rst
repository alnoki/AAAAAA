.. _dist-doc:


#############
Documentation
#############

.. csv-table:: Select references within :term:`AAAAAA`
   :align: center
   :header: Reference, Topic

   :ref:`tools-read-the-docs`, Conceptual explanation
   :ref:`tools-sphinx`, Conceptual explanation
   :ref:`Sphinx configurations <configs-sphinx>`, Options
   :ref:`RTD configurations <configs-read-the-docs>`, Options
   :ref:`Versioning <versioning-releasing>`, :term:`Checklist`

.. csv-table:: Select references
   :align: center
   :header: Reference, Topic

   :yt-vid:`Quickstart tutorial <oJsUvBQyHBs>`, "Start a
   :doc:`Read the Docs with Sphinx <rtfd:intro/getting-started-with-sphinx>`
   project"
   :doc:`Read the Docs build process <rtfd:builds>`, Generation process

:wiki-pg:`Documentation <Software_documentation>` for :term:`AAAAAA` was
initially created using the
:doc:`Read the Docs with Sphinx getting started guide
<rtfd:intro/getting-started-with-sphinx>`, which should have you on your way
if you want to create a similar :wiki-pg:`website <Website>`

.. contents:: Contents
   :local:

.. _dist-doc-create-project:


******************
Creating a project
******************

If you complete :doc:`sphinx-quickstart <sphinx:usage/quickstart>`, you'll have
a :ref:`tools-sphinx` project on your :wiki-pg:`computer <Computer>`, but
you'll need to
:doc:`set up GitHub integration <rtfd:intro/getting-started-with-sphinx>`
before your :wiki-pg:`documentation <Software_documentation>` shows up on the
:wiki-pg:`Internet`

If you decide to use any :ref:`tools-sphinx-extensions`, you'll need to
indicate them in :ref:`configs-conf-py`, and potentially in
:ref:`configs-requirements-txt` if they are not
:doc:`built-in extensions <sphinx:usage/extensions/index>`

.. _dist-doc-monitor-builds:


*****************
Monitoring builds
*****************

The :ref:`Sphinx procedures <procedures-sphinx>` describe how to
:ref:`build documentation <sphinx-building-doc>` on your
:wiki-pg:`computer <Computer>`, which you'll want to do as you write

Whenever you :ref:`commit <git-committing>`,
:ref:`tools-read-the-docs` will create a new :wiki-pg:`website <Website>` of
your :wiki-pg:`documentation <Software_documentation>`. On your
:xref:`rtfd-account`, it is important to become familiar with the
:doc:`builds <rtfd:builds>` monitoring interface at
:menuselection:`Projects --> AAAAAA --> Builds`. You should check this when you
are :ref:`releasing a new version <versioning-releasing>` at the very least,
and definitely whenever you use a new
:ref:`Sphinx extension <tools-sphinx-extensions>`

If you experience a failed :doc:`build <rtfd:builds>`, you probably just need
to update :ref:`configs-conf-py` or :ref:`configs-requirements-txt`


.. _dist-doc-versions:

*****************
Managing versions
*****************

As you :ref:`create development branches <versioning-start-new>`, you'll start
to :wiki-pg:`upload <Upload>` new sets of
:wiki-pg:`documentation <Software_documentation>` with every
:ref:`commit <git-committing>`, and you'll want to enable different
:doc:`versions <rtfd:versions>`. On your :xref:`rtfd-account`, you will need to
:wiki-pg:`navigate <Web_browser>` to
:menuselection:`Projects --> AAAAAA --> Versions` to enable the
:wiki-pg:`rendering <Rendering_(computer_graphics)>` of different
:ref:`tags and branches <tools-git>`

It is helpful to enable whatever
:ref:`development branch <versioning-start-new>` you are working on so that you
can see how it will actually appear in your :wiki-pg:`browser <Web_browser>`,
and as long as you use the suggested
:ref:`versioning procedures <versioning-start-new>`, only the last
:ref:`tagged version <git-tagging>` on the :xref:`master branch <git-manual>`
will be outwardly visible when you view your :wiki-pg:`website <Website>`

When you :ref:`merge <git-merging>`, it makes sense to disable the
:ref:`development branch <versioning-start-new>` you were just working on,
then :ref:`tag <git-tagging>` the new :ref:`version <indices-versions>` on the
:xref:`master branch <git-manual>` and enable it instead, so that your
:wiki-pg:`website <Website>` will show the latest
:ref:`version <indices-versions>`

.. _dist-doc-pdf:


**************
Creating a PDF
**************

:doc:`Read the Docs <rtfd:index>` will automatically create a :wiki-pg:`PDF`
of your :wiki-pg:`documentation <Software_documentation>` that you can access
from your :xref:`rtfd-account` at
:menuselection:`Projects --> AAAAAA --> Downloads`. The structural
layout is dictated by the :ref:`toctrees <tools-sphinx>` in your project and
by the :ref:`headings <concepts-doc-style>` in :py:data:`conf.master_doc`

The :wiki-pg:`website <Website>` is considered the primary way to view
:wiki-pg:`documentation <Software_documentation>` for :term:`AAAAAA`, but the
:wiki-pg:`PDF` is useful for measuring the
:ref:`amount of content generated for a version release <versions-stats>`. You
can also follow the :ref:`procedures to build a PDF <sphinx-building-pdf>` on
your computer if you are okay with :wiki-pg:`downloading <Download>` a
particularly large :wiki-pg:`LaTeX` library

Content is, of course, :wiki-pg:`rendered <Rendering_(computer_graphics)>`
differently in the :wiki-pg:`PDF` and in the :wiki-pg:`website <Website>`,
especially for:

* :rst:role:`guilabels <guilabel>` like :guilabel:`this`
* :ref:`tools-BibTeX`
* :ref:`concepts-code-e4`
* :wiki-pg:`URLs <URL>` in a
  :doc:`directive argument <sphinx:usage/restructuredtext/basics>` for a
  :ref:`csv-table <sphinx:table-directives>`
* The :ref:`automatic indices <indices-auto>`
