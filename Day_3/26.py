"""
LeetCode 26: Remove Duplicates from Sorted Array

Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the
elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates,
return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.

Custom Judge:
The judge will test your solution with the following code:
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

Given:
- nums: List[int] (an array of integers sorted in non-decreasing order)
- Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.

Output:
- int: k (the number of unique elements in nums)
- In-place modification: nums[:k] contains the unique elements in sorted order.

Examples:
- Example 1:
    Input: nums = [1, 1, 2]
    Output: 2, nums = [1, 2, _]
    Explanation:
        Your function should return k = 2, with the first two elements of nums
        being 1 and 2 respectively. It does not matter what you leave beyond
        the returned k (hence they are underscores).

- Example 2:
    Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
    Explanation:
        Your function should return k = 5, with the first five elements of nums
        being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave
        beyond the returned k (hence they are underscores).
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        insert_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_idx] = nums[i]
                insert_idx += 1
                
        return insert_idx


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 1, 2],
            "expected_k": 2,
            "expected_nums": [1, 2],
        },
        {
            "nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            "expected_k": 5,
            "expected_nums": [0, 1, 2, 3, 4],
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        original_nums = list(test["nums"])
        nums = list(test["nums"])
        expected_k = test["expected_k"]
        expected_nums = test["expected_nums"]
        
        actual_k = solution.removeDuplicates(nums)
        actual_unique = nums[:actual_k]
        
        is_pass = (actual_k == expected_k) and (actual_unique == expected_nums)
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {original_nums}")
        print(f"Expected Output:  k = {expected_k}, nums = {expected_nums}")
        print(f"Actual Output:    k = {actual_k}, nums = {actual_unique}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
