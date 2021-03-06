=================
random_projection
=================

**random_projection** package implements gaussian random probjection.

Random Projection is a technique used to reduce dimenshionality of a dataset,
while a the same time preserving inter-point Euclidian distances.

The resulting dimenshionality is a function of number of samples in the dataset,
instead of the ininitial dimenshionality.
This feature makes random projection idea for datasets with very high dimenshionality.

The random projection in governed by Johnson-Lindenstrauss lemma, which states that
given some epsilon error (`0 < eps < 1`) and a set `X` of `m` points in `N` dimensions
there exists a projection `R^N -> R^M` where `M << N` while preserving relative 
distances between points with maximum `+-eps` error.
The number of dimensions `M` depend only on number of points `m`.

Example of such projection is Random Gaussian Projection which projects points
from space `R^N` to `R^M` by means of projection matrix (M, N) which elements are
sampled from Normal Distribution with standard deviation of `1/sqrt(M)`.

The `M` for targeted `eps` and given `m` can be calculated by formula:

`4 * ln(m) / ((eps^2 / 2) - (eps^3 / 3))`

or by using the :py:func:`random_projection.gaussian.johnson_min_dim`.


Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: http://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: http://sphinx-doc.org/domains.html#the-python-domain
.. _Sphinx: http://www.sphinx-doc.org/
.. _Python: http://docs.python.org/
.. _Numpy: http://docs.scipy.org/doc/numpy
.. _SciPy: http://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: http://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: http://scikit-learn.org/stable
.. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _Google style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists
