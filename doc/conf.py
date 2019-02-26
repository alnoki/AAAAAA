import os
import sys
sys.path.insert(0, os.path.abspath('exts'))  # For xref
sys.path.insert(0, os.path.abspath('../src'))  # For napoleon
sys.path.insert(0, os.path.abspath('.'))  # For conf.py in napoleon

extensions = [
    # Included from sphinx-quickstart
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    # Included with Sphinx
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    # Not included with Sphinx
    'xref',
    'sphinxcontrib.bibtex',
]
"""Which :doc:`extensions <sphinx:usage/extensions/index>` to use

Includes :ref:`extensions <tools-sphinx-extensions>` that are:

   * Automatically
     :wiki-pg:`installed <Installation_(computer_programs)>` via
     :doc:`sphinx-quickstart <sphinx:usage/quickstart>`
   * Selected from the
     :doc:`built-in Sphinx extensions <sphinx:usage/extensions/index>`
     for usage in :term:`AAAAAA`
   * Used for :term:`AAAAAA`, but not included in the
     :doc:`built-in Sphinx extensions <sphinx:usage/extensions/index>`
"""

project = 'AAAAAA'
"""What to call this :ref:`tools-sphinx` project"""

copyright = '2019, alnoki'
"""Basic :wiki-pg:`copyright <Copyright>`"""

author = 'alnoki'
""":github:`Who <alnoki>` even made this anyways?"""

version = '0.4'
"""Just ``MAJOR.MINOR`` for the :ref:`version <version-list>`"""

release = '0.4.0'
"""``MAJOR.MINOR.PATCH`` for the :ref:`version <version-list>`"""

master_doc = 'index'
"""The top-level :ref:`.rst file <tools-restructured-text>`

For :term:`AAAAAA`, is inside of the
:ref:`documentation root directory <concepts-doc-tree>`
"""

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
"""What to ignore

When :ref:`building documentation <sphinx-building-doc>`, don't use
:wiki-pg:`files <Computer_file>` or :wiki-pg:`paths <Path_(computing)>`
with these patterns
"""

html_static_path = []
""":wiki-pg:`Directory` with supplementary data"""

html_theme = 'sphinx_rtd_theme'
"""What the :wiki-pg:`website <Website>` should look like

For :term:`AAAAAA`, use the
:doc:`Read the Docs Sphinx Theme <rtd-sphinx-theme:index>`
"""

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': -1,
    'prev_next_buttons_location': 'both',
}
""":doc:`Read the Docs theme <rtd-sphinx-theme:index>` options

These are only :ref:`configured <concepts-configs>` if they differ from
the :doc:`default options <rtd-sphinx-theme:configuring>`
"""

linkcheck_ignore = [
    r'http://localhost:8000/_build/html/index.html',  # Manual
    r'http://127.0.0.1:8000'  # sphinx-autobuild
]
"""Ignore when :ref:`checking links <sphinx-checking-links>`

These :wiki-pg:`URLs <URL>` only exist when
:ref:`building documentation <sphinx-building-doc>`, so ignore them
"""

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
    'bibtex': ('https://sphinxcontrib-bibtex.readthedocs.io/en/latest', None),
    'pypa': ('https://pip.pypa.io/en/latest/', None),
    'pypa-guide': ('https://packaging.python.org/', None),
}

extlinks = {
    'wiki-pg': ('https://en.wikipedia.org/wiki/%s', ''),
    'real-py': ('https://realpython.com/%s', ''),
    'git-doc': ('https://git-scm.com/docs/%s', ''),
    'github': ('https://github.com/%s', ''),
    'yt-vid': ('https://www.youtube.com/watch?v=%s', ''),
    'stack-q': ('https://stackoverflow.com/questions/%s', ''),
    'yt-pl': ('https://www.youtube.com/playlist?list=PL%s', ''),
    'vs-code-ext':
        ('https://marketplace.visualstudio.com/items?itemName=%s', ''),
    'vs-code-doc':
        ('https://code.visualstudio.com/docs/%s', ''),
    'vim-wiki': ('https://vim.fandom.com/wiki/%s', ''),
    'docutils': ('http://docutils.sourceforge.net/%s', ''),
}

# Base urls used by xrefs extension: delete eventually after migrating
url = {
    'Wiki pg': 'https://en.wikipedia.org/wiki/',
    'GitHub': 'https://github.com/',
    'VS Code doc': 'https://code.visualstudio.com/docs/',
    'RealPython': 'https://realpython.com/',
    'git-scm': 'https://git-scm.com/',
    'VS Code': 'https://code.visualstudio.com/',
    'VS Code ext': 'https://marketplace.visualstudio.com/items?itemName=',
    'YT vid': 'https://www.youtube.com/watch?v=',
    'YT PL': 'https://www.youtube.com/playlist?list=PL',
    'Stack OF': 'https://stackoverflow.com/questions/',
    'docutils': 'http://docutils.sourceforge.net/',
    'GitHub help': 'https://help.github.com/en/articles/',
    'conda-forge': 'https://anaconda.org/conda-forge/',
    'linux-die': 'https://linux.die.net/man/1/',
    'pypi': 'https://pypi.org/'
}

xref_links = {
    'Python': ('Python', 'https://www.python.org'),
    'semver': ("Semantic Versioning", 'https://semver.org/'),
    'ottobib': ('OttoBib', 'https://www.ottobib.com'),
    'Anaconda': ('Anaconda', 'https://www.anaconda.com'),
    'Change-bash-prompt':
        ("Cyberciti.biz instructions to change bash prompt", 'https://www.'
         'cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html'),
    'dencode': ("DenCode", "https://dencode.com/en/date/iso8601"),
    'VS-Code': ("Visual Studio Code", 'https://code.visualstudio.com'),
    'Jupyter': ("Project Jupyter", 'https://jupyter.org'),
    'Writer-intro-to-Sphinx':
        ("Intro to Sphinx and Read the Docs", 'http://www.ericholscher.com/'
         'blog/2016/jul/1/sphinx-and-rtd-for-writers/'),

    # To sort
    'Wikipedia': ('Wikipedia', 'https://www.wikipedia.org'),
    'Google': ('Google', 'https://www.google.com'),
    '219-Design': ("219 Design", 'https://www.219design.com/who-we-are/'),
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
    'AAAAAA-zip-archive': ('AAAAAA repository archive', 'https://codeload.'
                           'github.com/alnoki/AAAAAA/zip/master'),
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
    'Doc8': ("Doc8 reST syntax checker", url['conda-forge'] + 'doc8'),
    'git-manual': ("Git manual", url['git-scm'] + 'docs/user-manual.html'),
    'git-download': ("Git download", url['git-scm'] + 'downloads'),
    'git-book': ("Git book", url['git-scm'] + 'book/en/v2'),
    'git-config': ('git-config', url['git-scm'] + 'docs/git-config'),
    'git-log': ('git-log', url['git-scm'] + 'docs/git-log'),
    'git-commit': ('git-commit', url['git-scm'] + 'docs/git-commit'),
    'git-push': ('git-push', url['git-scm'] + 'docs/git-push'),
    'git-clone': ('git-clone', url['git-scm'] + 'docs/git-clone'),
    'git-branch': ('git-branch', url['git-scm'] + 'docs/git-branch'),
    'git-tag': ('git-tag', url['git-scm'] + 'docs/git-tag'),
    'git-checkout': ('git-checkout', url['git-scm'] + 'docs/git-checkout'),
    'git-merge': ('git-merge', url['git-scm'] + 'docs/git-merge'),
    'git-setup': ("Git setup", url['git-scm'] + 'book/en/v2/Getting-Started-'
                  'First-Time-Git-Setup'),
    'git-commit-guidelines':
        ("Git commit guidelines", url['git-scm'] + 'book/en/v2/Distributed-Git'
         '-Contributing-to-a-Project#_commit_guidelines'),
    'commit-conventions':
        ("Git commit message style", url['Stack OF'] + '3580013/should-i-use'
         '-past-or-present-tense-in-git-commit-messages'),
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
    'finance-share': ('Share', url['Wiki pg'] + 'Share_(finance)'),
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
    'admonition': ('Admonition', url['docutils'] +
                   'docs/ref/rst/directives.html#admonitions'),
    'bibtex': ('BibTeX', 'http://www.bibtex.org'),
    'ISBN': ('ISBN', url['Wiki pg'] + 'International_Standard_Book_Number'),
    'bibtex-syntax': ("BibTeX Entry and Field Types", 'http://bib-it'
                      '.sourceforge.net/help/fieldsAndEntryTypes.php'),
    'cite-multiple-authors':
        ("Convention for citing multiple authors",
         'https://research.moreheadstate.edu/c.php?g=107001&p=695202'),
    'book': ('Book', url['Wiki pg'] + 'Book'),
    'sphinx-autobuild': ('sphinx-autobuild', url['pypi'] +
                         'project/sphinx-autobuild/'),
    'internet': ('Internet', url['Wiki pg'] + 'Internet'),
    'website': ('Website', url['Wiki pg'] + 'Website'),
    'web-browser': ("Web browser", url['Wiki pg'] + 'Web_browser'),
    'webpage': ("Webpage", url['Wiki pg'] + 'Web_page'),
    'URL': ("Uniform Resource Locator (URL)", url['Wiki pg'] + 'URL'),
    'citation': ('Citation', url['Wiki pg'] + 'Citation'),
    'command-line': ("Command line", url['Wiki pg'] +
                     'Command-line_interface'),
    'msfc-lab':
    ("NASA Marshall Space Flight Center Flight Robotics Laboratory",
     'https://archive.org/details/NASAMarshallTV-yrt04t5ZYDo'),
    'caye-caulker': ("Caye Caulker", url['Wiki pg'] + 'Caye_Caulker'),
    'mvp-development': ("Minimum Viable Prototype (MVP)",
                        url['Wiki pg'] + 'Minimum_viable_product'),
    'torvalds-interview': ('Linus Torvalds interview', url['YT vid'] +
                           'o8NPllzkFhE'),
    'why-poignant-guide': ("_why's (Poignant) Guide to Ruby, Chapter 3",
                           'https://poignant.guide/book/chapter-3.html'),
    'schafer-interview': ("Corey Schafer interview from RealPython",
                          url['RealPython'] + 'interview-corey-schafer/'),
    'computer': ('Computer', url['Wiki pg'] + 'Computer'),
    'mobile-device': ("Mobile device", url['Wiki pg'] + 'Mobile_device'),
    'source-code': ("Source code", url['Wiki pg'] + 'Source_code'),
    'copy-paste': ("Cut, copy, and paste", url['Wiki pg'] +
                   'Cut,_copy,_and_paste'),
    'software': ('Software', url['Wiki pg'] + 'Software'),
    'string': ('String', url['Wiki pg'] + 'String_(computer_science)'),
    # New links below, sorted links above
    'stack-overflow': ("Stack Overflow", url['Stack OF']),
}
