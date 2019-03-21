## Links audit: 1 at the start, 1 at the end of your session
* Py like you rest, rest like you Py

# 0.5.0

## Proofreading notes
* src updates use the dateutil parser from version-stats.ipynb
* PPP should be the page count of PDF, not what last page says
   * Page 116 said 112 at the bottom
   * Update for the released ones
* rev-list count HEAD for current commit
* Check doc8 output when proofreading
* https://www.idownloadblog.com/2015/01/14/how-to-enable-key-repeats-on-your-mac/
* Proofreading changed documents
   * Not need identify a tag
   * Go in the order of the next button
      * Compare vs gitlens output
   * If file totally changed, may just re-do whole file
   * Still can just proofread after Gitlens has identified a change
   * Only may want tag if file moved
* Proofreading can also just hover over the link too
* Button_(computing) find all and insert
* Vim series to tools page
* Should read E4s everywhere because it is a plural compound noun
   * Compared with AAAAAA, which is "owned"
* Numerical conda packages deal with at some point, when writing about Jupyter?
   * Or say the user guide provides additional examples, but learn more hear
      * Also link to examples and user guide?
   * Link to the a6 table
* PDF version of sample-doc?
   * Note not show up in PDF form?
* Should check doc8 output when proofreading
* Find all for "inside" and link to wiki-pg path
* A moved document
   * Compare working tree with branch or tag
   * Usually GitLens will say :guilabel`R` for renamed
      * But sometimes shows ``A`` and ``D`` in two places
   * If file moved, open the new one in an editor
      * Can do this by clicking it in GitLens
      * Select the old one in GitLens then say compare with working file
   * Open doc/indices/links.rst in editor
      * Compared with doc/getting-started/references/links from 0.3.1
* Move environment setup into dev/intro
   * Merge the conent from dev/intro onto the introduction page as a header

## Napoleon
* Use :obj: when not just one simple type
* The intersphinx target in use is outdated
   * Use the orphan document:
      * https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html#example-numpy
* Only have an extra line at end when the docstring is inside a class
   * Not for a module level variable
   * Actually, doesn't hurt

        Parameters
        ----------
        param1 : str
            Description of `param1`.
        param2 : :obj:`list` of :obj:`str`
            Description of `param2`. Multiple

## User guide restructuring
* Intro
   * Show how to install via conda, etc
   * For now, use pip install -e and the package name
      * This will end up being the lowest-priority option later on?
* Any examples just assume package has been imported
   * Can do by running book inside src folder or adding to path
* Fundamentals
   * Introduction
      * Talk about what this section is for
   * Transactions
      * Per PEP257, __init__ should have docstring
         * Just mention attributes in class docstring, others in __init__
         * Explain in initialization
      * Move the possible kinds into the kinds docstring
      * Have require args/kwargs per real python
      * https://docs.python.org/3/glossary.html#term-parameter
      * per_share_amount is defined twice
      * Table of kinds should say exchange money for a security
         * exchange a security for money
      * Receive money from a security (typically dividends)
      * Make sure to update quickstart if you change variable names
      * ISO8601
      * Transaction types tell brokerage account what to do (like git)
         * Buy, sell, contribute, withdraw, receive (dividends), pay (fees)
      * Change num_shares to just shares
      * Show an examples of what it means to initialize a transaction
         * In that section
   * Connectivity
      * Connect to robinhood
         * Robinhood tools section
         * API: a way for software to communicate with other software
      * Make a robinhood module
      * Download a transaction
      * Need a way to store it...
         * Motivation for ledgers
   * Ledgers
      * Subclass of a dataframe
      * Use int instead of decimal
      * Properties at a certain time
         * Holdings
            * Dict from symbols to shares
      * Some properties here (in ledger.py module) may be explained later
* Performance
   * Introduction
      * Net asset price
      * Contribution event (either a withdrawal or a contribution)
      * contribution-independent ledger coefficient (CILC)
      * Here include the matplotlib plot directive with:
         * Use the examples from CIIC entry in financial journal
      * To do this, we will need to get quotes, which motivates next page
   * Quotes
      * Add to the robinhood module
   * Ledger additions
      * Net asset price at a point in time
      * Just concise pandas calls, no loops
   * Subledgers
      * Based on how you want
   * After you get a plot to show, put on home page
      * Do you want to make something like this? Keep reading!
* Picking
   * Coming soon: how to pick stocks

## Developer guide
* Distributing section has data section
   * How to anonymize your transaction data
   * Simply hashes symbols, multiplies by random number?
   * Save as a .pkl
   * Can then use this data for pytest on ledger and performance data
   * Make a jupyter notebook with commands not yet run
      * Commit it, then run it, then clear all, then check diff
         * Shouldn't reveal any data
* Testing section goes by module?
   * Intro says more or less these were written as user guide was made
* Proposal to enhance AAAAAA (PEAs)
   * Require a whitepaper if someone wants to contribute
   * Keep this in the indices section?
   * PEA1 is you writing a PEA about how to contribute

## Data integration
* Consider pandas_datareader
   * Has a wrapper for instant quotes off alphavantage
* There is an alphavantage wrapper at github romelTorres/alpha_vantage
* Also coyo8/sec-edgar
   * Downloads in pdf form
* Just use robinhood if can get away with it

## Passwords
* Use an environment variable like in pandas_datareader?
* Use corey schafer tutorials?
* Use python secrets library?

## Jupyter
* When split off nbs page from doc page, re-do header levels on doc page
   * Also need to update concepts index page
* Should have concepts notebooks page
* Do all official 10 minutes to "x" tutorials in one notebook
   * On examples page mention official-tutorials.ipynb
* https://jupyter.org/try
   * Shows how to make the lorenz interactive sliders
* jupyter --paths
   * Shows how to edit configs
* Read the docs
   * https://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html
   * Talks about configs
   * Should add to Jupyter tools and configs options
* Use the editor extension
* Dark themes mess stuff up
   * Edit it yourself if you really think it's necessary
      * Just background, heading, and markdown text colors
   * Save the config
* Dev env setup, don't need to open a new notebook to set nb extension themes
   * Just find nb extensions tab from home screen
* Update the documentation.rst jupyter section
* All jupyter notebooks should be able to be viewed
   * If you add one, must be able to access it from the AAAAAA nb viewer link
* Verify all Jupyter notebooks are linked
* Link a Jupyter notebook per Carol Willing video
* Make an examples page with Jupyter notebook to follow along
* Tip to open the nb viewer
* TOC for all Jupyter notebooks?
* Need a way to include he nbs directory
* Need a table that says which doc pages link to which nbs
* Each doc that links to an nb also says which nb it links to
* Add to nbs concepts page
   * Say links in them may not be in links page
   * Core content is distilled into .rst
* Procedure for linking an nb says the two places that must be update
   * Link to this procedure in the nbs concepts page
   * Link to it in the nbs toc page
* examples page is a jupyter notebook you can reset and run all cells
* Use one common file to prototype LaTeX
* The Anaconda table needs to link to a purpose
   * For Jupyter, numpy, matplotlib, and pandas
* https://nbsphinx.readthedocs.io/en/rtd-theme/index.html
   * Can embed jupyter plots
* Can use Jupyter to prototype, matplotlib to embed
   * However, matplotlib can take some time to load
* Add a Jupyter configurations page
   * Talk about the notebook extensions, etc
* Update the Jupyter row in the a6 table

## Dev Order
* Write up testing first before packaging
   * Do what you know first
* Update ISO8061 then do testing

## Examples page
* Say can do either in the interpreter or in Jupyter notebook
* Then put in a link from jupyter page
* Python tools section should link here

## Doc coverage
* Figure out how to do this
   * The packaging video on iPad may help
* Doc coverage is a sphinx extension

## pytest
* Get pytest from home dir to actually run....
* Cite DO-178B
* Have a test index in the developer's guide
   * The pytest entry on the links page should link here
      * Framework for :ref:`writing test code <test-index>`
* Document test_ledger.py
   * Add a section to common tasks about testing
   * May need to update the quickstart guide
* Document test_utilities.py
* Get files to import via AAAAAA.ledger, not src.AAAAAA.ledger for tests
* tests should be motivated by the examples page
* On the code structure page, update the dir tree
   * Use a table for each of the components like on the other dir trees
      * name, function

## src updates
* Use corey schafer url post video from iPad to explain concept
* Already have the link for autofunction in napoleon links if need to describe
* User sections for "tracking" and "choosing"
* Give an example of initializing a transaction class
* ISO 8061 (or whatever robinhood uses) for dates
* xref in transaction source code
* Transaction class then explains how file structure is
   * For importing the module, etc.
* Then say we need to talk about the dir structure
   * Then make the dir tree script
* Explain how Transaction is, of course, all part of a module
   * Then describe automodule and show below
   * Then, enable modindex
* use datetime.datetime with zulu time - call the instance variable "when"
* Restructure other attributes as necessary
* change kinda to a dict of str to tuple(bool,bool)
   * bools say is associated with ticker
   * Second says does it result in add or subtract to buying power
* overload + to add two transactions and yield effect on the brokerage
* As you segway into explaining file structure
   * https://docs.python.org/3/tutorial/modules.html
   * Should help you get ready to package on conda
* Add to python tools description as you go
* Run https://docs.python.org/3/tutorial/modules.html#the-dir-function
* https://docs.python.org/3/tutorial/modules.html#packages
* Then, use https://docs.python.org/3/library/argparse.html#module-argparse
   * Draw a dir tree?
* Uncomment module index on homepage, verify it works
* Re-write the jupyter section after the jupyter examples page is live
   * Will need aaaaaa usage on the examples page
   * The numerical analysis packages should link to tools-numpy, etc.
* Tables can line break in the title without quotes
   * See VS code extensions
* Add a csv table to the concepts-code page once you have more references
   * Packges, __init__, setup.py, etc.
   * As you go through and explain
* Because AAAAAA are colloquially known as alnoki's apps
   * We are going to import as aa

## Writing procedures
* Use draw.io to make an SVG
* Where to keep the .xml?
* Always use code block
   * Use >>> if shouldn't be able to copy-paste
* Use vs code sort imports

## AAAA (analyst archives)
* Jupyter SVGs should have the date on which they were generated
* Reasons not to buy something
* Colloquially known as alnoki's arcks
* Terms for p/e ratio, book value, etc
* alnoki's algorithmic analysis archives
* Shows how your portfolio is, etc
* All print outs should have iso8601 of when generated
* INSURANCE
   * I need something underwritten: ridiculous assets nobody can explain
   * Cite wolf of wall street, it is just fairy dust

## adp.py
* Makefile wraps adp.py
   * make obj sphinx calls adp which searches through conf.py
   * make dev opens a website and watches src directory
   * make clean does cd doc, make clean, the cd ..
* Put on procedures home page?
* Use option directive https://virtualenv.pypa.io/en/latest/reference/#options
* An intersphinx that automatically grabs the intersphinx target from conf.py
   * adp.py objs rtfd
* https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/lists_tables.html#option-lists
* autodoc it on the procedures index page
* Cite the checklist manifesto
* arg parse from early on in python tutorial
* Talk about utils.py in AAAAAA root?
    * code for writing dir tree
        * Take command line args
* Wrapper for sphinx-autobuild
    * Says which folders to watch
    * Simple command line prompt:
        * python utils -doc
* Explain how the terminal opens at top aaaaaa dir, so use argparse
   * For wrapping autobuild, etc.
* Use the command line options style of table
   * See the RTD theme
   * Add this to the sphinx autobuild options once you know how to do it
* Have one that automatically opens a :ref: or a :doc:
   * python adp ref-tools-restructured-text

## VS Code
* Keyboard shortcuts print page
* https://code.visualstudio.com/docs/getstarted/tips-and-tricks

## Wrapping autobuild
* Make it run in command line
   * Only open html files that have been changed, after the build started
   * Shows how the argument parser, etc. works from command line
   * Appears that it only opens a browser the first time
* Run your own python script that looks for touched .html files
   * Open a new window if the browser doesn't already have it open
   * How to know whether to open a new window or to reload the old one...
      * Need to check if the server isn't already "serving" the page?
* Don't bother integrating with makefiles, it doesn't work on windows too...
   * https://www.gnu.org/software/make/manual/make.html#Phony-Targets
* Later, may want to incorporate --watch jupyter notebooks
   * Just incorporate to the autobuilder
      * The wrapper should then handle the html monitoring correctly
* Potentially just have one script to call
   * Make sure python doesn't go crazy and open eveything
      * Only open changed pages, not new pages?
      * Guard: only if the .rst and the .html were changed?
   * Make clean at the end?
      * Would this make you have to re-intersphinx everytime?
* Keep in mind that autobuild sends out some sort of ping or hook
   * You could somehow monitor this?
* See https://docs.python.org/3/tutorial/modules.html
* Have the wrapper put the output to the console
   * See autobuild for how this is done, because it wraps sphinx
   * https://docs.python.org/3/library/argparse.html#module-argparse
* Watch the server that autobuild makes
   * https://pythonhosted.org/watchdog/index.html
   * It should send out some sort of ping that says to reload
   * Only open a new browser window if the html file in question isn't served
      * And if a reload ping came
* When the html file changes, the autobuild console should say so
   * Have the wrapper look for this and then open up a new browser?

## Packaging
* Update copyright year in versioning
* See the project management -> distribution section of links
   * Update the comment for requirements files?
* After making a packaging section, link to it from the top of the code.rst pg
* Reciprically link with the project directory structure
* https://anaconda.org/conda-forge/doc8
   * This one is showing on anaconda cloud....
* Tools section on PyPI
* Currently, the link to pip already exists
* Do this first!
* Section on writing tests and packaging in dev-guide
* Try out with the 0.3.0 codebase
* First get onto PyPi
    * https://packaging.python.org/tutorials/packaging-projects/
* Then, can try adding to conda-forge
    * https://conda-forge.org/docs/
    * There is a sample file that just points to PyPi
    * https://github.com/conda-forge/staged-recipes/blob/master/recipes/example/meta.yaml
* PEP 328
* yaml should freeze at last release and then update each release
   * Sort of depends on Travis
* Update license
* https://stackoverflow.com/questions/448271/what-is-init-py-for
* https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html
* Ship conda with the dependencies
   * Then can install in the quick start
      * Mention you have just started the python interpreter with link
         * Link is in the floating point rampage
* Push to conda and create procedures as you go
* https://packaging.python.org/tutorials/packaging-projects/
   * Go through the tutorial and upload to test pypi
* https://choosealicense.com/
   * Probably MIT
      * Need to have a versioning section that says to update year
* https://packaging.python.org/guides/distributing-packages-using-setuptools/
   * More info about setup tools
* The examples page (if in Jupyter) should link to interactive analysis
   * In the Anaconda a6 table
   * Also, the Code testing link should go to the test index
   * And, the numerical analysis parts should get links
* Make sure to do Conda-forge packaging too

## Git
* Need to do a fetch before checkout a remote branch with tracking

## Doc
* TOC for everything page?
* Software also has an auto-api section?
   * May enable module index
* When conda finally gets sphinx rtd theme 0.4.3 (or whatever it is)
   * Are the settings different?
      * How far down can the stick TOC go?

## Proofreading
* Use [inline view](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_git-integration)
   * If only part of file changed
* what-next should explain how to navigate with the sidebar
   * If viewing in website form

## myPy
* Add to tools testing section and create TOC
   * Same with Travis?
* ttps://code.visualstudio.com/docs/python/settings-reference#_mypy
* MyPy type linter
   * https://www.python.org/dev/peps/pep-0526/
   * https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
      * Get the mypy linter going in the conda package
   * VS Code linter
      * https://code.visualstudio.com/docs/python/linting
         * Make a type checking procedures page
         * Talk about how to disable the pep8 colon warning but leave mypy on
* Figure out how to show all lines in rst files that are too long
* :pep:`Type hint theory <483>`
   * Compare to https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
* :pep:`Variable annotations <527>`
* :doc:`Typing module <python:library/typing>`

## Downloading transaction history from Robinhood
* If transaction type isn't recognized, just skip over it
   * Print out that a .json object was obtained that was unknown
* After downloading, the pandas portfolio parser (PPP) does checksum
   * Does net portfolio amount equal buying power?
* Need a logger / other way to harvest syntax from others
   * What does a stock split or withdrawal look like?
      * You can easily simulate withdrawal, then can put right back in

## Transaction updates
* When transaction init gets an error, should
   * Raise error
   * Show a trace to the data that produced it
* Class method to convert to a dataframe?
   * Could have a subclass of DataFrame called ledger
      * By merit of existing, it has already been sanitized
         * Thus can go straight back into transactions
   * Would already have sanitized data

## gitignore
* Explain what different things can cause gitignore to have contents
   * Pytest/compiled python, etc
* Make a development task to clean it out?
* Do a commit that is just cleaning out .gitignore

# 0.6.0

## Derived version statistics
* Only made date the index when exporting to first .csv
* Use df.r_type.value_counts(), etc
* Try exporting to .rst for include::
* Per minor release, get average difference in metrics
   * N commits
   * PPP
   * AAA
   * Time
   * Have this print out to a text file that can be literal included?
      * Use the :include: directive
* Also say time between releases?

## plot directive
* On home page
* Feeling super fancy?
   * Exit interpreter
   * Conda install matplotlib
   * Then do the matplotlib code
* Use the in-line version that shows the sample and the plot
* Matplotlib plotting need to change packages setup phase
   * Also go off conda install procedure
   * Same for numpy and pandas? Since will embed them?
* Search links for the word plot and link to matplotlib tools section
* https://matplotlib.org/sampledoc/extensions.html
* Appears to be included with matplotlib
* https://matplotlib.org/devel/plot_directive.html
* Need to include matplotlib and numpy in documenting package
* Make a factorial plot on the homepage
   * If you want to run this, you may need to install matplotlib with anaconda
      * See what happens when you do it from inside python
         * What pops up?
* Try out on homepage
* Search links for the word plot and link to matplotlib?
* Create a section in tools on Matplotlib
* matplotlib sample doc
* Have an example page in iPython
   * Show link to the actual notebook so people can play around with it
* Integrate plots
* Link Jupyter
* Try out log base 16 of factorial of x
* On links page, the jupyter general link says plotting, should link
   * Link to matplotlib

## Content card
* AnaKAHNndaKAHN 2019?
* Front
   * :term:`AAAAAA`: link :xref:`everywhere`
      * At bottom:
         * * 'everywhere' : ("The internet", url['Wiki pg] + 'Universe')
   * Have your email and your website
* On back, explanation field list
   * Just make the window smaller in order to view it
* Use version 0.3 field list

## kwarg passing

   - In Python 3 you can use a bare "*" asterisk
   - in function parameter lists to force the
   - caller to use keyword arguments for certain
   - parameters:

   >>> def f(a, b, *, c='x', d='y', e='z'):
   ...     return 'Hello'

   - To pass the value for c, d, and e you
   - will need to explicitly pass it as
   - "key=value" named arguments:
   >>> f(1, 2, 'p', 'q', 'v')
   TypeError:
   "f() takes 2 positional arguments but 5 were given"

   >>> f(1, 2, c='p', d='q',e='v')
   'Hello'

   -  Python 3.5+ allows passing multiple sets
   -  of keyword arguments ("kwargs") to a
   -  function within a single call, using
   -  the "**" syntax:

   >>> def process_data(a, b, c, d):
   >>>    print(a, b, c, d)

   >>> x = {'a': 1, 'b': 2}
   >>> y = {'c': 3, 'd': 4}

   >>> process_data(**x, **y)
   1 2 3 4

   >>> process_data(**x, c=23, d=42)
   1 2 23 42

## Robinhood time
* https://stackabuse.com/converting-strings-to-datetime-in-python/
   * Do strptime
   * https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
   * Have a robinhood.py file
      * module variable robinhood.date_format
         * '%b %d %Y %I:%M%p' or similar
* https://docs.python.org/3/library/datetime.html#datetime.datetime
   * Looks like robinhood is already in correct format
   * https://github.com/sanko/Robinhood/blob/master/Order.md#place-an-order
* Assume all times are zulu to avoid confusion
* Use a Naive timezone, assume zulu

## Robinhood integration
* Services setup
   * Robinhood
   * Will require its own setup section, adding to .yaml, etc
* Can do later:
   * AlphaVantage
   * Google Sheets
   * EDGAR
* Use Corey Schafer password tutorial
* [Unofficial Robinhood API documentation](https://github.com/sanko/Robinhood)
* GitHub Robinhood modules
   * [version with 736 stars](https://github.com/Jamonek/Robinhood)
   * [version with 30 stars](https://github.com/westonplatter/fast_arrow)
   * [version with 27 stars](https://github.com/mstrum/robinhood-python)
* RegEx
   * https://regexr.com/

## Zen page updates
* Go through and re-write/re-link once there are more places to link to
* Tools of Titans
   * You'll be overwhelmed with references, but remember...
   * The good *stuff* sticks

## Pandas ledger class
* Make a ledger a sub class of a dataframe
   * Use super like in https://realpython.com/python-super/
      * Also has inheritance tutorials, OOP:
         * https://realpython.com/python3-object-oriented-programming/

## Proofreading
* Delete base_url from conf.py or defer until later

# 0.7.0

## Tools re-linking
* See the a6 table
   * Need to link Numpy, Matplotlib, Jupyter, etc.

## KFREAP
* Kalman filter recursive estimator of asset price
* You reap what you (KF)SOW?
* Use price position, velocity, acceleration
   * https://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html
* Make so you can nominalize to a percentage when you inject to the portfolio
* Use simpson integration
   * If not here, at least somewhere else


## robinhood user data
* Have a .txt file that denotes portfolios
* Have a way you can use google drive to store data

## alnoki's analysis archives
* A new section with a ton of plots
* Use SVGs with the date embedded in each one

# *0.0 Package release

## Main functionality
* Download a Robinhood history to a pandas DataFrame
* MVP (minimum viable prototype)
* Package per the YouTube tutorial by the freelancer, link on iPad
* Make sure the downloadable PDF version is okay

## Deployment
* Use iPad video
   * Travis
      * Add link to willing talk too?
   * Coverage for both code and docs
* Coverage.py for testing framework
* Per Carol Willing talk
   * Make spelling test with exception words
   * Links for topics in csv table, like spellchecking, etc.
   * Links for package deployment talk
* __init__.py should have docstrings too per {PEP257 (?)}

## Setup page
* For the python enthusiast
   * Conda install AAAAAA
   * pip install AAAAAA (?)

## Linking
* Import times from the iPad speech about packaging
   * Shows code coverage
   * Link to the topics when you get around to it
      * Link to every topic from a csv table
* Make sure all topics from the willing speech are linked too

## Transaction code
* Do original tutorials but with financial data
* NaN in GoogleSheets should be different than $0
* __repr__ should sanitize inputs
* Need a to_string()

# **0 BTMF
* Can't be a coefficient, because sign of you and market could be different
* Should just be a percentage positive or negative

## Main functionailty
* Adds PARDAFA and BTMF versus CRSPTMT
* Cast a portfolio into a Pandas dataframe then plot
* ABC: Annualized BTMF coefficient
   * (APR of alnoki) / (APR of CRSPTMT)

# 1.0 and on

## General ideas
* See all notebook entries since Dec 26
   * Leisurely review paper notebook notes for more ideas
* Robinhood interface to Google sheets?
   * Make an AAAAAA GSheet and update the associated GDrive document ledger
* RODCA with LaTeX?
* Do some fun stats first just for fun
   * Those goons at instutions don't know DSP
   * The patterns are there
* Watch realpython video courses on iPad
* Compare 52 week lows with CRSP small cap value
   * See what is common to both?

## Investing philosophy page?
* For The Intelligent investor, can link to another "concepts page"
   * The 7-step checklist, etc.
* See other investing references from urls on Google Drive
* Warren Buffet BRK website
   * Fair price wonderful company vs wonderful price fair company
* Easy to be small guy vs hunting elephants
* Growth in book value per year as a metric?
* Standard and Poors facilitated the 2009 crisis
   * This is why we use CRSPTMT
      * Also it is academic

## Numerical analysis
* https://scipy-cookbook.readthedocs.io/
   * https://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html
* https://web.stanford.edu/~schmit/cme193/
   * has seaborn and pandas examples
   * Predictor of survivor on Titanic, powerful statistical modeling tools
* [RealPython.com Pandas optimization](https://realpython.com/fast-flexible-pandas/)
* Other references from Python training logs on Google Drive