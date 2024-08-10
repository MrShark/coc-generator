# noqa: INP001
"""Sphinx configuration."""

project = "coc-generator"
author = "jens persson"
copyright = f"2024, {author}"  # noqa: A001
extensions = [
    "sphinx_click",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
