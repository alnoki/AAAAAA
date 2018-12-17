# Proof reading

Code
AAAAAA source code is available at the AAAAAA repository, and alnoki's
GitHub repositories contain some additional content from relevant tutorials
Structure should be a dir tree

Documentation
Talk about what is actually used to write the documentation - copy links from the reference page
Split up the two links into bullet points
Keep the 3 space indentation comment
Use the 2-line indent and link directly to an example from the two references

Jupyter Notebooks are used for an interactive style of development
during "whiteboard" stages of a project (reference Brett Glasner)
References to relevant notebooks should be found through AAAAAA documentation

Using Intersphinx
Clean up, syntax shouldn't be inside of a tip
Reference the roles document about :xref:`Custom link <xref-ext>`
Use an rst code block and show output
Don't have a tip about the base url dictionary
Use a Python term to talk about the base url dictionary
Take out the delimiter comment note

Building documentation take out tip

References
The intersphinx explanation at the top should be more concise
Corey Schafer link to xref python, same for below sentence
Python tutorial -> Official tutorial from "Python.org"
Conda -> command line configurator for Anacondaa
Cyberciti.biz -> how to change :program:Terminal prompt
Pytest -> official [pytest](the actual intersphinx for pytest), same on next line
	copy-paste from the 3rd line
AAAAAA codebase linnk to GitHub.com should be live link -> source code, test code, and documentation
alnoki's repositories 0-> link to Jupyter Notebooks with capital N
	Also use for next line, get the intersphinx handle from the documentation page
Sphinx-> official documentation for the [Sphinx](instersphinx) documentation engine
Carol willing -> Jupyter Notebooks with cap N intersphinx, intersphinx for Extensions and Autodoc
Python dev guide -> reST should link to docutils xref
Read the Docs Sphinx theme -> A Sphinx theme for creating....
Mahdi Yusuf -> intersphinx to quickstart and toctree and reST
	He should be at top of the section
	With Read the Docs section should be first under Sphinx
reStructuredText Primer -> Sphinx documentation explanation of [reST](intersphinx)
Next two items same thing
Jupyter xref Python, "format used for algorithm development"
	Xref to LaTeX, markdown, etc.
xref to Corey Schafer jupyter tutorial
xref to markdown link (that shows up from inside Jupyternotebook help menu)
xref to the markdown table generator
Managing references section---
Intersphinx->Official extension documentation from [Sphinx](intersphinx) website
Michael Jones -> intershpinx to Sphinx name
Intersphinx inventory parser -> remove word Sphinx
NumPy/Matplotlib -> Instructions to reference numerical analysis and plotting tools via....
Factorial -> wikipedia.org should be a live link
Mathematics sphinx LaTeX ref, which should yield a LaTeX xref
VS Code -> development, testing, and documentation -> has marketplace with extensions
	developed by open source community
RST preview extension -> should xref to reST -> live preview functionality



## TODO
1. AAAAAA as a glossary term
1. Explain single vs double quotes style in python strings
1. Get intersphinx working with additional sites
    1. Sample `reST` code
        1. [Python developer's guide to documenting](https://devguide.python.org/documenting/)
            1. reST code should be 80 columns wide
        1. [matlibplot sampledoc tutorial](https://matplotlib.org/sampledoc/)
        1. [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/latest/)
        1. [Read the Docs table/admonition syntax](https://learning-readthedocs.readthedocs.io/en/latest/Options/table.html)
    1. Using `autodoc`
        1. [Sphinx autodoc feature](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
        1. [Numpy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
        1. [Napolean for numpy docstring support](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon)
    1. Sphinx walkthroughs
        1. [Brandon's PyCon Sphinx tutorial on Read the Docs](https://brandons-sphinx-tutorial.readthedocs.io/en/latest/index.html)
            1. [PDF form](https://media.readthedocs.org/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf)
1. Migrate readme to Sphinx
1. File away:
    1. https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
    1. http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
    1. [External links extension](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#use-the-external-links-extension)
    1. https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext
1. Per Carol Willing talk
    1. Link a Jupyter notebook
    1. Make spelling test with exception words
    1. Import video annotation times from iPad notes
        1. Get link from below too, the packaging/deploying/etc. video
1. Get a `<project name>` sort of reference in docs for AAAAAA
1. Autodoc with source files and numpy style
1. Numbering in references page should restart automatically
1. Developer's page with 80 lines vs 72, etc. and how to do in VS code
    1. PEP8 2 spaces for comment
1. DO-178B link for Zen page
1. Markdown table generator for Jupyter
1. Split up links in all .rst files
1. Get a toctree to render inside the references page
1. `pip install -e` for using package with `pytest` to `dev tasks`
1. Link official python developer's guide in `development` pages
1. Link DO-178b
1. Linkcheck intersphinx
1. Install DOC8 linter for reST extension
1. LaTeX external reference
1. Make sure all links are in as necessary
1. Items from paper notebook
1. Read through all documentation out loud at then end of above updates
1. Keep on hand a section for out-loud proof-reading
1. Use the live render in the reST pluging
1. Figure out what uncommenting indices and tables in index.rst will do
1. Tools should have additional non-open source section:
    1. Robinhood
    1. alphavantage
    1. Google sheets
1. Plan out actual source code dev design when website is all ready
    1. Robinhood interface to Google sheets
    1. RODCA with LaTeX

## Design procedures
1. Update `docs` for `test` and `src` after incremental developments
1. pytest with the VS Code debugger
1. Write tests and design source code in cyclical stages
    1. C-style/speed-optimal source code with repeat code as necessary
    1. Design test code without any clever tricks (STUPID simple)
    1. Rearrange source code for maximal decomposition, not speed
    1. Update `docs` for `test` and `src` after the incremental
    development
    1. Optimize for speed only when needed

## Recommended documentation review order
As documentation was written, various Python terms were explained with
hyperlinks so as to provide a means for teaching. To review
documentation in a sequential order that will elucidate various
concepts throughout the software architecture, it is suggested that
documentation be read in the order in which it was written:
1. `nbs`\\`dev`\\`ledger`
1. `nbs`\\`src`\\`ledger`
1. `nbs`\\`src`\\`utilities`