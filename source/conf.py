import os
import sys

sys.path.append(os.path.join(os.environ["SAMPLE_DOCS_LOCATION"], "demo"))
print("", sys.path[-1], "", sep="\n" + "-" * 80 + "\n")

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
]

# -- Options for HTML output -------------------------------------------------

html_title = project

# NOTE: All the lines are after this are the theme-specific ones. These are
#       written as part of the site generation pipeline for this project.
# !! MARKER !!
html_theme = "catalyst_sphinx_theme"
