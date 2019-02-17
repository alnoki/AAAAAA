# 0.4.0

## Proofreading followup
1. Follow td3
1. Does pushing a tag push the merged master?
   1. If so, verify in version procedures and in git procedures
1. AAAAAA should link to double triple alpha
   1. Also use a link to :xref:`software`
1. Try putting py:function:explanation in text somewhere
   1. User guide warning to show what you won't be able to see
      1. This is a sample, but the real ones might not show ups
1. Should have an index.rst for dev-guide
   1. Add to doc structure tree
   1. Then, on the what-next page, re-do the links to these places
1. Should have index.rst for every .rst dir
   1. In a spirit of apps
      1. Because it tells you where to go next
1. If not on an anchor (.html#heading-title), livereload doesn't jump
around
1. Add a csv table to the concepts-code page once you have more references
   1. Packges, __init__, setup.py, etc.
1. Add in links to the zen page, they are lacking
   1. Do this after a few versions
1. Documentation page section about AAAAAA live within, not live(S) within
1. When proofreading, in .rst, look at anything that isn't rendered white
   1. You already looked at the white part when reading the site
   1. When you see, :term:`aaaaaa`, say *alnoki's apps*
      1. Link to the documentation page
   1. Clear cookies and make every link turn purple
   1. Should still read in the major section you are on
1. Need a references link to print() (from homepage)
1. Link for wiki pg to download
   1. On the VS Code tools page
   1. Git links general: download Git
   1. Put on the quickstart
   1. Put in the link for to :xref:`download` the AAAAAA repository
   1. Put in link page for miniconda quick to download
   1. Also on the concepts index page (downloading them all)
   1. Also on anaconda tools page
1. wiki pg for "file"
   1. In changes to a document writing procedure
   1. rst file on tools-restructured-text
   1. Git procedure for commiting
   1. And in writing about a project tree
1. wiki pg for "save a file"
   1. Find all for places where it should be linked
1. Upload
   1. Link in push, a couple places find all for "upload" on git page
   1. Will also use with PyPI
   1. Also in Git table for upload to github
1. The conda package is lowercase in-line
   1. Need to update on the pages before the links page
   1. Git is uppercase in-line
1. https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/lists_tables.html#option-lists
   1. For the sphinx-autobuild
   1. And for dev.py
1. Search links for the word plot and link to matplotlib?
1. Find all for tutorial/interpreter (some instances may not have python:)
   1. Same for copy-paste
   1. Finda all for open-source - should read "open-source" need hyphen
      1. Have a documentation checklist for common ones
1. The Internet should be capitalized at the end of a sentence, the Internet
1. Tag the version comment before you go through the document
1. Reading out loud in a british accent is way more fun
1. doctest block like the user guide on the homepage and quickstart
1. Directive should indent to the same leve as the text after the * or the #.
   1. This is not easy after a *
1. Add git-clone to the git links page
1. Use conda tidy up when doing tests to make sure everything still works
1. Get pytest from home dir to actually run....
1. All toctrees should have
   1. .. If you add to the toctree, explain what it is above
1. Matplotlib plotting need to change packages setup phase
   1. Also go off conda install procedure
1. Link at the top of the user guide, per the writing tools procedure
   1. :term:`AAAAAA` conceptual explanation
1. Verify tools-sphinx links to :ref:`concepts-documentation-structure`
1. dev-guide needs and index.rst and should be on documentation structure
1. Do a name, function table (like in documentation.rst) on code.rst later
1. Search for :ref:`Labels <ref-role>` - should have sphinx:ref-role
1. See what sample-doc looks like
   1. Beware of how the literalinclude directive will be affected
1. After making a packaging section, link to it from the top of the code.rst pg
1. Re-write/re-link zen in a later version
1. Put an explanation on the procedures page
1. What about pulling a branch from the aaaaaa repo?
1. The index for procedures assumes you've already read everything else
   1. It's going to be direct and basically notes to yourself
1. Proofread with a silly voice
1. RegEx link from Lance
1. Using cite external links for the wiki page will create a new link
   1. But, it is not error checked
   1. xref does error checking.....
1. Use the :guilabel:`raw` on GitHub
   1. find all for view on github
1. Find all for .rst - use a or an before it?
1. Find all for document and replace with file?
1. Use same ISO standard that Robinhood uses for dates in version list
   1. Mention in src updates, for planning the when instance attribute
1. When diffing in stage changes, confirm new tag at top of .rst file

## toctree stubbing
1. Re-do labels for user-guide and dev-guide
1. First page (index) in user/dev guide should be "how to use this guide"
1. PyPI is a tool in "distributing" section
1. Need stubs for the testing index and developer guide index
   1. Re write links to these places in there parent indices and in what-next
1. Put in a stub for the examples page
   1. Say can do either in the interpreter or in Jupyter notebook
   1. Then put in a link from jupyter page
   1. Python tools section should link here
1. Procedures page should say what different procedures are for
   1. A table  of procedure pages, and a link to a conceptual explanation(s)
1. All toctrees should have similar comment below them
   1. Add to writing procedure
   1. Use find all to find all toctrees
1. Procedures are not as tutorialesque, more of a checklist
1. Explain in version link how some additions are pertinent to developers too

## External references extension
1. Should be a subsection of managing external links procedure
   1. "Common links"
1. https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension
1. Restructured role revolution "r3"
1. Add to the exts dir on the doc dir tree
1. Look for that which has 'url[' in it
   1. Only do super common ones
      1. Don't do Stack OF, because its redirect links are huge
1. Wikipedia page for sure
   1. Use the extension that creates a role :wikipg:`money`
      1. Verify you can give it a custom title first, before you migrate
   1. Migrate all first, then use diff to check out link text rendering

## Packaging
1. https://anaconda.org/conda-forge/doc8
   1. This one is showing on anaconda cloud....
1. Tools section on PyPI
1. Currently, the link to pip already exists
1. Do this first!
1. Section on writing tests and packaging in dev-guide
1. Try out with the 0.3.0 codebase
1. First get onto PyPi
    1. https://packaging.python.org/tutorials/packaging-projects/
1. Then, can try adding to conda-forge
    1. https://conda-forge.org/docs/
    1. There is a sample file that just points to PyPi
    1. https://github.com/conda-forge/staged-recipes/blob/master/recipes/example/meta.yaml
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
1. https://packaging.python.org/tutorials/packaging-projects/
   1. Go through the tutorial and upload to test pypi
1. https://choosealicense.com/
   1. Probably MIT
      1. Need to have a versioning section that says to update year
1. https://packaging.python.org/guides/distributing-packages-using-setuptools/
   1. More info about setup tools
1. The examples page (if in Jupyter) should link to interactive analysis
   1. In the Anaconda a6 table
   1. Also, the Code testing link should go to the test index
   1. And, the numerical analysis parts should get links

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
   1. Do sqrt(x!) ?

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
1. Try out log base 16 of factorial of x

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
1. See https://docs.python.org/3/tutorial/modules.html
1. Have the wrapper put the output to the console
   1. See autobuild for how this is done, because it wraps sphinx
   1. https://docs.python.org/3/library/argparse.html#module-argparse
1. Watch the server that autobuild makes
   1. https://pythonhosted.org/watchdog/index.html
   1. It should send out some sort of ping that says to reload
   1. Only open a new browser window if the html file in question isn't served
      1. And if a reload ping came
1. When the html file changes, the autobuild console should say so
   1. Have the wrapper look for this and then open up a new browser?

## adp.py
1. autodoc it on the procedures index page
1. Cite the checklist manifesto
1. arg parse from early on in python tutorial
1. Talk about utils.py in AAAAAA root?
    1. code for writing dir tree
        1. Take command line args
1. Wrapper for sphinx-autobuild
    1. Says which folders to watch
    1. Simple command line prompt:
        1. python utils -doc
1. Explain how the terminal opens at top aaaaaa dir, so use argparse
   1. For wrapping autobuild, etc.
1. Use the command line options style of table
   1. See the RTD theme
   1. Add this to the sphinx autobuild options once you know how to do it
1. Have one that automatically opens a :ref: or a :doc:
   1. python adp ref-tools-restructured-text

## Content card
1. AnaKAHNndaKAHN 2019
1. Front
   1. :term:`AAAAAA`: link :xref:`everywhere`
      1. At bottom:
         1. * 'everywhere' : ("The internet", url['Wiki pg] + 'Universe')
   1. Have your email and your website
1. On back, explanation field list
   1. Just make the window smaller in order to view it
1. Use version 0.3 field list

## Git
1. Explain .gitignore and link to project tree
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
1. xref in transaction source code
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
1. As you segway into explaining file structure
   1. https://docs.python.org/3/tutorial/modules.html
   1. Should help you get ready to package on conda
1. Add to python tools description as you go
1. Run https://docs.python.org/3/tutorial/modules.html#the-dir-function
1. https://docs.python.org/3/tutorial/modules.html#packages
1. Then, use https://docs.python.org/3/library/argparse.html#module-argparse
   1. Draw a dir tree?
1. Uncomment module index on homepage, verify it works
1. Re-write the jupyter section after the jupyter examples page is live
   1. Will need aaaaaa usage on the examples page
   1. The numerical analysis packages should link to tools-numpy, etc.
1. Tables can line break in the title without quotes
   1. See VS code extensions

## Settings autodoc
1. Need a conf.py part of documentation concepts
   1. Then can hyperlink the conf.py part in the Sphinx references table
1. Automodule conf.py and settings.json?
   1. If you do this, then be sure to review the links in the vs code section
   1. Also then review the sphinx settings section

## Test code
1. Cite DO-178B
1. Have a test index in the developer's guide
   1. The pytest entry on the links page should link here
      1. Framework for :ref:`writing test code <test-index>`
1. Document test_ledger.py
   1. Add a section to common tasks about testing
   1. May need to update the quickstart guide
1. Document test_utilities.py
1. Get files to import via AAAAAA.ledger, not src.AAAAAA.ledger for tests
1. tests should be motivated by the examples page

## Doc coverage
1. Figure out how to do this
   1. The packaging video on iPad may help
1. Doc coverage is a sphinx extension

## Jupyter
1. Update the documentation.rst jupyter section
1. All jupyter notebooks should be able to be viewed
   1. If you add one, must be able to access it from the AAAAAA nb viewer link
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

## Conda-forge packaging

## Doc
1. TOC for everything page?
1. Software also has an auto-api section?
   1. May enable module index

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