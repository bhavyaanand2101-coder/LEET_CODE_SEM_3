"""
LeetCode 33: Search in Rotated Sorted Array

Question:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown
index k (1 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

Given the array nums after the possible rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Given:
- nums: List[int] (integer array sorted in ascending order with distinct values, possibly rotated)
- target: int (integer to search for)
- Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values of nums are unique.
    - nums is an ascending array that is possibly rotated.
    - -10^4 <= target <= 10^4

Output:
- int: The index of target in nums, or -1 if target is not in nums.

Examples:
- Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

- Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

- Example 3:
    Input: nums = [1], target = 0
    Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified Binary Search:
        In a rotated sorted array, splitting the array at the midpoint always results
        in at least one sorted half. We identify which half is sorted, check if the
        target lies within the boundaries of that sorted half, and adjust our search
        range accordingly.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
            "expected": 4,
        },
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
            "expected": -1,
        },
        {
            "nums": [1],
            "target": 0,
            "expected": -1,
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 0,
        },
        {
            "nums": [3, 1],
            "target": 1,
            "expected": 1,
        },
        {
            "nums": [5, 1, 3],
            "target": 5,
            "expected": 0,
        },
        {
            "nums": [4, 5, 6, 7, 8, 1, 2, 3],
            "target": 8,
            "expected": 4,
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
