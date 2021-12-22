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
def test_binary_gap(N, expected):
    assert codility_challenges.binary_gap(N) == expected



reverse = [([1,1,0,1,1,0,0,1,0], 3),
           ([1,1,1,0,1,0,0,0,1,0,1], 2),
           ([0,0,0,0,0,0,1], 3),
           ([1,0,1], 0),
           ([0,1,0], 0)]
@pytest.mark.parametrize(["A", "expected"], reverse)
def test_array(A, expected):
    assert codility_challenges.solution(A) == expected
