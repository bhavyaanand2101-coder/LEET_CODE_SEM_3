"""
LeetCode 53: Maximum Subarray

Question:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Given:
- nums: List[int] (an array of integers)
- Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

Output:
- int: The maximum subarray sum.

Examples:
- Example 1:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.

- Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

- Example 3:
    Input: nums = [5, 4, -1, 7, 8]
    Output: 23
    Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum 23.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm: O(n) time, O(1) space
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
        },
        {
            "nums": [1],
            "expected": 1,
        },
        {
            "nums": [5, 4, -1, 7, 8],
            "expected": 23,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.maxSubArray(given_nums)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
