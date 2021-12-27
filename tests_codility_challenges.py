"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Codility Challenges - Tests

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


odds = [([1, 6, 5, 1, 5, 7, 6], 7),
        ([0, 2, 5, 2, 5, 9, 0], 9),
        ([0, 0, 0, 0, 1], 1),
        ([98, 56, 78, 1001, 56, 1001, 78], 98)]
@pytest.mark.parametrize(["A", "expected"], odds)
def test_odd_occurrency(A, expected):
    assert codility_challenges.solution_odd_occurrency(A) == expected


jump = [(10, 85, 30, 3),
        (1, 75, 1, 74),
        (1, 1, 1, 0),
        (1065, 98546, 23, 4239)]
@pytest.mark.parametrize(["X", "Y", "D", "expected"], jump)
def test_frog_jump(X, Y, D, expected):
    assert codility_challenges.solution_frog_jump(X, Y, D) == expected


miss = [([1, 3, 4, 8, 6, 1, 7, 9, 10, 5, 5, 10, 20, 19, 18, 17, 16, 15, 16, 17, 14, 13, 12, 11], 2),
        ([8, 4, 6, 7, 10, 15, 5, 12, 14, 13], 11),
        ([50, 47, 46, 48, 45], 49)]
@pytest.mark.parametrize(["A", "expected"], miss)
def test_missing_element(A, expected):
    assert codility_challenges.solution_missing_element(A) == expected
