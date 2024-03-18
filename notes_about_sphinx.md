# Using Sphinx

Getting Started with Sphinx (install guide and more)
https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html

Quick Start
http://www.sphinx-doc.org/en/master/usage/quickstart.html

"reStructuredText is the preferred format for technical documentation"

reStructuredText Primer
http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

reStructuredText: See also demo
https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/demo/demo.rst

reStructuredText directives (comprehensive list)
https://docutils.sourceforge.io/docs/ref/rst/directives.html

Handle images
https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure

Embed code
https://www.sphinx-doc.org/en/1.5/markup/code.html

https://pythonhosted.org/an_example_pypi_project/pkgcode.html

https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example

## Viewing the docs you create

Use the Makefile to build the docs, like so -- `make builder`

-- where *builder* is one of the supported builders, e.g. `html`, `latex` or `linkcheck`

https://www.sphinx-doc.org/en/master/usage/builders/index.html

## Themes

Sphinx theme
https://sphinx-rtd-theme.readthedocs.io/en/stable/

https://github.com/readthedocs/sphinx_rtd_theme

Configuring the theme
https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

Looked at a bunch of themes
https://sphinx-themes.org/

Picked this one
https://sphinx-rtd-theme.readthedocs.io/en/latest/

Liked one other theme more, but it had NPM/Node crap, so no.

## Run the Python dev server

`python -m http.server` (or, not in env, Mac: `python3 -m http.server`)

Then: `http://localhost:8000/docs/_build/html/`

## Build

Be in the `docs` dir

```
$ conda deactivate
$ cd /Users/username/Documents/python/the_sphinx_dir
$ source env/bin/activate
$ cd docs
$ make html
```

## Check the build

Go here and log in to see why it failed: 
https://readthedocs.org/dashboard/


## Create new page/chapter in docs

1. Create a new .rst file in /docs/ e.g. `foobar.rst`

2. In `index.rst`, add filename (case-sensitive) to any tree --

```
.. toctree::
   :maxdepth: 2
   :caption: Contents

   foobar
```

`:caption: Contents` is a subheading; can have more than one list here

## Sphinx tutorials

https://buildmedia.readthedocs.org/media/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf

https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b

## Scannable Sphinx documentation

https://pythonhosted.org/an_example_pypi_project/sphinx.html

.
