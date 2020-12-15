# -*- coding: utf-8 -*-
import numpy as np
from numpy.random import default_rng

__all__ = ["johnson_min_dim", "GaussianRandomProjection"]

import logging
logger = logging.getLogger(__name__)

class GaussianRandomProjection:
    def __init__(self, n_components='auto', eps=0.1, random_generator=None):
        self.n_components_in =  n_components
        self.eps = eps
        self.random_generator = random_generator

    def fit(self, X, y=None):
        """Fit generates the gaussian projection matrix.

        Parameters
        ----------
        X : numpy array
            Should include training set, only the shape of it is used to
            determine optimial size of projection matrix.

        y : ignored
            Here to keep compatibility with scikit Transform

        Returns
        -------
        self

        """
        n_samples, n_features = X.shape

        if self.n_components_in == 'auto':
            self.n_components = johnson_min_dim(samples = n_samples, eps = self.eps)
        else:
            self.n_components = self.n_components_in

        if self.n_components > n_features:
            logger.warning("number of components (%r) greater than number of features (%r)"
                        % (self.n_components, n_features))

        self.components = _random_gaussian_matrix(self.n_components, n_features,
                                                  random_generator = self.random_generator)

        return self

    def transform(self, X):
        """transofrm projects data by using the random projection matrix.
        
        Parameters
        ----------
        X : numpy array [n_samples, n_features]
            Data to be projected

        Returns
        -------
        X2 : numpy array [n_samples, n_components]
            Projected data

        """
        if not hasattr(self, "components"):
            raise AttributeError("model is not fitted")

        return X @ (self.components.T)



def johnson_min_dim(samples, eps=0.1):
    """
    johnson_min_dim estimates 'correct' number of dimensions given number of
    samples can be projected into while distorting the distance between
    any two samples only by factor of (1 +- eps) with high probabilty.

    Parameters
    ----------
    samples : int greater than 0
        The number of samples.

    eps : float in (0, 1) range, optinal (default=0.1)
        Range of maximum distorition.

    Examples
    --------
    >>> johnson_min_dim(1e7, eps=0.4)
    1098
    """
    if eps <= 0.0 or eps >= 1:
        raise ValueError("eps has to be within (0, 1) exclusive, got %r" % eps)

    if samples <= 0:
        raise ValueError("samples has to be greater than 0, got %r" % samples)
    
    return (4 * np.log(samples) / ((eps ** 2 / 2) - (eps ** 3 / 3))).astype(np.int)

def _random_gaussian_matrix(n_components, n_features, random_generator=None):
    rng = default_rng(random_generator)
    return rng.normal(loc=0.0,
                      scale = 1.0/ np.sqrt(n_components),
                      size = (n_components, n_features))
