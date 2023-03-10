# -- Project information -----------------------------------------------------

project = "Executable Book Team Compass"
copyright = "2022"
author = "Executable Book Community"

main_doc = "index"

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser", "sphinx_design", "sphinx.ext.intersphinx"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# MyST Configuration
myst_enable_extensions = ["colon_fence", "linkify"]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/logo-square.png"
html_title = ""
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/team-compass",
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_source_button": True,
    "path_to_docs": "docs",
    "icon_links": [{
        "url": "https://github.com/executablebooks/team-compass",
        "icon": "fa-brands fa-github",
    
    },{
        "url": "https://executablebooks.org",
        "icon": "_static/logo-square.png",
        "type": "local",
    
    }]
}

# Intersphinx
intersphinx_mapping = {
    "jb": ("https://jupyterbook.org/en/latest", None),
    "meta": ("https://executablebooks.org/en/latest/", None),
    "meps": ("https://mep.myst-tools.org/en/latest/", None),
}

# -- Extra scripts at build time ---------------------------------------------

from pathlib import Path
from sphinx.application import Sphinx
import os
from sphinx.util import logging
import requests

LOGGER = logging.getLogger("conf")

# Functions that this calls are below
def setup(app: Sphinx):
    app.connect("builder-inited", update_contributing)
    app.add_crossref_type("team", "team")

def update_contributing(app: Sphinx):
    """Downloads the latest version of the contributing guide."""
    path_contributing = Path(app.srcdir) / "development/conventions.txt"
    if path_contributing.exists():
        LOGGER.info("Contributing page exists, delete and re-build to update...")
        return
    LOGGER.info("Updating conventions page...")
    # Grab the latest contributing docs
    url_contributing = "https://raw.githubusercontent.com/executablebooks/.github/master/CONTRIBUTING.md"
    resp = requests.get(url_contributing, allow_redirects=True)
    path_contributing.write_bytes(resp.content)
