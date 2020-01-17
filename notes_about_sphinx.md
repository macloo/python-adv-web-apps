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

Sphinx theme
https://sphinx-rtd-theme.readthedocs.io/en/stable/
https://github.com/readthedocs/sphinx_rtd_theme

Configuring the Theme
https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

## Viewing the docs you create

Use the Makefile to build the docs, like so -- `make builder`

-- where *builder* is one of the supported builders, e.g. html, latex or linkcheck

## Themes

Looked at a bunch of themes
https://sphinx-themes.org/

Picked this one
https://sphinx-rtd-theme.readthedocs.io/en/latest/

Liked one other theme but it had NPM/Node crap, so no.

## Run the Server

`python -m http.server` (or, not in env, Mac: `python3 -m http.server`)

Then: `localhost:8000`

## Build

```
$ conda deactivate
$ cd /Users/mcadams/Documents/python/the_sphinx_dir
$ source env/bin/activate
$ cd docs
$ make html
```

## Create New Page/Chapter

Create a new .rst file in /docs/ e.g. `foobar.rst`
In `index.rst`, add filename (case-sensitive) to any tree --

```
.. toctree::
   :maxdepth: 2
   :caption: Contents

   foobar
```


## Sphinx Tutorials

https://buildmedia.readthedocs.org/media/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf

https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b

## Scannable Documentation

https://pythonhosted.org/an_example_pypi_project/sphinx.html

.
