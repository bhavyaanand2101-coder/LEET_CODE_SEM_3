"""
LeetCode 3005: Count Elements With Maximum Frequency

Question:
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Given:
- nums: List[int] (an array of positive integers)
- Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100

Output:
- int: The total frequencies of elements in nums with the maximum frequency.

Examples:
- Example 1:
    Input: nums = [1, 2, 2, 3, 1, 4]
    Output: 4
    Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
                 So the number of elements in the array with maximum frequency is 4.

- Example 2:
    Input: nums = [1, 2, 3, 4, 5]
    Output: 5
    Explanation: All elements of the array have a frequency of 1 which is the maximum.
                 So the number of elements in the array with maximum frequency is 5.
"""

from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Frequency counting approach: O(n) time, O(k) space (where k is unique elements)
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(f for f in freq.values() if f == max_freq)


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 2, 2, 3, 1, 4],
            "expected": 4,
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 5,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.maxFrequencyElements(given_nums)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
