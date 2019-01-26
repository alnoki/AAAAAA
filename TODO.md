Viewing local build: http://localhost:8000/_build/html/index.html

## Proofreading
1. Explain how sha1 is at top of each document
   1. Get a link to sha1 and put in documentation.rst and writing.rst

## Administrative
1. Should go through conf.py and figure out what is going on
   1. Can explain in concepts section what defaults are, etc.
      1. Talk about how xref is used, folder it is in, etc.
   1. Update license
   1. Update copyright year
1. Link Willing video times in a CSV table

## Source documentation
1. date.__name__ f string? instead of the string "date"
1. Do autodoc first, then update type annotations, then mypy
   1. Mypy goes into testing developer setup
   1. Real python typing guide
1. Autodoc, then docstrings, then types
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
1. Do original tutorials but with financial data
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
1. Module index on home page :ref:`modindex`
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
1. matplotlib sampledoc tutorial shows how to embed plots
1. numpy codebasics tutorial videos
1. https://web.stanford.edu/~schmit/cme193/
   1. has seaborn and pandas examples
   1. Predictor of survivor on Titanic, powerful statistical modeling tools
1. [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
1. Review references
1. Pandas/matplotlib/numpy tutorial videos on iPad while getting ready
1. Other references from Python training logs on Google Drive