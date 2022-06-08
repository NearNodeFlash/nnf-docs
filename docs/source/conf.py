#!/usr/bin/env python3
# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'Near Node Flash'
copyright = '2022, Hewlett Packard Enterprise'
author = ''

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# Couldn't get the RTD theme to work on MACOS
try:
  import sphinx_rtd_theme
  html_theme = 'sphinx_rtd_theme'
except:
  print("sphinx_rtd_theme not found")

# -- Options for EPUB output
epub_show_urls = 'footnote'
