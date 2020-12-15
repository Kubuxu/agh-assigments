# -*- coding: utf-8 -*-

import pytest
from random_projection.skeleton import fib

__author__ = "Jakub Sztandera"
__copyright__ = "Jakub Sztandera"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
