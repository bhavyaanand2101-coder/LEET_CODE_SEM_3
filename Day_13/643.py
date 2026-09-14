"""
LeetCode 643: Maximum Average Subarray I

Question:
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Given:
- nums: List[int] (an integer array)
- k: int (length of the contiguous subarray)
- Constraints:
    - n == nums.length
    - 1 <= k <= n <= 10^5
    - -10^4 <= nums[i] <= 10^4

Output:
- float: The maximum average value of a contiguous subarray of length k.

Examples:
- Example 1:
    Input: nums = [1, 12, -5, -6, 50, 3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

- Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Fixed-size Sliding Window approach: O(n) time, O(1) space
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum / k


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 12, -5, -6, 50, 3],
            "k": 4,
            "expected": 12.75000,
        },
        {
            "nums": [5],
            "k": 1,
            "expected": 5.00000,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        given_k = test["k"]
        expected_output = test["expected"]
        actual_output = solution.findMaxAverage(given_nums, given_k)
        
        is_pass = abs(actual_output - expected_output) < 1e-5
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}, k = {given_k}")
        print(f"Expected Output:  {expected_output:.5f}")
        print(f"Actual Output:    {actual_output:.5f}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
