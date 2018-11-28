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
sys.path.insert(0, os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'AAAAAA'
copyright = '2018, alnoki'
author = 'alnoki'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


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
    'xref'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
    'navigation_depth': -1,  # Allows unlimited depth of tree
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

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
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Base urls used by xrefs extension
url = {
    'GitHub': 'https://github.com/',
    'YT vid': 'https://www.youtube.com/watch?v=',  # Video
    'YT PL': 'https://www.youtube.com/playlist?list=PL',  # Playlist
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
    'codebasics-pytest-vids':
        ("codebasics YouTube playlist: Pytest Tutorial (Python Automated "
         "Testing)", url['YT PL'] + 'eo1K3hjS3utzQYDNRNluzqJqpMXx6hHu'),
    # New links below, sorted links above
    }
