Viewing local build: http://localhost:8000/_build/html/index.html

# Out-loud proof reading notes

# General notes
1. Intersphinx to math page about LaTeX
1. File references in conf.py
1. Use Corey Schafer password tutorial for Robinhood, Google API, etc.
1. Link to conf.py intersphinx in footnote to reST on tools page
1. Go through top to bottom - either do, or re-order for later
1. AAAAAA as a glossary term
1. Get intersphinx working with additional sites
    1. Sample `reST` code
        1. [matlibplot sampledoc tutorial](https://matplotlib.org/sampledoc/)
    1. Using `autodoc`
        1. [Sphinx autodoc feature](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
        1. [Numpy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
        1. [Napolean for numpy docstring support](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon)
1. File away:
    1. https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext
1. Per Carol Willing talk
    1. Link a Jupyter notebook
    1. Make spelling test with exception words
    1. Import video annotation times from iPad notes
        1. Get link from below too, the packaging/deploying/etc. video
1. Autodoc with source files and numpy style
1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Install DOC8 linter for reST extension
1. Items from paper notebook
1. Use the live render in the reST plugin
1. Figure out what uncommenting indices and tables in index.rst will do
1. Tools should have additional non-open source section:
    1. Robinhood
    1. alphavantage
    1. Google sheets
1. Plan out actual source code dev design when website is all ready
    1. Robinhood interface to Google sheets
    1. RODCA with LaTeX
1. AAAAAA glossary term for anywhere find all finds AAAAAA
1. Make trees that describe the structure of various project directories
    1. Update code.rst structure section

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