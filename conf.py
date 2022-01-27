# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- sys.path preparation ----------------------------------------------------
#

import os
import sys
import datetime
sys.path.insert(0, os.path.abspath("."))


#
# -- Project information ------------------------------------------------------
#

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

project = 'Documentation System'
full_title = project
copyright = f"{datetime.date.today().year} Divio Technologies AB"
author = "Divio"
version = "1.0"
release = version

#
# -- General configuration ----------------------------------------------------
#

extensions = []

#
# -- Options for the theme ----------------------------------------------------
#

html_theme = "furo"
html_theme_options = {
    "show_cloud_banner": True,
    "cloud_banner_markup": """
        <div class="divio-cloud">
            <span class="divio-cloud-caption">Cloud deployment by Divio</span>
            <iframe src="https://player.vimeo.com/video/435660924" width="226" height="141" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
            <p>There's a better, faster, easier way to develop, deploy and manage web applications.</p>
            <a class="btn-neutral divio-cloud-btn" target="_blank" href="https://www.divio.com">Find out more at Divio</a>
        </div>
    """,
    "segment_id": "f5RRB4OHVUYHtvdKL0Q1KdrZnAYx4jwU",
    "style_external_links": True,
    "navigation_depth": 2,
    "sidebar_hide_name": True,
}

#
# -- Options for HTML output --------------------------------------------------
#

html_title = full_title
html_help_basename = "DivioDocumentationSystem"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
    "styles/furo.css",
]

#
# -- Options for Sphinx -------------------------------------------------------
#

source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = ["README.rst", "_build", "Thumbs.db", ".DS_Store", "env"]
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

#
# -- Options for latex output -------------------------------------------------
#

latex_documents = [
    (master_doc, html_help_basename + ".tex", full_title, author, "manual"),
]

#
# -- Options for manual page output -------------------------------------------
#

man_pages = [
    (master_doc, html_help_basename, full_title, [author], 1)
]
