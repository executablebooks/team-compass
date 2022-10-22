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
html_title = None
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/team-compass",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
}

# Intersphinx
intersphinx_mapping = {
    "jb": ("https://jupyterbook.org/en/latest", None),
    "meta": ("https://executablebooks.org/en/latest/", None),
}
