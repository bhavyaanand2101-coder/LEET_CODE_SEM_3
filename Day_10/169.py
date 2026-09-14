"""
LeetCode 169: Majority Element

Question:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Given:
- nums: List[int] (an array of integers)
- Constraints:
    - n == nums.length
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9
    - The input is generated such that a majority element will exist in the array.

Output:
- int: The majority element that appears more than ⌊n / 2⌋ times.

Examples:
- Example 1:
    Input: nums = [3, 2, 3]
    Output: 3

- Example 2:
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Follow-up:
Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm: O(n) time, O(1) space
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
            
        return candidate


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [3, 2, 3],
            "expected": 3,
        },
        {
            "nums": [2, 2, 1, 1, 1, 2, 2],
            "expected": 2,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        expected_output = test["expected"]
        actual_output = solution.majorityElement(given_nums)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")

# class Solution {
# public int majorityElement(int[] nums) {
    # HashMap<Integer, Integer> map = new HashMap<>();
    # for (int num : nums) {
    #     map.put(num, map.getOrDefault(num, 0) + 1);
    # }
    # for (int num : map.keySet()) {
    #     if (map.get(num) > nums.length / 2) {
    #         return num;
    #     }
    # }
    # return -1;  
# }