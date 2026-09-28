"""
LeetCode 35: Search Insert Position

Question:
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Given:
- nums: List[int] (sorted array of distinct integers in ascending order)
- target: int (target value to search or insert)
- Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums contains distinct values sorted in ascending order.
    - -10^4 <= target <= 10^4

Output:
- int: The index where target is found or where it should be inserted.

Examples:
- Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

- Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

- Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary Search:
        Maintain a search interval [left, right].
        If nums[mid] == target, return mid.
        If nums[mid] < target, search right half: left = mid + 1.
        If nums[mid] > target, search left half: right = mid - 1.
        When the loop ends without finding target, left represents the insertion point.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 3, 5, 6],
            "target": 5,
            "expected": 2,
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 2,
            "expected": 1,
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 7,
            "expected": 4,
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 0,
            "expected": 0,
        },
        {
            "nums": [1],
            "target": 0,
            "expected": 0,
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 0,
        },
        {
            "nums": [1],
            "target": 2,
            "expected": 1,
        },
    ]

    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        given_target = test["target"]
        expected_output = test["expected"]
        actual_output = solution.searchInsert(given_nums, given_target)

        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}, target = {given_target}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
