"""
Question:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Given:
- nums: List[int] (an array of integers)
- Constraints:
    - 1 <= nums.length <= 10^4
    - -1000 <= nums[i] <= 1000

Output:
- int: The leftmost pivot index, or -1 if no such index exists.

Examples:
- Example 1:
    Input: nums = [1, 7, 3, 6, 5, 6]
    Output: 3
    Explanation:
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11

- Example 2:
    Input: nums = [1, 2, 3]
    Output: -1
    Explanation:
        There is no index that satisfies the conditions in the problem statement.

- Example 3:
    Input: nums = [2, 1, -1]
    Output: 0
    Explanation:
        Left sum = 0 (no elements to the left of index 0)
        Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {"nums": [1, 7, 3, 6, 5, 6], "expected": 3},
        {"nums": [1, 2, 3], "expected": -1},
        {"nums": [2, 1, -1], "expected": 0},
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.pivotIndex(given_nums)
        
        print(f"--- Example {i} ---")
        print(f"Given (Input): nums = {given_nums}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output:   {actual_output}")
        print(f"Status:          {'PASS' if actual_output == expected_output else 'FAIL'}\n")