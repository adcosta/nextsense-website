# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'neXtSense P13'
copyright = '2026, neXtSense P13 Project Team'
author = 'António Costa, Maria João Nicolau'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = "pydata_sphinx_theme"
html_theme = "furo"
html_title = "neXtSense P13 Project"

html_theme_options = {
    "navigation_with_keys": True,
    "sidebar_hide_name": False,
    "top_of_page_buttons": ["view"],
    "source_repository": "",
    "footer_icons": [
        {
            "name": "Co-financed-by",
            "url": "",
            "html": '<img src="_static/page_footer.png">',
            "class": "footer-img",
        },
        {
            "name": "Partner-Institutions",
            "url": "",
            "html": '<img src="_static/page_header.png">',
            "class": "footer-img",
        }
    ]
}

html_theme_options.update({
    "light_css_variables": {
        "font-stack": "Georgia, serif",
        "font-size": "17px",
        "line-height": "1.6",
    }
})

templates_path = ["_templates"]
html_static_path = ["_static"]
html_favicon = "_static/icon.png"
html_logo = "_static/icon.png"
html_css_files = ["custom.css"]

