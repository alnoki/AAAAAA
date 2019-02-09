# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('exts'))  # For xref
sys.path.insert(0, os.path.abspath('../src'))  # For napoleon


# -- Project information -----------------------------------------------------

project = 'AAAAAA'
copyright = '2019, alnoki'
author = 'alnoki'

# The short X.Y version
version = '0.2'
# The full version, including alpha/beta/rc tags
release = '0.2.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'xref',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# The below options are for the Read the Docs theme, see
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,  # Render errors if using more depth
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AAAAAAdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AAAAAA.tex', 'AAAAAA Documentation',
     'alnoki', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'aaaaaa', 'AAAAAA Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AAAAAA', 'AAAAAA Documentation',
     author, 'AAAAAA', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
# Napoleon default settings, except turn off Google docstrings
napoleon_google_docstring = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('http://www.sphinx-doc.org/en/master/', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
    'rtfd': ('https://docs.readthedocs.io/en/latest/', None),
    'rtd-sphinx-theme':
        ('https://sphinx-rtd-theme.readthedocs.io/en/latest/', None),
    'py-dev-guide': ('https://devguide.python.org/', None),
    'anaconda': ('https://docs.anaconda.com/', None),
    'conda': ('https://docs.conda.io/projects/continuumio-conda/en/latest/',
              None),
    'matplotlib-sampledoc':
        ('https://matplotlib.org/sampledoc/', None),
    'sublime-with-sphinx':
        ('https://sublime-and-sphinx-guide.readthedocs.io/en/latest', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'nb-extensions': ('https://jupyter-contrib-nbextensions.readthedocs.io/en/'
                      'latest', None),
    'napoleon': ('https://sphinxcontrib-napoleon.readthedocs.io/en/latest/',
                 None),
}

# Base urls used by xrefs extension
url = {
    'GitHub': 'https://github.com/',
    'YT vid': 'https://www.youtube.com/watch?v=',  # Video
    'YT PL': 'https://www.youtube.com/playlist?list=PL',  # Playlist
    'Stack OF': 'https://stackoverflow.com/questions/',  # Question
    'Wiki pg': 'https://en.wikipedia.org/wiki/',  # Article
    'VS Code ext': 'https://marketplace.visualstudio.com/items?itemName=',
    'VS Code doc': 'https://code.visualstudio.com/docs/',
    'docutils': 'http://docutils.sourceforge.net/',
    'GitHub help': 'https://help.github.com/articles/',
    'RealPython': 'https://realpython.com/',
    'conda-forge': 'https://anaconda.org/conda-forge/',
    'git-scm': 'https://git-scm.com/',
    'linux-die': 'https://linux.die.net/man/1/',
    'VS Code': 'https://code.visualstudio.com/',
}

xref_links = {
    'Python': ('Python', 'https://www.python.org'),
    'xref-ext': ("Michael Jones' sphinx-xref repository",
                 url['GitHub'] + 'michaeljones/sphinx-xref'),
    'Willing-Sphinx': ("Carol Willing's Practical Sphinx talk from PyCon 2018",
                       url['YT vid'] + '0ROZRNZkPS8'),
    'Yusuf-Sphinx-RTD': ("Mahdi Yusuf's Sphinx & Read the Docs screencast",
                         url['YT vid'] + 'oJsUvBQyHBs'),
    'Anaconda': ('Anaconda', 'https://www.anaconda.com'),
    'AAAAAA-repo': ("AAAAAA repository", url['GitHub'] + 'alnoki/AAAAAA'),
    'Change-bash-prompt': ("Cyberciti.biz instructions to change bash prompt",
                           'https://www.cyberciti.biz/tips/howto-linux-unix-'
                           'bash-shell-setup-prompt.html'),
    'Corey-Schafer-vids': ("Corey Schafer YouTube playlist: Python Tutorials",
                           url['YT PL'] + '-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU'),
    'alnoki-repos': ("alnoki's GitHub repositories",
                     url['GitHub'] + 'alnoki?tab=repositories'),
    'intersphinx-numpy-matplotlib':
        ("Intersphinx with NumPy/Matplotlib", url['Stack OF'] +
         '21538983/specifying-targets-for-intersphinx-links-to-numpy-'
         'scipy-and-matplotlib'),
    'intersphinx-inv-parser':
        ("Intersphinx inventory parser", url['Stack OF'] +
         '30939867/how-to-properly-write-cross-references-to-external-'
         'documentation-with-intersphin'),
    'intersphinx-inv-targets':
        ("Intersphinx objects.inv explanation", url['Stack OF'] +
         '45699577/how-to-link-to-root-page-in-intersphinx'),
    'factorial-definition':
        ("Definition of factorial", url['Wiki pg'] + 'Factorial'),
    'GitLens': ("GitLens extension", url['VS Code ext'] + 'eamodio.gitlens'),
    'VS-Code-Python-ext':
        ("Python extension", url['VS Code ext'] + 'ms-python.python'),
    'RST-preview-ext':
        ("RST preview extension", url['VS Code ext'] +
         'lextudio.restructuredtext'),
    'Test-explorer-UI':
        ("Python Test Explorer Extension", url['VS Code ext'] +
         'LittleFoxTeam.vscode-python-test-adapter'),
    'VS-Code': ("Visual Studio Code", 'https://code.visualstudio.com'),
    'Jupyter': ("Project Jupyter", 'https://jupyter.org'),
    'VS-Code-Python-tutorial':
        ("VS Code Python tutorial", url['VS Code doc'] + 'languages/python'),
    'VS-Code-unit-testing':
        ("VS Code unit testing", url['VS Code doc'] + 'python/unit-testing'),
    'Writer-intro-to-Sphinx':
        ("Intro to Sphinx and Read the Docs", 'http://www.ericholscher.com/'
         'blog/2016/jul/1/sphinx-and-rtd-for-writers/'),
    'reST-documentation': (
        "reStructuredText documentation", url['docutils'] + 'rst.html'),
    'quick-reST': ("Quick reST reference",
                   url['docutils'] + 'docs/user/rst/quickref.html'),
    'Mac': ('Mac', url['Wiki pg'] + 'Macintosh_operating_systems'),
    'Windows': ('Windows', url['Wiki pg'] + 'Microsoft_Windows'),
    'Linux': ('Linux', url['Wiki pg'] + 'Linux'),
    'Wikipedia': ('Wikipedia', 'https://www.wikipedia.org'),
    'Google': ('Google', 'https://www.google.com'),
    'Garmin': ("Garmin Ltd.", url['Wiki pg'] + 'Garmin'),
    '219-Design': ("219 Design", 'https://www.219design.com/who-we-are/'),
    'DO-178B': ('DO-178B', url['Wiki pg'] + 'DO-178B'),
    'AHRS': ('AHRS', url['Wiki pg'] + 'Attitude_and_heading_reference_system'),
    'Python-quote-convention':
        ("Python quote convention", url['Stack OF'] + '56011/single-quotes-vs-'
         'double-quotes-in-python'),
    'AAAAAA-nbs': ("Jupyter Notebook viewer for AAAAAA", 'https://nbviewer.'
                   'jupyter.org/github/alnoki/AAAAAA/tree/master/nbs/'),
    'LaTeX': ('LaTeX', url['Wiki pg'] + 'LaTeX'),
    'YouTube': ('YouTube', 'https://www.youtube.com/'),
    'doc8-newline-issue':
        ("Doc8 newline issue fix", url['GitHub'] + 'vscode-restructuredtext/'
         'vscode-restructuredtext/issues/84'),
    'reST-cheatsheet': ("reST cheatsheet", url['GitHub'] + 'ralsina/rst-'
                        'cheatsheet/blob/master/rst-cheatsheet.rst'),
    'GitHub': ('GitHub', url['GitHub']),
    'Markdown': ('Markdown', url['GitHub help'] + 'basic-writing-and'
                 '-formatting-syntax/'),
    'Schafer-Jupyter': ("Jupyter Notebook Tutorial: Introduction, Setup, and "
                        "Walkthrough", url['YT vid'] + 'HW29067qVWk'),
    'tables-generator': ("Tables generator for assorted languages",
                         'http://tablesgenerator.com'),
    'http-socket-error':
        ("http socket error", url['Stack OF'] + '19071512/socket-error-errno'
         '-48-address-already-in-use'),
    'reST-list-indentation':
        ("reST list indentation", url['Stack OF'] +
         '5550089/how-to-create-a-nested-list-in-restructuredtext'),
    'documenting-python': ("Guide to Documenting Python",
                           url['RealPython'] + 'documenting-python-code/'),
    'open-source': ('open-source', url['Wiki pg'] + 'Open-source_software'),
    'RealPython': ('RealPython.com', url['RealPython']),
    'AAAAAA-zip-archive': ('AAAAAA repository archive', url['GitHub'] +
                           'alnoki/AAAAAA/archive/master.zip'),
    'VS-Code-settings': ("VS Code settings", url['VS Code doc'] +
                         'getstarted/settings'),
    'VS-Code-terminal': ("integrated terminal", url['VS Code doc'] +
                         'editor/integrated-terminal'),
    'command-palette': ("command palette", url['VS Code doc'] +
                        'getstarted/userinterface#_command-palette'),
    'VS-Code-interpreter':
        ("select Python interpreter", url['VS Code doc'] +
         'python/environments#_select-and-activate-an-environment'),
    'VS-Code-bookmarks-ext': ("Bookmarks extension", url['VS Code ext'] +
                              'alefragnani.Bookmarks'),
    'cmd.exe-invocation': ("cmd.exe options", 'https://ss64.com/nt/cmd.html'),
    'bash-man-page': ("bash shell manual", url['linux-die'] + 'bash'),
    'Doc8': ("Doc8 reST linter", url['conda-forge'] + 'doc8'),
    'git-manual': ("Git manual", url['git-scm'] + 'docs/user-manual.html'),
    'git-download': ("Git download", url['git-scm'] + 'downloads'),
    'git-book': ("Git book", url['git-scm'] + 'book'),
    'git-config': ('git-config', url['git-scm'] + 'docs/git-config'),
    'git-log': ('git-log', url['git-scm'] + 'docs/git-log'),
    'git-commit': ('git-commit', url['git-scm'] + 'docs/git-commit'),
    'git-push': ('git-push', url['git-scm'] + 'docs/git-push'),
    'git-clone': ('git-clone', url['git-scm'] + 'docs/git-clone'),
    'git-setup': ("Git setup", url['git-scm'] + 'book/en/v2/Getting-Started-'
                  'First-Time-Git-Setup'),
    'less-pager': ('less pager', url['linux-die'] + 'less'),
    'Vim': ("Vim text editor", 'https://www.vim.org/'),
    'Vim-tutorial': ("Interactive Vim tutorial", 'https://www.openvim.com/'),
    'Vim-cheatsheet': ("Vim cheatsheet", 'https://devhints.io/vim'),
    'list-git-developers':
        ("Listing Git project developers", url['Stack OF'] +
         '9597410/list-all-developers-on-a-project-in-git'),
    'git-log-formatting': ("Git log formatting options", url['Stack OF'] +
                           '1441010/the-shortest-possible-output-from-git-log-'
                           'containing-author-and-date'),
    'github-change-authors':
        ("GitHub.com instructions to change author history",
         url['GitHub help'] + 'changing-author-info/'),
    'git-branch-filtering':
        ("Git filter-branch options", 'https://devsector.wordpress.com/'
         '2014/10/05/advanced-git-branch-filtering/'),
    'VS-Code-extensions': ("Extensions", url['VS Code doc'] + 'setup/'
                           'additional-components#_vs-code-extensions'),
    'codebasics-numpy': ("codebasics NumPy tutorial", url['YT PL'] +
                         'eo1K3hjS3uset9zIVzJWqplaWBiacTEU'),
    'codebasics-matplotlib': ("codebasics Matplotlib tutorial", url['YT PL'] +
                              'eo1K3hjS3uu4Lr8_kro2AqaO6CFYgKOl'),
    'codebasics-pandas': ("codebasics pandas tutorial", url['YT PL'] +
                          'eo1K3hjS3uuASpe-1LjfG5f14Bnozjwy'),
    'codebasics-pytest': ("codebasics pytest tutorial", url['YT PL'] +
                          'eo1K3hjS3utzQYDNRNluzqJqpMXx6hHu'),
    'live-md-preview':
        ("Live Markdown Preview", url['GitHub'] + 'ipython-contrib/'
         'jupyter_contrib_nbextensions/tree/master/src/'
         'jupyter_contrib_nbextensions/nbextensions/livemdpreview'),
    'conda-forge': ('conda-forge', "https://conda-forge.org/#about"),
    'OS': ("Operating System", url['Wiki pg'] + 'Operating_system'),
    'VS-Code-insiders': ("Insider Edition", url['VS Code'] + 'insiders'),
    'pytest-discovery-issue': ("VS Code pytest issue", url['GitHub'] +
                               'Microsoft/vscode-python/issues/4099'),
    'print-dir-tree': ("Printing a directory tree", url['Stack OF'] +
                       '9727673/list-directory-tree-structure-in-python'),
    'directory': ("Directory", url['Wiki pg'] + 'Directory_(computing)'),
    'sha1': ('SHA-1', url['Wiki pg'] + 'SHA-1'),
    'realpython-type-checking':
        ("RealPython guide to type checking", url['RealPython'] +
         'python-type-checking'),
    'finance-security': ('Securities', url['Wiki pg'] + 'Security_(finance)'),
    'financial-asset': ("Financial asset", url['Wiki pg'] + 'Financial_asset'),
    'finance-stock': ('Stock', url['Wiki pg'] + 'Stock'),
    'corporation': ('Corporation', url['Wiki pg'] + 'Corporation'),
    'brokerage': ('Brokerage', url['Wiki pg'] + 'Brokerage_firm'),
    'ticker-symbol': ("Ticker symbol", url['Wiki pg'] + 'Ticker_symbol'),
    'finance-share': ('Share', url['Wiki pg'] + 'Ticker_symbol'),
    'finance-transaction': ("Financial transaction", url['Wiki pg'] +
                            'Financial_transaction'),
    'money': ('Money', url['Wiki pg'] + 'Money'),
    'medium-of-exchange': ("Medium of exchange", url['Wiki pg'] +
                           'Medium_of_exchange'),
    'USD': ("United States dollar", url['Wiki pg'] + 'United_States_dollar'),
    'finance-cent': ('Cent', url['Wiki pg'] + 'Cent_(currency)'),
    'dividend': ('Dividend', url['Wiki pg'] + 'Dividend'),
    'fee': ('Fee', url['Wiki pg'] + 'Fee'),
    'bank': ('Bank', url['Wiki pg'] + 'Bank'),
    # New links below, sorted links above
    }
