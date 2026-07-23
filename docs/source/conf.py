# Configuration file for the Sphinx documentation builder.

from pathlib import Path, PurePosixPath
from posixpath import relpath


# -- Project information
project = 'KINESIS CTP Lab'
copyright = '2025, NYU Abu Dhabi'
author = 'NYU Abu Dhabi'

release = '1.0'
version = '1.0.0'

# The canonical repository includes protected content by default. The public exporter removes
# every protected RST block before building the sanitized public source tree.
tags.add('internal')

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid',
    'sphinx_reredirects',
]


def _moved_section_redirects():
    """Preserve page URLs after top-level source sections are renumbered."""
    source_root = Path(__file__).parent
    section_moves = {
        '4-facilities': '2-facilities',
        '2-equipment': '3-equipment',
        '3-computing': '4-computing',
    }
    result = {}

    for old_section, new_section in section_moves.items():
        for source_path in (source_root / new_section).rglob('*.rst'):
            relative_doc = source_path.relative_to(source_root / new_section).with_suffix('')
            relative_docname = relative_doc.as_posix()
            old_docname = f'{old_section}/{relative_docname}'
            new_docname = f'{new_section}/{relative_docname}.html'
            old_parent = PurePosixPath(old_docname).parent.as_posix()
            result[old_docname] = relpath(new_docname, start=old_parent)

    return result


redirects = _moved_section_redirects()


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

# The internal wiki links contributors to the canonical private source repository. The public
# exporter disables this control because the generated public repository is not an editing source.
html_context = {
    'display_github': False,
    'github_user': 'KinesisCTP',
    'github_repo': 'rtd-kinesis-internal',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path = ['_static']

html_css_files = [
    'custom.css',
    'sidebar-contrast.css',
    'homepage-hero-v5.css',
    'native-responsive-nav-v4.css',
    'lab-overview-polish-v1.css',
]

html_js_files = [
    'custom.js',
]
