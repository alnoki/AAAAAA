## Links audit: 1 at the start, 1 at the end of your session
1. Py like you rest, rest like you Py

## Configurations page
1. Reciprical cross links
      1. Then can reference quickstart from rtd setup
      1. Even need to do on the trees
1. csv tables for all tools on the configs page
   1. Then click through them to the other places and make sure they come back
1. Use :annotation: ~blank~ will take out the entire data field showing up
   1. Then can use docstring from .py file
   1. Use to update all autodata, especiallyin conf.py
.. autodata:: ACQdoctor.crc.crc_tbl_8408
   :annotation:

## Extensions and rtd
1. :term:`AAAAAA` was started with the sphinx-quickstart
1. After you do quickstart, you have a project, but you want to upload it, etc.
   1. Thus you need to think about extensions
1. Verify builds pass on rtd before pushing tag
1. Just made a requirements.txt file
   1. On my account, had to update advanced settings
1. You need conf.py to say the bibtex, but rtd doesn
   1. You conda, it pip
1. Will need to uncomment in conf.py to load using conda
1. Configs page should be a one-time thing
1. Talk about the process of monitoring builds, etc.

## Dev env setup
1. Show how to install a vs code extension
1. Zen should be the last env setup page
   1. Make sure no references elsewhere

## Writing section
1. Has VS Code section
   1. Link to VS code in the tools page, and recipricollay
   1. Show how to get tokens, language rulers, select colors, show web colors
      1. Already have links
1. :guilabel:`Preferences: Open Raw Default Settings`
1. VS Code its own page
   1. Show how to view the raw settings file

## Versioning
1. Update configurations if any have changed

## quicklinks
1. :wiki-pg:`run <Execution_(computing)>`
1. :wiki-pg:`scroll <Scrolling>`
1. :wiki-pg:`Click <Point_and_click>`
1. :wiki-pg:`Typing`
1. :wiki-pg:`HTML`
1. :wiki-pg:`Install <Installation_(computer_programs)>`
1. :wiki-pg:`Download`
1. :wiki-pg:`Filename extension <Filename_extension>`
1. :wiki-pg:`File <Computer_file>`
1. :wiki-pg:`Open-source_software`
1. :wiki-pg:`Character <Character_(computing)>`
1. :wiki-pg:`String <String_(computer_science)>`
1. :wiki-pg:`Line <Line_(text_file)>`
1. :wiki-pg:`Line break <Newline>`
1. :wiki-pg:`Whitespace <Whitespace_character>`
1. :wiki-pg:`Indentation <Indentation_(typesetting)>`
1. :wiki-pg:`User <User_(computing)>`
1. :wiki-pg:`Developer <Programmer>`
1. :wiki-pg:`Development <Software_development>`
1. :wiki-pg:`Algorithm`
1. :wiki-pg:`Rendering_(computer_graphics)`
1. :wiki-pg:`Host <Host_(network)>`
1. :wiki-pg:`Documentation <Software_documentation>`
1. :wiki-pg:`Delimiter`

# 0.5.0

## Dev Order
1. Write up testing first before packaging
   1. Do what you know first
1. Update ISO8061 then do testing

## Examples page
1. Say can do either in the interpreter or in Jupyter notebook
1. Then put in a link from jupyter page
1. Python tools section should link here

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
1. Add a Jupyter configurations page
   1. Talk about the notebook extensions, etc

## Doc coverage
1. Figure out how to do this
   1. The packaging video on iPad may help
1. Doc coverage is a sphinx extension

## pytest
1. Get pytest from home dir to actually run....
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
1. On the code structure page, update the dir tree
   1. Use a table for each of the components like on the other dir trees
      1. name, function

## Settings concept
1. Vim and Git setup?
1. VS Code
   1. Colors via textmate
   1. https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector
      1. :guilabel:`Developer: Inspect TM Scopes` then add to settings.json
   1. https://stackoverflow.com/questions/46689334
   1. https://github.com/Microsoft/vscode/pull/29393
1. :wiki-pg:`Web_colors` already in links
1. link to "linter"
1. Need a conf.py part of documentation concepts
   1. Then can hyperlink the conf.py part in the Sphinx references table
1. https://stackoverflow.com/questions/46689334
1. Automodule conf.py and settings.json
   1. If you do this, then be sure to review the links in the vs code section
   1. Also then review the sphinx settings section

## src updates
1. Give an example of initializing a transaction class
1. ISO 8061 (or whatever robinhood uses) for dates
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
1. Add a csv table to the concepts-code page once you have more references
   1. Packges, __init__, setup.py, etc.
   1. As you go through and explain

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

## adp.py
1. https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/lists_tables.html#option-lists
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

## plot directive
1. On home page
1. Feeling super fancy?
   1. Exit interpreter
   1. Conda install matplotlib
   1. Then do the matplotlib code
1. Use the in-line version that shows the sample and the plot
1. Matplotlib plotting need to change packages setup phase
   1. Also go off conda install procedure
   1. Same for numpy and pandas? Since will embed them?
1. Search links for the word plot and link to matplotlib tools section
1. https://matplotlib.org/sampledoc/extensions.html
1. Appears to be included with matplotlib
1. https://matplotlib.org/devel/plot_directive.html
1. Need to include matplotlib and numpy in documenting package
1. Make a factorial plot on the homepage
   1. If you want to run this, you may need to install matplotlib with anaconda
      1. See what happens when you do it from inside python
         1. What pops up?
1. Try out on homepage
1. Search links for the word plot and link to matplotlib?
1. Create a section in tools on Matplotlib
1. matplotlib sample doc
1. Have an example page in iPython
   1. Show link to the actual notebook so people can play around with it
1. Integrate plots
1. Link Jupyter
1. Try out log base 16 of factorial of x
1. On links page, the jupyter general link says plotting, should link
   1. Link to matplotlib


## Packaging
1. See the project management -> distribution section of links
   1. Update the comment for requirements files?
1. After making a packaging section, link to it from the top of the code.rst pg
1. Reciprically link with the project directory structure
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
1. Make sure to do Conda-forge packaging too

## Doc
1. TOC for everything page?
1. Software also has an auto-api section?
   1. May enable module index
1. When conda finally gets sphinx rtd theme 0.4.3 (or whatever it is)
   1. Are the settings different?
      1. How far down can the stick TOC go?

## myPy
1. ttps://code.visualstudio.com/docs/python/settings-reference#_mypy
1. MyPy type linter
   1. https://www.python.org/dev/peps/pep-0526/
   1. https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
      1. Get the mypy linter going in the conda package
   1. VS Code linter
      1. https://code.visualstudio.com/docs/python/linting
         1. Make a type checking procedures page
         1. Talk about how to disable the pep8 colon warning but leave mypy on
1. Figure out how to show all lines in rst files that are too long
1. :pep:`Type hint theory <483>`
   1. Compare to https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
1. :pep:`Variable annotations <527>`
1. :doc:`Typing module <python:library/typing>`

## Robinhood integration

## Downloading transaction history from Robinhood
1. If transaction type isn't recognized, just skip over it
   1. Print out that a .json object was obtained that was unknown
1. After downloading, the pandas portfolio parser (PPP) does checksum
   1. Does net portfolio amount equal buying power?
1. Need a logger / other way to harvest syntax from others
   1. What does a stock split or withdrawal look like?
      1. You can easily simulate withdrawal, then can put right back in

## Transaction updates
1. When transaction init gets an error, should
   1. Raise error
   1. Show a trace to the data that produced it
1. Class method to convert to a dataframe?
   1. Could have a subclass of DataFrame called ledger
      1. By merit of existing, it has already been sanitized
         1. Thus can go straight back into transactions
   1. Would already have sanitized data

## gitignore
1. Explain what different things can cause gitignore to have contents
   1. Pytest/compiled python, etc
1. Make a development task to clean it out?
1. Do a commit that is just cleaning out .gitignore

# 0.6.0

## Robinhood time
1. https://stackabuse.com/converting-strings-to-datetime-in-python/
   1. Do strptime
   1. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
   1. Have a robinhood.py file
      1. module variable robinhood.date_format
         1. '%b %d %Y %I:%M%p' or similar
1. https://docs.python.org/3/library/datetime.html#datetime.datetime
   1. Looks like robinhood is already in correct format
   1. https://github.com/sanko/Robinhood/blob/master/Order.md#place-an-order
1. Assume all times are zulu to avoid confusion
1. Use a Naive timezone, assume zulu

## Robinhood integration
1. Services setup
   1. Robinhood
   1. Will require its own setup section, adding to .yaml, etc
1. Can do later:
   1. AlphaVantage
   1. Google Sheets
   1. EDGAR
1. Use Corey Schafer password tutorial
1. [Unofficial Robinhood API documentation](https://github.com/sanko/Robinhood)
1. GitHub Robinhood modules
   1. [version with 736 stars](https://github.com/Jamonek/Robinhood)
   1. [version with 30 stars](https://github.com/westonplatter/fast_arrow)
   1. [version with 27 stars](https://github.com/mstrum/robinhood-python)
1. RegEx
   1. https://regexr.com/



## Zen page updates
1. Go through and re-write/re-link once there are more places to link to

## Pandas ledger class
1. Make a ledger a sub class of a dataframe
   1. Use super like in https://realpython.com/python-super/
      1. Also has inheritance tutorials, OOP:
         1. https://realpython.com/python3-object-oriented-programming/

## Proofreading
1. Delete base_url from conf.py or defer until later

# 0.7.0

## robinhood user data
1. Have a .txt file that denotes portfolios
1. Have a way you can use google drive to store data

## alnoki's analysis archives
1. A new section with a ton of plots

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
1. See all notebook entries since Dec 26
   1. Leisurely review paper notebook notes for more ideas
1. Robinhood interface to Google sheets?
   1. Make an AAAAAA GSheet and update the associated GDrive document ledger
1. RODCA with LaTeX?
1. Do some fun stats first just for fun
   1. Those goons at instutions don't know DSP
   1. The patterns are there

## Investing philosophy page?
1. For The Intelligent investor, can link to another "concepts page"
   1. The 7-step checklist, etc.
1. See other investing references from urls on Google Drive
1. Warren Buffet BRK website
   1. Fair price wonderful company vs wonderful price fair company
1. Easy to be small guy vs hunting elephants
1. Growth in book value per year as a metric?
1. Standard and Poors facilitated the 2009 crisis
   1. This is why we use CRSPTMT
      1. Also it is academic

## Numerical analysis
1. https://web.stanford.edu/~schmit/cme193/
   1. has seaborn and pandas examples
   1. Predictor of survivor on Titanic, powerful statistical modeling tools
1. [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
1. Other references from Python training logs on Google Drive