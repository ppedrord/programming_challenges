"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

LeetCode Challenges

"""

from typing import List


class Solution:
    """
    1. Two Sum (Easy)

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]


    Constraints:
        1. 2 <= nums.length <= 104
        2. -109 <= nums[i] <= 109
        3. -109 <= target <= 109
        4. Only one valid answer exists.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            A function to return the indices of the two numbers that when added the result is the target.

        :param nums: A list of numbers to be analyzed
        :param target: An integer representing the target value

        :returns: A list of integers representing the indices of the numbers that when added the result in the target
        """
        print("\n## -- TWO SUM -- ##")
        hash_table = {}
        n = len(nums)

        for i in range(n):
            hash_table[nums[i]] = i

        print(f"Hash table: {hash_table}")

        result_list = []
        for index in range(n):
            complement = target - nums[index]
            print(f"Calculating complement: {target} - {nums[index]} = {complement}")
            if complement in nums and index != hash_table[complement]:
                result_list = [index, hash_table[complement]]
                print(f"Result list: {result_list}")
                return result_list
        return []

    """
    2. Roman to Integer (Easy)

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Given a roman numeral, convert it to an integer.
    Example 1:
        Input: s = "III"
        Output: 3
        Explanation: III = 3.
    
    Example 2:
        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
    
    Example 3:
        Input: s = "MCMXCIV"
        Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:
        1. 1 <= s.length <= 15
        2. s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        3. It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    """

    def romanToInt(self, s: str) -> int:
        """
            A function to convert a roman numeral to an integer.

        :param s: A string representing the roman numeral

        :returns: An integer representing the roman numeral
        """
        print("\n## -- ROMAN TO INTEGER -- ##")
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        print("String s:", s)

        for index in range(len(s)):
            print("-- Analyzing index:", index)
            if (index < len(s) - 1) and (
                roman_dict[s[index]] < roman_dict[s[index + 1]]
            ):
                print(
                    f"Index {index} is less than index {index + 1} and {roman_dict[s[index]]} is less than {roman_dict[s[index + 1]]}"
                )
                print("Subtracting")
                result -= roman_dict[s[index]]
                print(f"Result: {result}")
            else:
                print("Adding")
                result += roman_dict[s[index]]
                print(f"Result: {result}")

        print("-- Result for s =", s, "is:", result)
        return result

    """
    3. Palindrome Number (Easy)

        Given an integer x, return true if x is a palindrome, and false otherwise.

        Example 1:
            Input: x = 121
            Output: true
            Explanation: 121 reads as 121 from left to right and from right to left.
        
        Example 2:
            Input: x = -121
            Output: false
            Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
        
        Example 3:
            Input: x = 10
            Output: false
            Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
        
        Constraints:
            - -231 <= x <= 231 - 1
    """

    def isPalindrome(self, x: int) -> bool:
        """
            A function to check if a number is a palindrome.

        :param x: An integer to be checked

        :returns: A boolean value representing if the number is a palindrome
        """
        print("\n## -- IS PALINDROME -- ##")
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[-(i + 1)]:
                return False

        return True

    """
    4. Maximum Subarray (Medium)

    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    Example 1:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    
    Example 2:
        Input: nums = [1]
        Output: 1
        Explanation: The subarray [1] has the largest sum 1.
    
    Example 3:
        Input: nums = [5,4,-1,7,8]
        Output: 23
        Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    
    Constraints:
        - 1 <= nums.length <= 105
        - -104 <= nums[i] <= 104
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
            A function to find the subarray with the largest sum.

        :param nums: An integer array

        :returns: An integer representing the largest sum
        """
        print("\n## -- MAXIMUM SUBARRAY -- ##")
        max_result = -99999999
        for index, value in enumerate(nums):
            sum_sub_array = value
            for inside_index, inside_value in enumerate(nums):
                sum_sub_array = sum_sub_array + inside_value if inside_index != index else inside_value 
                if sum_sub_array > max_result:
                    max_result = sum_sub_array
                else:
                    continue 
        return max_result




if __name__ == "__main__":
    s = Solution()
    two_sum_test = s.twoSum([2, 7, 11, 15], 9)
    print(two_sum_test)

    roman_to_int_test = s.romanToInt("MCMXCIV")
    print(roman_to_int_test)

    is_palindrome_test = s.isPalindrome(0)
    print(is_palindrome_test)

    max_sub_array_test = s.maxSubArray([5,4,-1,7,8])
    print(max_sub_array_test)
