Viewing local build: http://localhost:8000/_build/html/index.html

# General review

## Out-loud proof reading notes

## Lunch-time reading
1. https://realpython.com/documenting-python-code/
1. https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings

## Immediate modifications
1. Py like you reST, reST like you Py
   1. Footnote to Tom C Bryan
   1. Be able to get blank computer to environment stage via QuickStart
1. Intersphinx to footnotes on documentation page
1. Index under first Python tutorial step
   1. If the above step didn't work, then it appears your machine didn't come
      preloaded with Python. At this point you have two options
         1. Quit
         1. Install anaconda
            1. And follow the quickstart guide (when it becomes available)

## .rst read-through
1. Continue on documentation page
1. Verify admonitions are all lowercase
1. Verify 3-space indent in rst files, and with nested lists
1. Verify all AAAAAA references are to glossary term

# Next tasks

## QuickStart guide
1. Jupyter extensions and settings
1. VS Code bookmarks extension
1. 2 sections
   1. Basic setup has minimal needed for a transaction to be declared
      1. Just get VS Code going and clone/install .yaml
      1. Explain activating the environment on Windows vs Mac
      1. Explain selecting interpreter as user setting, etc.
      1. `Conda install -e` (if it exists) last, else `pip install -e`
      1. Say that can do developer setup next too
   1. For Developers has everything that alnoki uses, and says so
      1. Should be the basic guide, plus extensions added
      1. Explain the VS Code workspace settings
      1. Links to more tasks pages as they become available
         1. They should link back too
      1. Talk about how to test/document code as task guides become available
1. .yaml creation in common tasks links to setup
1. Clear .gitignore and re-make it from scratch
1. Install :xref:`Anaconda`, which should include :xref:`VS Code`
1. Install :xref:`VS Code` extensions (on the advanced setup page)
1. Do environment walkthrough
1. Make a new AAAAAA conda environment from scratch
   1. Try installing all possible packages via conda, then forge, then pip
      1. Per https://anaconda.org/anaconda/sphinx_rtd_theme style of command
      1. Install those needed for doc8
      1. If `conda list` shows something as a pip package, try installing in
         Conda and then `pip uninstall`
   1. pytest
   1. restructured text extension
1. Save the AAAAAA environment in .yaml
1. Select which interpreter to use - may make a user setting
1. Clone the AAAAAA repo
1. `pip install -e` for using package with `pytest` to `dev tasks`
   1. Should always come after downloading a .yaml or making Conda environment
   1. Is there a Conda install -e?
1. Install extensions per extension page (should be last after)
1. Make sure .yaml file from before hasn't changed
1. Index says - having trouble running Python? Try the QuickStart guide
1. All Jupyter extensions used should be mentioned on tools page
   1. Is there an equivalen to a .yaml that can keep nbextensions/preferences?
1. Tools page says to look at references for more information on extensions
1. Any time a package is added to Conda, add it to tools page under Anaconda

## Source documentation
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
1. Link to the Python article about Decimal vs floating point types
1. Uncomment mod index on main page

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
1. [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
1. Review references
1. Pandas/matplotlib/numpy tutorial videos on iPad while getting ready
1. Other references from Python training logs on Google Drive