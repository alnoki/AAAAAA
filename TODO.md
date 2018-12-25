Viewing local build: http://localhost:8000/_build/html/index.html

# General review

## Out-loud proof reading notes

## Lunch-time reading
1. https://realpython.com/documenting-python-code/
1. https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings

## Immediate modifications
1. Index should show how to install MiniConda
   1. Install miniconda https://conda.io/miniconda.html
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
1. Extensions section should mention bookmarks extension
1. Clear .gitignore and re-make it from scratch
1. All Jupyter extensions used should be mentioned on tools page
1. Tools page says to look at references for more information on extensions
1. Any time a package is added to Conda, add it to tools page under Anaconda
   1. Harvest packages thus far from the QuickStart
   1. Make a .yaml file eventually

## .rst read-through
1. Continue on documentation page
1. Verify admonitions are all lowercase
1. Verify 3-space indent in rst files, and with nested lists
1. Verify all AAAAAA references are to glossary term

# QuickStart guide
Some of these notes were made while trying to do a basic setup on a "virgin"
Mac.

## Building documentation - done on virgin Mac
1. Explain the VS Code workspace settings
1. Introduce the command pallete
1. Make an integrated terminal
   1. For Conda to work inside VS Code on Mac:
      1. "terminal.integrated.shell.osx": "/bin/bash"  // .json setting
   1. For Conda to work inside VS Code on Windows:
      1. Must get when have access to Windows machine
1. Make a miniconda environment
   1. conda create --name a6 python pep8 sphinx sphinx_rtd_theme
      1. Put in a reference to the conda cheatsheet
   1. Source activate vs activate the new env, a6
   1. conda info -e to get path for the interpreter
   1. which python will show python path, then paste into select interpreter
      1. /Users/alnoki/miniconda3/envs/a6/bin/python
1. Install Python extension
   1. Select interpreter for the path just found
      // .json setting
      "python.pythonPath": "/Users/alnoki/miniconda3/envs/a6/bin/python",
1. Open terminal type git --version
   1. Mac may say it needs to be downloaded
   1. Mac Should take care of install via command line tools
   1. Can also download at https://git-scm.com/downloads
1. Git clone the repo
1. conda install -c conda-forge doc8
1. Install reST extension
1. Then follow instructions to build documentation from common tasks

## Running a pytest - still need to attempt
1. conda install pytest pep8 // from inside a6 environment
1. Install doc8 and other rst extension dependencies per
   1. https://anaconda.org/anaconda/sphinx_rtd_theme style of command
1. Jupyter extensions and settings
   1. Conda nbextensions install
   1. Is there an equivalent to a .yaml that can keep nbextensions/preferences?
1. Run a pytest with the pip install -e or conda install -e equivalent
   1. Link to pytest test discovery explanation
1. Install all the extensions and maybe .yaml?
   1. .yaml could become obsolete

# Next tasks

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