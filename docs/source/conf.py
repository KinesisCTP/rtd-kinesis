# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import json

project = 'KINESIS CTP Lab'
copyright = '2025, NYU Abu Dhabi'
author = 'NYU Abu Dhabi'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # NYU purple sidebar header
    'style_nav_header_background': '#57068c',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Logo path relative to conf.py dir; Sphinx also copies basename into HTML _static/
html_logo = '_static/images/Core-Technology-Platforms-lockup-DIGITAL-white.png'
html_title = 'KINESIS CTP Lab'

# Edit on GitHub button
html_context = {
    'display_github': True,
    'github_user': 'KinesisCTP',
    'github_repo': 'rtd-kinesis',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
]



def setup(app):
    app.add_css_file('custom.css')
    app.add_js_file('custom.js')

    app.add_config_value('equipment_data', {}, 'env')

    here = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(here, '_static', 'data', 'equipment.json')

    with open(json_path) as f:
        app.config.equipment_data = json.load(f)
