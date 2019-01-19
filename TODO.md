Viewing local build: http://localhost:8000/_build/html/index.html

# General review

# Developer's setup

## Tools
1. Update Sphinx procedures
   1. Make linkcheck and make spelling should be their own procedure?
   1. Less admonitions?


## Testing - still need to attempt
1. conda install pytest
1. Jupyter extensions and settings
   1. Conda nbextensions install
   1. Is there an equivalent to a .yaml that can keep nbextensions/preferences?
1. Run a pytest with the pip install -e or conda install -e equivalent
   1. Link to pytest test discovery explanation
1. Install all the extensions and maybe .yaml?
   1. .yaml could become obsolete
1. Testing viewer extension in the pytest section
1. pip install -e from inside src folder
   1. Will involve moving setup.py
      1. May need to update in folder tree structure description

## Jupyter
1. Will need to conda install
1. Have a link to the tools page for notebook extensions
1. .yaml equivalent of Jupyter notebooks?
1. All Jupyter extensions used should be mentioned on tools page

## Setup after development configuration is complete
1. All VS Code extensions from the tools page should be added in dev setup
1. Conda procedures
   1. Conda update
   1. Make a .yaml
   1. Install a .yaml
1. After completing setup guide
   1. Should go through conf.py and figure out what is going on
   1. Can explain in concepts section what defaults are, etc.
      1. Talk about how xref is used, folder it is in, etc.
   1. Update license
   1. Update copyright year
1. Proofreading before src changes
1. Any time a package is added to Conda, add it to tools page under Anaconda
   1. Harvest packages thus far from the QuickStart
   1. Make a .yaml file eventually

## Proofreading procedures
1. Should be done with browser side-by-side with VS Code
1. Verify admonitions are all lowercase
1. Verify 3-space indent in rst files, and with nested lists
1. Verify all AAAAAA references are to glossary term
1. Go through website front to end read aloud
   1. Make sure reST looks fine
   1. Then can have a "not proofread" section
   1. Can have comment on each page: last proofread YYYYMMDD
         1. Then can compare this date with commit change dates
         1. Can be a procedure for editing
1. Live build next to .rst
   1. Read a section out loud first, use the anchor to go to it
   1. Click links as you go through
   1. Read a section at a time on text, then check rest for style and links

# Next tasks

## Source documentation
1. https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
1. https://realpython.com/documenting-python-code/
1. Use sphinx rtd theme for test_module.py
1. Link a Jupyter notebook per Carol Willing video
1. Separate ledger.py into a snippets file
1. Document utilities.py
   1. Autodoc with source files and maybe numpy style
      1. Reference the autodoc extension in the tools page
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
1. MyPy type linter
   1. https://www.python.org/dev/peps/pep-0526/
   1. https://realpython.com/python-type-checking/
1. Link to the Python article about Decimal vs floating point types
1. Uncomment mod index on main page
1. https://realpython.com/python-type-checking/#annotations
   1. Annotate everything
   1. Get mypy going

## Transaction code
1. NaN in GoogleSheets should be different than $0
1. __repr__ should sanitize inputs
1. Need a to_string()

## Robinhood API references
1. [Unofficial Robinhood API documentation](https://github.com/sanko/Robinhood)
1. GitHub Robinhood modules
   1. [version with 736 stars](https://github.com/Jamonek/Robinhood)
   1. [version with 30 stars](https://github.com/westonplatter/fast_arrow)
   1. [version with 27 stars](https://github.com/mstrum/robinhood-python)

# Future development

## General ideas
1. Books
   1. Header for each book is the name
   1. Include ISBN, author
   1. CSV table with a page number and the concept
   1. For The Intelligent investor, can link to another "concepts page"
      1. The 7-step checklist, etc.
1. See all notebook entries since Dec 26
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
1. Do some fun stats first just for fun
   1. Those goons at instutions don't know DSP
   1. The patterns are there
1. Cast a portfolio into a Pandas dataframe then plot
1. Make an AAAAAA GSheet and update the associated GDrive document ledger
1. Leisurely review paper notebook notes for more ideas
1. See other investing references from urls on Google Drive

## Numerical analysis
1. numpy codebasics tutorial videos
1. https://web.stanford.edu/~schmit/cme193/
   1. has seaborn and pandas examples
   1. Predictor of survivor on Titanic, powerful statistical modeling tools
1. [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
1. Review references
1. Pandas/matplotlib/numpy tutorial videos on iPad while getting ready
1. Other references from Python training logs on Google Drive