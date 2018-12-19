Viewing local build: http://localhost:8000/_build/html/index.html

# Out-loud proof reading notes

# Website references
1. Sample `reST` code
    1. [matlibplot sampledoc tutorial](https://matplotlib.org/sampledoc/)
1. Other
    1. https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext
1. File references in conf.py

# Immediate website additions
1. Try table format extension from marketplace from .rst search
1. Add reST extension side preview usage to building documentation section
    1. Most of the time can use extension, else proofread live rtfd.io site
1. AAAAAA as a glossary term - use find all to replace
1. Items from paper notebook
1. Figure out what uncommenting indices and tables in index.rst will do
1. Make directory trees that describe the structure of the project

# Environment setup
1. VS Code workspace file to git
1. Clear .gitignore and re-make it from scratch
1. Make a new AAAAAA conda environment from scratch
    1. Try installing all possible packages via conda, then forge, then pip
        1. Per https://anaconda.org/anaconda/sphinx_rtd_theme style of command
    1. pytest
    1. restructured text extension auto-installs
    1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Save the AAAAAA environment in .yaml

# Source documentation
1. Link a Jupyter notebook per Carol Willing video
1. Separate ledger.py into a snippets file
1. Document utilities.py
    1. Autodoc with source files and maybe numpy style
    1. [Sphinx autodoc feature](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
    1. [Numpy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
    1. [Napolean for numpy docstring support](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon)
1. Document test_utilities.py
1. Document ledger.py
1. Document test_ledger.py
1. Incorporate ledger.py snippets
1. Verify all Jupyter notebooks are linked

# Future development
1. Per Carol Willing talk
    1. Make spelling test with exception words
    1. Import video annotation times from iPad notes
1. Package per the YouTube tutorial by the freelancer, link on iPad
1. Tools should have an additional non-open source section:
    1. Robinhood
    1. Alphavantage
    1. Google Sheets
1. Use Corey Schafer password tutorial
1. Robinhood interface to Google sheets
1. RODCA with LaTeX