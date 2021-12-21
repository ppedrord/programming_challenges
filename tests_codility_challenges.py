"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Codility - Iteration Lessions 1 - Binary Gap


"""


import pytest
import codility_challenges

binary = [(1, 0),
          (2, 0),
          (147, 2),
          (483, 3),
          (647, 4)]
@pytest.mark.parametrize(["N", "expected"], binary)
def test_example_add(N, expected):
    assert codility_challenges.binary_gap(N) == expected
