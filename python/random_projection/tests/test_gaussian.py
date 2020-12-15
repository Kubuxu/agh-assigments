# -*- coding: utf-8 -*-

import numpy as np
import pytest
from random_projection import johnson_min_dim, GaussianRandomProjection

__author__ = "Jakub Sztandera"
__copyright__ = "Jakub Sztandera"
__license__ = "mit"


def test_johnson_min_dim():
    # test simple usage
    assert johnson_min_dim(1e7, eps=0.4) == 1098

def test_johnson_min_dim_bounds():
    for eps in [-2, -2.0, -1, -1.0, -0.0, 0.0, 0, 1.0, 1, 1.1, 2, 2.0]:
        with pytest.raises(ValueError):
            johnson_min_dim(1e7, eps=eps)

    for samples in [-100, -1, 0]:
        with pytest.raises(ValueError):
            johnson_min_dim(samples)

from random_projection.gaussian import _random_gaussian_matrix

def test_random_gaussian_matrix():
    # _random_gaussian_matrix() produces matrix of correct dimensions
    M = _random_gaussian_matrix(10, 20)
    assert M.shape == (10, 20)

    # each time the matrix is different
    M2 = _random_gaussian_matrix(10, 20)
    assert (M != M2).any()

    # we can use it with fixed seed

    M = _random_gaussian_matrix(10, 20, random_generator=42)
    M2 = _random_gaussian_matrix(10, 20, random_generator=42)
    assert (M == M2).all()


from numpy.random import default_rng
from sklearn.metrics.pairwise import euclidean_distances


def test_GaussianRandomProjection():
    rng = default_rng(42)
    X = rng.choice([0, 1], size=(10, 1000))
    eps = 0.2

    for grp in [GaussianRandomProjection(eps=eps),
                GaussianRandomProjection(n_components = 550, eps=eps),
                GaussianRandomProjection(n_components = 1100, eps=eps)]:
        grp.fit(X)
        Xnew = grp.transform(X)

        # collect distances between all vectors in X
        org_dist = euclidean_distances(X, squared = True)
        # exclude distances between the point and itself
        non_self = np.eye(*org_dist.shape) == 0
        org_dist = org_dist[non_self]

        new_dist = euclidean_distances(Xnew, squared = True)
        new_dist = new_dist[non_self]
        ratios = new_dist / org_dist

        # verify that johnson lemma was held
        assert (ratios < 1 + eps).all()
        assert (ratios > 1 - eps).all()

def test_GaussianRandomProjection_transfom_without_fit():
    rng = default_rng(42)
    X = rng.choice([0, 1], size=(10, 1000))

    grp = GaussianRandomProjection()
    with pytest.raises(AttributeError):
        grp.transform(X)

