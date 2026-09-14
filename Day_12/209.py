"""
LeetCode 209: Minimum Size Subarray Sum

Question:
Given an array of positive integers nums and a positive integer target, return the minimal 
length of a subarray whose sum is greater than or equal to target. If there is no such 
subarray, return 0 instead.

Given:
- target: int (positive integer target sum)
- nums: List[int] (array of positive integers)
- Constraints:
    - 1 <= target <= 10^9
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^4

Output:
- int: Minimal length of a contiguous subarray whose sum is >= target, or 0 if none exists.

Examples:
- Example 1:
    Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    Output: 2
    Explanation: The subarray [4, 3] has the minimal length under the problem constraint.

- Example 2:
    Input: target = 4, nums = [1, 4, 4]
    Output: 1

- Example 3:
    Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
    Output: 0

Follow-up:
If you have figured out the O(n) solution, try coding another solution of which the 
time complexity is O(n log(n)).
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window approach: O(n) time, O(1) space
        left = 0
        current_sum = 0
        min_length = float("inf")
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left as long as the sum is >= target
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "target": 7,
            "nums": [2, 3, 1, 2, 4, 3],
            "expected": 2,
        },
        {
            "target": 4,
            "nums": [1, 4, 4],
            "expected": 1,
        },
        {
            "target": 11,
            "nums": [1, 1, 1, 1, 1, 1, 1, 1],
            "expected": 0,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_target = test["target"]
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.minSubArrayLen(given_target, given_nums)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    target = {given_target}, nums = {given_nums}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
