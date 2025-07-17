"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

LeetCode Challenges - Tests

"""

import pytest
from challenges.leetcode import leetcode_challenges


two_sum = [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])]


@pytest.mark.parametrize("nums, target, expected", two_sum)
def test_two_sum(nums, target, expected):
    assert leetcode_challenges.Solution().twoSum(nums, target) == expected


roman_to_int = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]


@pytest.mark.parametrize("s, expected", roman_to_int)
def test_roman_to_int(s, expected):
    assert leetcode_challenges.Solution().romanToInt(s) == expected


is_palindrome = [
    (121, True),
    (-121, False),
    (10, False),
    (1221, True),
    (12211221, True),
]


@pytest.mark.parametrize("x, expected", is_palindrome)
def test_is_palindrome(x, expected):
    assert leetcode_challenges.Solution().isPalindrome(x) == expected


max_sub_array = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)]


@pytest.mark.parametrize("nums, expected", max_sub_array)
def test_max_sub_array(nums, expected):
    assert leetcode_challenges.Solution().maxSubArray(nums) == expected
