Viewing local build: http://localhost:8000/_build/html/index.html

# Out-loud proof reading notes

# Immediate website modifications
1. AAAAAA as a glossary term - use find all to replace
1. Items from paper notebook
1. Figure out what uncommenting indices and tables in index.rst will do

# .rst read-through
1. Verify admonitions are all lowercase
1. Verify 3-space indent in rst files, and with nested lists
1. Verify all AAAAAA references are to glossary term

# Environment quickstart
1. Clear .gitignore and re-make it from scratch
1. Install :xref:`Anaconda`, which should include :xref:`VS Code`
1. Do environment walkthrough
1. Make a new AAAAAA conda environment from scratch
   1. Try installing all possible packages via conda, then forge, then pip
      1. Per https://anaconda.org/anaconda/sphinx_rtd_theme style of command
      1. Install those needed for doc8
   1. pytest
   1. restructured text extension
1. Save the AAAAAA environment in .yaml
1. Select which interpreter to use - may make a user setting
1. Clone the AAAAAA repo
1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Install extensions per extension page (should be last after)
1. Make sure .yaml file from before hasn't changed

# Source documentation
1. Link a Jupyter notebook per Carol Willing video
1. Separate ledger.py into a snippets file
1. Document utilities.py
   1. Autodoc with source files and maybe numpy style
      1. Autodoc reference already in references page
   1. [Numpy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
   1. [Napolean for numpy docstring support](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon)
1. Document test_utilities.py
1. Document ledger.py
1. Document test_ledger.py
   1. Add a section to common tasks about testing
   1. May need to update the quickstart guide
1. Incorporate ledger.py snippets
1. Verify all Jupyter notebooks are linked
1. Figure out how to do documentation coverage
1. Make directory trees that describe the structure of the project

# Future development
1. Coverage.py for testing framework
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