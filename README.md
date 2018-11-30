# AAAAAA
Alnoki's Algorithmic Analysis Asset Allocation Applications

*Brought to you by alnoki*

[AAAAAA documentation](https://alnoki.rtfd.io) is hosted at
[Read the Docs](https://rtfd.io), but below are some additional notes
that are kept locally during developement

## Design procedures
1. Update `docs` for `test` and `src` after incremental developments
1. pytest with the VS Code debugger
1. Write tests and design source code in cyclical stages
    1. C-style/speed-optimal source code with repeat code as necessary
    1. Design test code without any clever tricks (STUPID simple)
    1. Rearrange source code for maximal decomposition, not speed
    1. Update `docs` for `test` and `src` after the incremental
    development
    1. Optimize for speed only when needed

## Recommended documentation review order
As documentation was written, various Python terms were explained with
hyperlinks so as to provide a means for teaching. To review
documentation in a sequential order that will elucidate various
concepts throughout the software architecture, it is suggested that
documentation be read in the order in which it was written:
1. `nbs`\\`dev`\\`ledger`
1. `nbs`\\`src`\\`ledger`
1. `nbs`\\`src`\\`utilities`

## TODO
1. Intersphinx usage: make a task cheatsheet using below references
    1. https://my-favorite-documentation-test.readthedocs.io/en/latest/using_intersphinx.html
    1. https://stackoverflow.com/questions/30939867
    1. https://gist.github.com/bskinn/0e164963428d4b51017cebdb6cda5209
    1. https://stackoverflow.com/questions/21538983
    1. https://stackoverflow.com/questions/45699577
    1. http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#showing-all-links-of-an-intersphinx-mapping-file
1. Migrate readme to Sphinx
1. Get intersphinx working with additional sites
    1. Official Spinx documentation and
    1. http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-pep
    1. Python official tutorial
    1. Python developer's guide
    1. pytest documentation homepage
    1. [VS Code Python tutorial](https://code.visualstudio.com/docs/languages/python)
    1. [VS Code unit testing documentation](https://code.visualstudio.com/docs/python/unit-testing)
    1. Anaconda and cheatsheet
        1. [Anaconda user guide](https://docs.anaconda.com/anaconda/user-guide/)
        1. [cheat sheet](https://docs.anaconda.com/_downloads/Anaconda-Starter-Guide-Cheat-Sheet.pdf)
    1. [pytest tutorials](https://docs.pytest.org/en/latest/contents.html)
    1. Sphix and Read the Docs background
        1. [Read the Docs getting started with Sphinx](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#external-resources)
        1. [Sphinx documentation](http://www.sphinx-doc.org/en/master/)
        1. [reST primer](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
        1. [Sphinx/RTD intro for writers](http://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/)
    1. Sample `reST` code
        1. [Quick reST](http://docutils.sourceforge.net/docs/user/rst/quickref.html#example-callout)
        1. [Official reST documentation](http://docutils.sourceforge.net/rst.html)
        1. [Python developer's guide to documenting](https://devguide.python.org/documenting/)
            1. reST code should be 80 columns wide
        1. [matlibplot sampledoc tutorial](https://matplotlib.org/sampledoc/)
        1. [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/latest/)
        1. [Read the Docs table/admonition syntax](https://learning-readthedocs.readthedocs.io/en/latest/Options/table.html)
    1. Using `autodoc`
        1. [Sphinx autodoc feature](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
        1. [Numpy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
        1. [Napolean for numpy docstring support](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon)
    1. Sphinx walkthroughs
        1. [Brandon's PyCon Sphinx tutorial on Read the Docs](https://brandons-sphinx-tutorial.readthedocs.io/en/latest/index.html)
            1. [PDF form](https://media.readthedocs.org/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf)
1. File away:
    1. https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
    1. http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext
1. `xref` style for links on development page
1. In references top paragraph mention how the interspinx is used
1. Per Carol Willing talk
    1. Link a Jupyter notebook
    1. Make spelling test with exception words
1. Get a `<project name>` sort of reference in docs for AAAAAA
1. Autodoc with source files and numpy style
1. Numbering in references page should restart automatically
1. Developer's page with 80 lines vs 72, etc. and how to do in VS code
    1. PEP8 2 spaces for comment
1. DO-178B link for Zen page
1. Split up links in all .rst files
1. Get a toctree to render inside the references page
1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Official `AAAAAA` renaming
1. Link official python developer's guide in `development` pages
1. Link DO-178b
