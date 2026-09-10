"""
LeetCode 1: Two Sum

Question:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use
the same element twice. You can return the answer in any order.

Given:
- nums: List[int] (an array of integers)
- target: int
- Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Output:
- List[int]: [index1, index2] (indices of the two numbers that add up to target).

Examples:
- Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

- Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]
    Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].

- Example 3:
    Input: nums = [3, 3], target = 6
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].

Follow-up:
Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map approach: O(n) time, O(n) space
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            
        return []


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1],
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        given_target = test["target"]
        expected_output = test["expected"]
        actual_output = solution.twoSum(given_nums, given_target)
        
        # LeetCode accepts answer in any order
        is_pass = sorted(actual_output) == sorted(expected_output)
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}, target = {given_target}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
