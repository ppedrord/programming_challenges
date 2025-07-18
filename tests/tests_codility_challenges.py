"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Programming Challenges - Tests

"""

import pytest
from challenges.codility import codility_challenges

binary = [(1, 0),
          (2, 0),
          (147, 2),
          (483, 3),
          (647, 4)]


@pytest.mark.parametrize(["N", "expected"], binary)
def test_binary_gap(N, expected):
    assert codility_challenges.binary_gap(N) == expected


reverse = [([1, 1, 0, 1, 1, 0, 0, 1, 0], 3),
           ([1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1], 2),
           ([0, 0, 0, 0, 0, 0, 1], 3),
           ([1, 0, 1], 0),
           ([0, 1, 0], 0)]


@pytest.mark.parametrize(["A", "expected"], reverse)
def test_flip_coin(A, expected):
    assert codility_challenges.solution_flip_coin(A) == expected


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


tape = [([1, 2, 3, 4, 5], 3),
        ([0, 0, 0, 0, 0, 0], 0),
        ([145, 6548, 165, 14, 0, 1651], 8523),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 16)]


@pytest.mark.parametrize(["A", "expected"], tape)
def test_tape_equilibrium(A, expected):
    assert codility_challenges.solution_tape_equilibrium(A) == expected


jump = [([1, 3, 1, 4, 2, 3, 5, 4], 5, 6),
        ([1], 1, 0),
        ([7, 8, 1, 1, 3, 5, 6, 2, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 17)]


@pytest.mark.parametrize(["A", "X", "expected"], jump)
def test_frog_river_one(A, X, expected):
    assert codility_challenges.solution_frog_river_one(A, X) == expected


perm = [([4, 1, 3, 2], 1),
        ([4, 4, 1, 3, 5, 2], 1),
        ([1, 2, 3, 4, 5, 5, 7, 8, 9], 0),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 0)]


@pytest.mark.parametrize(["A", "expected"], perm)
def test_perm_check(A, expected):
    assert codility_challenges.solution_perm_check(A) == expected


counters = [([3, 4, 4, 6, 1, 4, 4], 5, [3, 2, 2, 4, 2]),
            ([6, 4, 4, 5, 7, 2, 1, 9], 8, [2, 2, 2, 2, 2, 2, 2, 2]),
            ([1, 2, 3, 2], 3, [1, 2, 1])]


@pytest.mark.parametrize(["A", "N", "expected"], counters)
def test_solution_max_counters(A, N, expected):
    assert codility_challenges.solution_max_counters(A, N) == expected


integer = [([1, 3, 6, 4, 1, 2], 5),
           ([1, 2, 3], 4),
           ([-1, -3], 1),
           ([2, 3, 4, 5, 6, 7, 8], 1),
           ([1, 4, 5, 6, 7, 8], 2)]


@pytest.mark.parametrize(["A", "expected"], integer)
def test_missing_integer(A, expected):
    assert codility_challenges.solution_missing_integer(A) == expected


cars = [([0, 1, 0, 1, 1], 5),
        ([1, 0, 1, 1, 1, 0, 1], 5),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1], 8),
        ([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)]


@pytest.mark.parametrize(["A", "expected"], cars)
def test_passing_cars(A, expected):
    assert codility_challenges.solution_passing_cars(A) == expected


count_div = [(6, 11, 2, 3),
             (0, 0, 0, 0),
             (1, 10, 2, 5),
             (15, 10, 2, 0),
             (0, 10, 2, 6),
             (0, 10, 0, 0),
             (1.5, 3, 2, 0),
             (1, 3.5, 2, 0),
             (1, 10, 1.5, 0),
             (1, 10, -1, 0)]


@pytest.mark.parametrize(["A", "B", "K", "expected"], count_div)
def test_count_div(A, B, K, expected):
    assert codility_challenges.solution_count_div(A, B, K) == expected


gen_range = [('CAGCCTA', [2, 5, 0], [4, 5, 6], [2, 4, 1]),
             ('agttcaagt', [0, 5, 4, 2], [3, 8, 4, 3], [1, 1, 2, 4]),
             ('ACGTACGTACGTT', [0], [12], [1]),
             ('aaaaaaaaaaaaaaaaacgt', [0, 17, 18, 19], [19, 19, 19, 19], [1, 2, 3, 4])]


@pytest.mark.parametrize(["S", "P", "Q", "expected"], gen_range)
def test_genomic_range_query(S, P, Q, expected):
    assert codility_challenges.solution_genomic_range_query(S, P, Q) == expected


slice = [([4, 2, 2, 5, 1, 5, 8], 1),
         ([-10000, 6, 98, -56, 87, 95], 0),
         ([-10000, 5, 6, 7, 8, 1, -10000], 5),
         ([-10000, -5000, 9, 9, -9000, 1000], 0)]


@pytest.mark.parametrize(["A", "expected"], slice)
def test_min_avg_two_slice(A, expected):
    assert codility_challenges.solution_min_avg_two_slice(A) == expected


distinct_values = [([2, 1, 1, 2, 3, 1], 3),
                   ([], 0),
                   ([1, 2, 3], 3),
                   ([1], 1),
                   ([-1, -2, -3, -4, -5], 5),
                   ([50000, 645878, 956842, 1000000, 789456], 5),
                   ([8, 9, 5, 7, 2, 3, 1, 6, 4, 10], 10)]


@pytest.mark.parametrize(["A", "expected"], distinct_values)
def test_distinct(A, expected):
    assert codility_challenges.solution_distinct(A) == expected


triplet = [([-3, 1, 2, -2, 5, 6], 60),
           ([1, 2, 3], 6),
           ([4, 5, 6, 2, 654, 85, -100, -9875, 65, 985, 65, 6892, 13, 56, 98369], 667789760780)]


@pytest.mark.parametrize(["A", "expected"], triplet)
def test_max_product_of_three(A, expected):
    assert codility_challenges.solution_max_product_of_three(A) == expected


triangle_search = [([10, 2, 5, 1, 8, 20], 1),
                   ([], 0),
                   ([1], 0),
                   ([1, 2], 0),
                   ([-5, -5, -5], 0),
                   ([5, 8, 9, 654, 12, 7825, 123, 4, 5, 8, 5, 10, 654, 8, 5, 6, 9, 4, 8, 9, 50, 51, 53], 1)]


@pytest.mark.parametrize(["A", "expected"], triangle_search)
def test_triangle(A, expected):
    assert codility_challenges.solution_triangle(A) == expected
