"""
LeetCode 704: Binary Search

Question:
Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Given:
- nums: List[int] (integer array sorted in ascending order with unique values)
- target: int (integer to search for)
- Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All the integers in nums are unique.
    - nums is sorted in ascending order.

Output:
- int: The index of target in nums, or -1 if target is not in nums.

Examples:
- Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

- Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Classic Binary Search:
        Since the array is sorted in ascending order, compare target with the middle element:
        - If nums[mid] == target, return mid.
        - If nums[mid] < target, target must be in the right half: left = mid + 1.
        - If nums[mid] > target, target must be in the left half: right = mid - 1.

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

        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [-1, 0, 3, 5, 9, 12],
            "target": 9,
            "expected": 4,
        },
        {
            "nums": [-1, 0, 3, 5, 9, 12],
            "target": 2,
            "expected": -1,
        },
        {
            "nums": [5],
            "target": 5,
            "expected": 0,
        },
        {
            "nums": [5],
            "target": -5,
            "expected": -1,
        },
        {
            "nums": [2, 5],
            "target": 2,
            "expected": 0,
        },
        {
            "nums": [2, 5],
            "target": 5,
            "expected": 1,
        },
        {
            "nums": [1, 3, 5, 7, 9, 11],
            "target": 1,
            "expected": 0,
        },
        {
            "nums": [1, 3, 5, 7, 9, 11],
            "target": 11,
            "expected": 5,
        },
    ]

    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        given_target = test["target"]
        expected_output = test["expected"]
        actual_output = solution.search(given_nums, given_target)

        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}, target = {given_target}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
