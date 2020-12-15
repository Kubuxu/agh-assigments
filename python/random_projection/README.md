# random_projection

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

Add a short description here!


## LICENSE

MIT

