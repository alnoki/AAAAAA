# AAAAAA
Alnoki Algorithmic Analysis Asset Allocation Advisor

*Brought to you by alnoki*

## Philosophy
1. Testing and documenting up front prevents runtime debug headaches
1. Have DRY (don't repeat yourself) code: decompose as much as possible
1. Documentation should enable another to re-write source and test code
1. Have STUPID simple tests. Don't recursively 'test the test code'
1. Documenting & testing forces consideration from various perspectives
1. Consider DO-178B as a model for software design assurance
1. PEP8 provides a repeatable and official means for formatting
1. Legacy conventions shouldn't prevent a new worthwhile philosophy
1. Play around and "whiteboard" code during initial stages

## Project structure
1. `src`: Source code
1. `test`: [pytest](https://docs.pytest.org) modules for testing source
code
1. `docs`: Documentation created via recommended [Read the Docs](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#quick-start)
procedure
1. `nbs`: [Jupyter Notebook](http://jupyter.org/) documentation of
`src` and `dev` (nbs = 'notebooks')
    1. `dev` includes walkthroughs done during experimental code
    creation
    1. `src` includes some documentation pre-[Read the Docs](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#quick-start)
procedure

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

## Select references
1. [Python.org documentation](https://docs.python.org/) and [tutorial](https://docs.python.org/3/tutorial/index.html)
1. [Corey Schafer YouTube playlist: Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
1. [codebasics YouTube playlist: Pytest Tutorial (Python Automated Testing)](https://www.youtube.com/playlist?list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu)
1. [pytest.org homepage](https://docs.pytest.org) and [tutorials](https://docs.pytest.org/en/latest/contents.html)
1. [VS Code Python tutorial](https://code.visualstudio.com/docs/languages/python) and [unit testing documentation](https://code.visualstudio.com/docs/python/unit-testing)
1. [Anaconda user guide](https://docs.anaconda.com/anaconda/user-guide/) and [cheat sheet](https://docs.anaconda.com/_downloads/Anaconda-Starter-Guide-Cheat-Sheet.pdf)
1. [alnoki Jupyter notebooks and sample code from assorted tutorials](https://github.com/alnoki?tab=repositories)
1. [Changing bash prompt](https://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html)
1. [Read the Docs external resources](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#external-resources)