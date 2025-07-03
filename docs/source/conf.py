# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../')) 

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MagiAttention1'
copyright = '2025, Sandai'
author = 'Sandai'
release = 'v1.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    "sphinx.ext.autosummary",
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    "myst_parser",
    # "sphinx_copybutton",
    # "sphinx.ext.autosectionlabel",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

autodoc_default_options = {
    'members': None,          # 包含所有成员
    'inherited-members': None,  # 包含继承的成员
    'show-inheritance': True,  # 显示继承关系
    'imported-members': False,  # 不包含导入的成员
    'special-members': False,  # 不包含特殊成员（如 __init__）
    'exclude-members': '__weakref__,__dict__,__module__',  # 排除特定成员
    'private-members': False,  # 不包含私有成员（以下划线开头）
    'member-order': 'bysource',  # 按源代码顺序排列
    'undoc-members': False,  # 不包含没有文档字符串的成员
}

# 只包含 __all__ 中定义的成员
autodoc_default_flags = ['members', 'special-members']

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# import pytorch_sphinx_theme2

# html_theme = 'pydata_sphinx_theme'
html_theme = 'furo'
# html_theme = 'classic'
# html_theme_path = [pytorch_sphinx_theme2.get_html_theme_path()]
html_static_path = ['_static']
html_baseurl = "https://wt1w.github.io/test_sphinx/blog1/"
