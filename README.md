# AAAAAA
Alnoki Algorithmic Analysis Asset Allocation Advisor

*Brought to you by alnoki*

[AAAAAA documentation](https://alnoki.rtfd.io) is hosted at
[Read the Docs](https://rtfd.io), but below are some additional notes
that are kept locally during developement

## Philosophy
1. Testing and documenting up front prevents runtime debug headaches
1. Have DRY (don't repeat yourself) code: decompose as much as possible
1. Documentation should enable another to re-write source and test code
1. Have STUPID simple tests. Don't recursively 'test the test code'
1. Documenting & testing forces consideration from various perspectives
1. Consider DO-178B as a model for software design assurance
1. PEP8 provides a repeatable and official means for formatting
1. Legacy conventions shouldn't prevent a new worthwhile philosophy
1. Play around and "whiteboard" code during initial stages

## Project structure
1. `src`: Source code
1. `test`: [pytest](https://docs.pytest.org) modules for testing source
code
1. `docs`: Documentation created via recommended [Read the Docs](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#quick-start)
procedure
1. `nbs`: [Jupyter Notebook](http://jupyter.org/) documentation of
`src` and `dev` (nbs = 'notebooks')
    1. `dev` includes walkthroughs done during experimental code
    creation
    1. `src` includes some documentation pre-[Read the Docs](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#quick-start)
procedure

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

## Select references
1. [Changing bash prompt](https://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html)
1. General Python
    1. [Python.org documentation](https://docs.python.org/) and
    [tutorial](https://docs.python.org/3/tutorial/index.html)
    1. [Corey Schafer YouTube playlist: Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
    1. [alnoki Jupyter notebooks and sample code from assorted tutorials](https://github.com/alnoki?tab=repositories)
    1. [Anaconda user guide](https://docs.anaconda.com/anaconda/user-guide/)
    and [cheat sheet](https://docs.anaconda.com/_downloads/Anaconda-Starter-Guide-Cheat-Sheet.pdf)
1. Testing with `pytest`
    1. [codebasics YouTube playlist: Pytest Tutorial (Python Automated Testing)](https://www.youtube.com/playlist?list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu)
    1. [pytest.org homepage](https://docs.pytest.org) and
    [tutorials](https://docs.pytest.org/en/latest/contents.html)
    1. [VS Code Python tutorial](https://code.visualstudio.com/docs/languages/python)
    and [unit testing documentation](https://code.visualstudio.com/docs/python/unit-testing)
1. Documentation
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
        1. [Carol Willing Practical Sphinx talk from PyCon with examples](https://www.youtube.com/watch?v=0ROZRNZkPS8)
            * `python -m http.server` -> http://localhost:8000/_build/html/index.html
            * `make linkcheck`
            * `make clean` then `make build`
        1. [Mahdi Yusuf Sphinx quickstart screencast](https://www.youtube.com/watch?v=oJsUvBQyHBs)


## TODO
1. Reference audit
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. Make a comprehensive references file
        1. PEP8 has a cross-reference directive
        [ref](http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-pep)
        1. Every other file should point to it, no links in other files
    1. Check every link to add to a references file
    1. Intersphinx with as much as possible
1. Migrate readme to Sphinx
1. How to line break in a bulleted list?
1. Per Carol Willing talk
    1. Link a Jupyter notebook
    1. Make spelling test with exception words
1. Get a `<project name>` sort of reference in docs for AAAAAA
1. Autodoc with source files and numpy style


