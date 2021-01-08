import os
import sys
import sphinx_rtd_theme

sys.path.append(os.path.abspath('..'))

from catalyst_sphinx_theme import __version__
# sys.path.append(os.path.join(os.environ["SAMPLE_DOCS_LOCATION"], "demo"))
# print("", sys.path[-1], "", sep="\n" + "-" * 80 + "\n")

# -- Project information -----------------------------------------------------

project = "Coding Chess Variants Docs"
copyright = "2020, Coding Chess Variants"
author = "Alex Liu, Isabel Li, Jimin Park, Kerry Xu, Radostein Petrov, Seiya Aoki"

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    'sphinxcontrib.httpdomain',
    "sphinx_rtd_theme"
]

# -- Options for HTML output -------------------------------------------------

html_title = project

# NOTE: All the lines are after this are the theme-specific ones. These are
#       written as part of the site generation pipeline for this project.
# !! MARKER !!

html_theme = "catalyst_sphinx_theme"

html_static_path = ['_static']