#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Box documentation build configuration file, created by
# sphinx-quickstart on Fri Apr 21 22:26:16 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
import shutil

project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.insert(0, project_root)

readme_file = os.path.join(project_root, "README.rst")
changes_file = os.path.join(project_root, "CHANGES.rst")
changes_4_file = os.path.join(project_root, "docs", "4.x_changes.rst")

shutil.copy(readme_file, "index.rst")

with open("index.rst", "r+") as index:
    modified = index.readlines()
    index.seek(0)
    index.write(''.join([x for x in modified if not x.startswith('Box 4 is out')]))


with open("index.rst", "a") as index, open(changes_file) as changes, open(changes_4_file) as change_4:
    index.write('\n')
    index.write(changes.read())
    index.write('\n')
    index.write(change_4.read())

with open(os.path.join(project_root, "box", "__init__.py"), "r") as init_file:
    init_content = init_file.read()

attrs = dict(re.findall(r"__([a-z]+)__ *= *['\"](.+)['\"]", init_content))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Box'
copyright = '2017-2020, Chris Griffith'
author = 'Chris Griffith'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = attrs['version']
# The full version, including alpha/beta/rc tags.
release = attrs['version']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `to do` and `to do List` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'github_fork': 'cdgriffith/Box',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Boxdoc'

# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'Box.tex', 'Box Documentation',
     'Chris Griffith', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'box', 'Box Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Box', 'Box Documentation',
     author, 'Box', 'One line description of project.',
     'Miscellaneous'),
]
