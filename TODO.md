# 0.3.0 Website restructuring

## New version pushing
1. Then proofread
1. Update the read the docs checkbox for the project
1. Need to update the "active versions" on readthedocs

## Proofreading procedures
1. Should make version update procedures first so they can be pointed to?
   1. Just start writing, you'll get it linked eventually
      1. Could make a stub document
1. When making a new document, reference to the last SHA-1
1. Current procedure for updating a document is inaccurate
   1. Shouldn't reference to last SHA-1 in log
   1. Should reference previous SHA-1 for when the document was changed
      1. Can get this from VS Code
1. Makes more sense to proofread the diff right before a version update
   1. Compare the diff on changed documents versus the previous version
   1. Then, should tag top of file with: .. 0.2.0 etc.
   1. Re-do all proofreading for 0.2.0 release and tag appropriately
   1. Also need to change the description in the concepts-documentation
      1. Shows a SHA-1 at the top of the file
      1. Also do this in the proofreading an original file procedure
1. Need to check the file diff since the last version commit
   1. Consider if the file has been added
      1. Then proofread the whole file
   1. If the file has been modified
      1. Proofread just the diff
   1. If the file has been moved and modified
      1. Need to do the diff against the file before it was moved
         1. Because a moved file shows up as a complete "add"
1. :std:doc: -> :doc:, same with :ref: should be on documentation page
   1. Link to sphinx saying the std isn't needed

## Versioning
1. Top-down to-do task deferral
   1. Punt ## when too many appear
   1. :guilabel:`View: Open View` + :guilabel:`Outline
1. Should be in concepts section
   1. Link to procedures page for versioning
   1. Keep pushing new functionalities in subsequent versions
1. Include link to https://embeddedartistry.com/blog/2017/12/7/start-using-semantic-versioning-to-give-your-version-numbers-meaning
1. https://semver.org/
1. Add a version page/release notes page with
1. Add a versioning procedures page
   1. Can also use this when releasing packages
1. Start next commit at 0.2.0
   1. Listed on release page as a beta
1. Verify can load various release versions on the Sphinx website
   1. After releasing, always increment minor version and list as beta
1. Should go through conf.py and figure out what is going on
   1. Can explain in concepts section what defaults are, etc.
      1. Talk about how xref is used, folder it is in, etc.
   1. Update license
   1. Update copyright year
1. yaml should freeze at last release and then update each release
1. Immediately checkout a branch on the next version number
1. SHA-1 for all docs before a minor rev?
   1. See all docs that have been changed since the last version
   1. Verify individually their proofread status
1. make linkcheck to verify all are correct
1. https://docs.readthedocs.io/en/latest/versions.html
1. https://git-scm.com/book/en/v2/Git-Basics-Tagging
   1. git tag v0.1-lw
   1. Need to tag the release
      1. Put two tags on master and see what happens?
      1. Use v0.2.0 and v0.1.0?
         1. Or just 0.1.0?
1. https://docs.readthedocs.io/en/latest/webhooks.html
   1. On settings for AAAAAA on GitHub, select tags too
1. Don't use lightweight tags because of hyphen

## Zen
1. Spirit of alnoki's apps on Zen page
   1. Functional programming is easiest to read, understand, and test
      1. Link to functional programming reference
   1. Should be open source
   1. Incremental versioning per the link above
      1. Each one should be an MVP (minimum viable prototype)
         1. Link
   1. Hyperlink to anything a novice might not understand
   1. Show how it's done, in case you forget later
   1. Open source and free as much as possible
1. AAAAAA term should say (colloquially referred to as alnoki's apps)
1. Tools should be concepts, code/documentation pages should be specifics
   1. Setup have concepts and specifics section?
   1. Code.rst should be specifics
   1. Move the theory in Code.rst to tools page
1. Cite "_why" and how we get to "live in the computer"
   1. _why's poingnant guide to Ruby
   1. https://poignant.guide/book/chapter-3.html
   1. "That therefore, we, the coders, are foreigners, seeking citizenship in the computer’s locale"
1. https://realpython.com/interview-corey-schafer/
   1. I believe the most important lesson I’ve learned is that you should make content for yourself

## toctree structure
1. quickstart
   1. Mention you have just started the python interpreter with link
1. What next? page
   1. Describes the site
   1. Talk about references
   1. Mention more info on tools in tools page
   1. Say how to get started with Python, etc.
   1. :doc:`python:faq` getting started
   1. :doc:`python:faq/programming` anything specific: keyword args, etc.
   1. TOC for everything page?
1. Fix module index

## Syntax/terminology
1. :std:doc: should just be :doc: per sphinx roles
1. Link to https://en.wikipedia.org/wiki/Command-line_interface
   1. Find all for command line and replace with :xref:
1. Capitalization should mention that proper nouns should be capitalized
   1. Consider the NumPy package
   1. Consider the pandas package
   1. Pandas package
1. Line break in documentation also say ..code-block can go over a line
1. Give all csv-table a title
   1. Use find all
1. Say how information sources (google, wikipedia, etc.) are used
   1. In open-source section
1. Conda procedures should add a link to pip (already in links)
1. Show how */#. spacing works in style guide
   1. Level indentation always 3 spaces
   1. Only one space since the * or the #.
1. Link the tables generator somewhere on tools
1. Use markdown link to say what TODO.md is made from

## Git environment
1. https://stackoverflow.com/questions/24046846
1. https://stackoverflow.com/questions/3459744
1. https://stackoverflow.com/questions/11553374
1. Link to the git commit conventions
1. Explain the Git theme for Vim?
   1. Shows up on current windows machine but not
1. Add configuration to dev setup
   1. Git tower reset local commit as a tip in committing process
1. Describe long message

## src updates
1. use datetime.datetime with zulu time - call the instance variable "when"
1. Restructure other attributes as necessary
1. change kinda to a dict of str to tuple(bool,bool)
   1. bools say is associated with ticker
   1. Second says does it result in add or subtract to buying power
1. overload + to add two transactions and yield effect on the brokerage

# 0.4.0

## matplotlib theme feature implementation
1. matplotlib sample doc
1. Have an example page in iPython
   1. Show link to the actual notebook so people can play around with it
1. Integrate plots
1. Link Jupyter

## Package deployment
1. PEP 328
1. https://stackoverflow.com/questions/448271/what-is-init-py-for
1. https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html
1. Ship conda with the dependencies
   1. Then can install in the quick start
      1. Mention you have just started the python interpreter with link
         1. Link is in the floating point rampage
1. Push to conda and create procedures as you go

## Conf.py autodoc
1. Need a conf.py part of documentation concepts
1. Automodule conf.py and settings.json?

## autodoc test code
1. Document test_ledger.py
   1. Add a section to common tasks about testing
   1. May need to update the quickstart guide
1. Document test_utilities.py
1. Get files to import via AAAAAA.ledger, not src.AAAAAA.ledger for tests
1. tests should be motivated by the examples page

## Doc coverage
1. Figure out how to do this
   1. The packaging video on iPad may help

## Jupyter
1. Verify all Jupyter notebooks are linked
1. Link a Jupyter notebook per Carol Willing video
1. Make an examples page with Jupyter notebook to follow along
1. Tip to open the nb viewer
1. TOC for all Jupyter notebooks?
1. Need a way to include he nbs directory
1. Need a table that says which doc pages link to which nbs
1. Each doc that links to an nb also says which nb it links to
1. Add to nbs concepts page
   1. Say links in them may not be in links page
   1. Core content is distilled into .rst
1. Procedure for linking an nb says the two places that must be update
   1. Link to this procedure in the nbs concepts page
   1. Link to it in the nbs toc page
1. examples page is a jupyter notebook you can reset and run all cells

# 0.5.0

## myPy
1. MyPy type linter
   1. https://www.python.org/dev/peps/pep-0526/
   1. https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
      1. Get the mypy linter going in the conda package
   1. VS Code linter
      1. https://code.visualstudio.com/docs/python/linting
         1. Make a type checking procedures page
         1. Talk about how to disable the pep8 colon warning but leave mypy on
1. :pep:`Type hint theory <483>`
   1. Compare to https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
1. :pep:`Variable annotations <527>`
1. :std:doc:`Typing module <python:library/typing>`

## Robinhood integration
1. Services setup
   1. Robinhood
   1. Will require its own setup section, adding to .yaml, etc
1. Can do later:
   1. AlphaVantage
   1. Google Sheets
   1. EDGAR
1. Use Corey Schafer password tutorial

## Robinhood API references
1. [Unofficial Robinhood API documentation](https://github.com/sanko/Robinhood)
1. GitHub Robinhood modules
   1. [version with 736 stars](https://github.com/Jamonek/Robinhood)
   1. [version with 30 stars](https://github.com/westonplatter/fast_arrow)
   1. [version with 27 stars](https://github.com/mstrum/robinhood-python)

## Transaction updates
1. When transaction init gets an error, should
   1. Raise error
   1. Show a trace to the data that produced it
1. Class method to convert to a dataframe?
   1. Could have a subclass of DataFrame called ledger
      1. By merit of existing, it has already been sanitized
         1. Thus can go straight back into transactions
   1. Would already have sanitized data

# 1.0.0 Package release

## Main functionality
1. Download a Robinhood history to a pandas DataFrame
1. MVP (minimum viable prototype)
1. Package per the YouTube tutorial by the freelancer, link on iPad
1. Make sure the downloadable PDF version is okay

## Deployment
1. Use iPad video
   1. Travis
   1. Coverage for both code and docs
1. Coverage.py for testing framework
1. Per Carol Willing talk
   1. Make spelling test with exception words
   1. Links for topics in csv table, like spellchecking, etc.
   1. Links for package deployment talk
1. __init__.py should have docstrings too per {PEP257 (?)}

## Setup page
1. For the python enthusiast
   1. Conda install AAAAAA
   1. pip install AAAAAA (?)

## Linking
1. Import times from the iPad speech about packaging
   1. Shows code coverage
   1. Link to the topics when you get around to it
      1. Link to every topic from a csv table
1. Make sure all topics from the willing speech are linked too

## Transaction code
1. Do original tutorials but with financial data
1. NaN in GoogleSheets should be different than $0
1. __repr__ should sanitize inputs
1. Need a to_string()

# 1.1.0 BTMF

# Main functionailty
1. Adds PARDAFA and BTMF versus CRSPTMT
1. Cast a portfolio into a Pandas dataframe then plot
1. ABC: Annualized BTMF coefficient
   1. (APR of alnoki) / (APR of CRSPTMT)

# 1.2.0 and on

## General ideas
1. Books
   1. Header for each book is the name
   1. Include ISBN, author
   1. CSV table with a page number and the concept
   1. For The Intelligent investor, can link to another "concepts page"
      1. The 7-step checklist, etc.
1. See all notebook entries since Dec 26
1. Robinhood interface to Google sheets
1. RODCA with LaTeX
1. Do some fun stats first just for fun
   1. Those goons at instutions don't know DSP
   1. The patterns are there
1. Standard and Poors facilitated the 2009 crisis
   1. This is why we use CRSPTMT
      1. Also it is academic

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