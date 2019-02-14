# 0.3.0 Website restructuring

## Mac env
1. Uninstall miniconda
1. clear bash profile
1. Reinstall miniconda
1. Import a6 and tidy up

## Versioning
1. Update project dir tree
   1. Need to say which ones must be updated
      1. The code tree, sphinx tree, etc.
      1. Cross-link with the tree code

## Writing procedures
1. Create a tools entry
   1. Make sure to reciprically cross-reference
   1. Copy links from the tools page and the procedures page
   1. Gather links first
   1. If adding a sphinx extension, add links to the sphinx extensions table

## Zen
1. Spirit of alnoki's apps on Zen page
   1. Show OHIO reference
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
   1. Use "additional body elements epigraph from rest primer
1. Your legacy is your documentation

## toctree structure
1. Remove mod index
1. quickstart
   1. Mention you have just started the python interpreter with link
1. What next? page
   1. Describes the site
   1. Talk about references
   1. Mention more info on tools in tools page
   1. TOC for everything page?
1. Say how to get started with Python, etc. on tools page
   1. :doc:`python:faq` getting started
   1. :doc:`python:faq/programming` anything specific: keyword args, etc.
1. Need to check dir tree during version completion
   1. There are several to check
   1. Have the "dir tree" procedure list a table of the directories that exist
      1. Then can update them when doing version updates
1. Software also has an auto-api section?
   1. May enable module index
1. Tools: what does it do, concepts/specifics: how does alnoki use it
   1. Split up the structure
   1. Make a table somewhere in an index page

## Syntax/terminology
1. Mention :xref:`internet` early on, in "what next"?
   1. Also, :xref:`Google`, :xref:`Wikipedia`, :xref:`YouTube`
   1. :xref:`Open-source software <open-source>`
1. Link to command line and find all
1. source code, code, etc. should link to python tools page
1. :std:doc: should just be :doc: per sphinx roles
      1.Search all for :std: and replace with :
         1. Do this when proofreading to maximize line width
   1. Find all for std doc and std ref
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

## Proofreading all docs
1. Field list in code
   1. should return an obj
   1. How many - parcels of knowledge?
   1. Put a sidebar next to it to compress it left?
      1. Put it in a sidebar?
      1. See rtd documentation
1. Replace :std: -> :
1. See where to remove RTD sphinx theme from

## New version pushing
1. Make 0.3.0 active so you can view it on RTD when doing procedures

# 0.4.0

## plot directive
1. https://matplotlib.org/sampledoc/extensions.html
1. Appears to be included with matplotlib
1. https://matplotlib.org/devel/plot_directive.html
1. Need to include matplotlib and numpy in documenting package
1. Make a factorial plot on the homepage
   1. If you want to run this, you may need to install matplotlib with anaconda
      1. See what happens when you do it from inside python
         1. What pops up?
1. Try out on homepage

## matplotlib theme feature implementation
1. matplotlib sample doc
1. Have an example page in iPython
   1. Show link to the actual notebook so people can play around with it
1. Integrate plots
1. Link Jupyter
1. Remove RTD Sphinx theme from conda
   1. Use conda procedures to see where to remove
   1. Remove mention in the rtd section
   1. Use deprecated feature? Or just mention in rtd section
1. Disclaimers for RTD
   1. Can't render as well on mobile
   1. Need to update the RTD theme section

## Wrapping autobuild
1. Make it run in command line
   1. Only open html files that have been changed, after the build started
   1. Shows how the argument parser, etc. works from command line
   1. Appears that it only opens a browser the first time
1. Run your own python script that looks for touched .html files
   1. Open a new window if the browser doesn't already have it open
   1. How to know whether to open a new window or to reload the old one...
      1. Need to check if the server isn't already "serving" the page?
1. Don't bother integrating with makefiles, it doesn't work on windows too...
   1. https://www.gnu.org/software/make/manual/make.html#Phony-Targets
1. Later, may want to incorporate --watch jupyter notebooks
   1. Just incorporate to the autobuilder
      1. The wrapper should then handle the html monitoring correctly
1. Potentially just have one script to call
   1. Make sure python doesn't go crazy and open eveything
      1. Only open changed pages, not new pages?
      1. Guard: only if the .rst and the .html were changed?
   1. Make clean at the end?
      1. Would this make you have to re-intersphinx everytime?
1. Keep in mind that autobuild sends out some sort of ping or hook
   1. You could somehow monitor this?

## Content card
1. Front
   1. :term:`AAAAAA`: link :xref:`everywhere`
      1. At bottom:
         1. * 'everywhere' : ("The internet", url['Wiki pg] + 'Universe')
   1. Have your email and your website
1. On back, explanation field list
1. Use version 0.3 field list

## Git
1. https://stackoverflow.com/questions/24046846
1. https://stackoverflow.com/questions/3459744
1. https://stackoverflow.com/questions/11553374
1. Link to the git commit conventions
1. Explain the Git theme for Vim?
   1. Shows up on current windows machine but not
1. Add configuration to dev setup
   1. Git tower reset local commit as a tip in committing process
1. Describe long message
1. 325 error occurs if you quit Vim improperly
   1. Makes a .swp file
   1. Remove the .swp file and it should be alright
   1. At .git/COMMIT_MSG.swp
1. Checking out a remote
   1. git checkout -b integration/adc2.07zb/ahrs2.08zb origin/integration/adc2.07zb/ahrs2.08zb
   1. Straight from the man page
   1. git checkout -b dev/0.3.0 --track origin/dev/0.3.0

## src updates
1. Transaction class then explains how file structure is
   1. For importing the module, etc.
1. Then say we need to talk about the dir structure
   1. Then make the dir tree script
1. Explain how Transaction is, of course, all part of a module
   1. Then describe automodule and show below
   1. Then, enable modindex
1. use datetime.datetime with zulu time - call the instance variable "when"
1. Restructure other attributes as necessary
1. change kinda to a dict of str to tuple(bool,bool)
   1. bools say is associated with ticker
   1. Second says does it result in add or subtract to buying power
1. overload + to add two transactions and yield effect on the brokerage

## Package deployment
1. PEP 328
1. yaml should freeze at last release and then update each release
   1. Sort of depends on Travis
1. Update license
1. https://stackoverflow.com/questions/448271/what-is-init-py-for
1. https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html
1. Ship conda with the dependencies
   1. Then can install in the quick start
      1. Mention you have just started the python interpreter with link
         1. Link is in the floating point rampage
1. Push to conda and create procedures as you go

## Settings autodoc
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
1. Use one common file to prototype LaTeX
1. The Anaconda table needs to link to a purpose
   1. For Jupyter, numpy, matplotlib, and pandas
1. https://nbsphinx.readthedocs.io/en/rtd-theme/index.html
   1. Can embed jupyter plots
1. Can use Jupyter to prototype, matplotlib to embed
   1. However, matplotlib can take some time to load

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
1. :doc:`Typing module <python:library/typing>`

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

## Main functionailty
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
1. https://web.stanford.edu/~schmit/cme193/
   1. has seaborn and pandas examples
   1. Predictor of survivor on Titanic, powerful statistical modeling tools
1. [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
1. Other references from Python training logs on Google Drive