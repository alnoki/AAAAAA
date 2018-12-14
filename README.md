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
1. Get intersphinx working with additional sites
    1. Sample `reST` code
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
1. Migrate readme to Sphinx
1. File away:
    1. https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
    1. http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext
1. Per Carol Willing talk
    1. Link a Jupyter notebook
    1. Make spelling test with exception words
    1. Import video annotation times from iPad notes
        1. Get link from below too, the packaging/deploying/etc. video
1. Get a `<project name>` sort of reference in docs for AAAAAA
1. Autodoc with source files and numpy style
1. Numbering in references page should restart automatically
1. Developer's page with 80 lines vs 72, etc. and how to do in VS code
    1. PEP8 2 spaces for comment
1. DO-178B link for Zen page
1. Markdown table generator for Jupyter
1. Split up links in all .rst files
1. Get a toctree to render inside the references page
1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Link official python developer's guide in `development` pages
1. Link DO-178b
1. Linkcheck intersphinx
1. Install DOC8 linter for reST extension
1. LaTeX external reference
1. Make sure all links are in as necessary
1. Items from paper notebook
1. Read through all documentation out loud at then end of above updates