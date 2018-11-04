# AAAAAA
Alnoki Algorithmic Analysis Asset Allocation Advisor

*Brought to you by alnoki*

## Philosophy
1. Testing and documenting up front prevents massive runtime debug headaches
2. Code shall be DRY (don't repeat yourself): decompose as much as possible
3. Documentation shall enable another to re-write source and test code
4. Test code shall be STUPID simple. Avoid recursion of 'testing the test code'
5. Documenting & testing forces code to be considered from various perspectives
6. Consider DO-178B as a model for software design assurance
7. PEP8 provides a repeatable and official means for formatting

## Project structure
1. `src`: Source code
2. `test`: [pytest](https://docs.pytest.org) modules for testing source code
3. `doc`: [Jupyter Notebook](http://jupyter.org/) documentation of `src`, `test`, and `dev`
    1. `dev` includes walkthroughs done during experimental code creation

## Design procedures
1. Update `doc` for `test` and `src` after incremental developments
2. pytest with the VS Code debugger
3. Write tests and design source code in cyclical stages
    1. C-style/speed-optimal source code with repeat code as necessary
    2. Design test code without any clever tricks (STUPID simple)
    3. Rearrange source code for maximal decomposition, not speed
    4. Update `doc` for `test` and `src` after the incremental development
    5. Optimize for speed only when needed

## Recommended documentation review order
As documentation was written, various Python terms were explained with hyperlinks so as to provide a means for teaching. To review documentation in a sequential order that will elucidate various concepts throughout the software architecture, it is suggested that documentation be read in the order in which it was written:
1. `dev`\\`ledger`
2. `src`\\`ledger`
3. `src`\\`utilities`

## Select references
1. [Python.org documentation](https://docs.python.org/) and [tutorial](https://docs.python.org/3/tutorial/index.html)
2. [Corey Schafer YouTube playlist: Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
3. [codebasics YouTube playlist: Pytest Tutorial (Python Automated Testing)](https://www.youtube.com/playlist?list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu)
4. [pytest.org homepage](https://docs.pytest.org) and [tutorials](https://docs.pytest.org/en/latest/contents.html)
5. [VS Code Python tutorial](https://code.visualstudio.com/docs/languages/python) and [unit testing documentation](https://code.visualstudio.com/docs/python/unit-testing)
6. [Anaconda user guide](https://docs.anaconda.com/anaconda/user-guide/) and [cheat sheet](https://docs.anaconda.com/_downloads/Anaconda-Starter-Guide-Cheat-Sheet.pdf)
7. [alnoki Jupyter notebooks and sample code from assorted tutorials](https://github.com/alnoki?tab=repositories)