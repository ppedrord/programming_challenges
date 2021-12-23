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


rotation = [([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
            ([0, 3, 5, 9], 3, [3, 5, 9, 0]),
            ([0, 0, 1], 3, [0, 0, 1]),
            ([5, 8, 7, 2, 4, 6, 9, 5], 6, [7, 2, 4, 6, 9, 5, 5, 8])]
@pytest.mark.parametrize(["A", "K", "expected"], rotation)
def test_array_rotation(A, K, expected):
    assert codility_challenges.rotation_solution(A, K) == expected