# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jason Walker Resume'
author = 'Jason Walker'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'README.md']

# MyST configuration
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    'strikethrough',
    'deflist',
    'fieldlist'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_title = 'Resume'

html_static_path = ['static']

html_sidebars = {
    '**': []
}

logo_color = '23568E'

html_theme_options = {
    'logo': 'logo.png',
    'analytics_id': 'G-ZYTNS5GN7G',
    'fixed_sidebar': True,
    'extra_nav_links': {
        'jason@onetrue.name': 'mailto:jason@onetrue.name',
        'LinkedIn': 'https://www.linkedin.com/in/ungood',
        'Seattle, WA': 'https://www.spaceneedle.com/webcam',
    }
}
