from numpy.random import default_rng
rng = default_rng()
X = rng.choice([0, 1], size=(100, 5000))
import random_projection
eps = 0.2
grp = random_projection.GaussianRandomProjection(eps=eps)
grp.fit(X)
Xnew = grp.transform(X)

from sklearn.metrics.pairwise import euclidean_distances
org_dist = euclidean_distances(X).ravel()
non_zero = org_dist != 0
org_dist = org_dist[non_zero]

new_dist = euclidean_distances(Xnew).ravel()
new_dist = new_dist[non_zero]
ratios = new_dist / org_dist
