"""
LeetCode 238: Product of Array Except Self

Question:
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Given:
- nums: List[int] (an array of integers)
- Constraints:
    - 2 <= nums.length <= 10^5
    - -30 <= nums[i] <= 30
    - The input is generated such that answer[i] fits in a 32-bit integer.

Output:
- List[int]: An array where answer[i] is the product of all elements except nums[i].

Examples:
- Example 1:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

- Example 2:
    Input: nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

Follow up:
Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time, O(1) extra space (excluding output array)
        n = len(nums)
        answer = [1] * n
        
        # Prefix pass: answer[i] contains the product of all elements to the left
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Suffix pass: multiply with the product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6],
        },
        {
            "nums": [-1, 1, 0, -3, 3],
            "expected": [0, 0, 9, 0, 0],
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.productExceptSelf(given_nums)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
