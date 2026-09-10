"""
LeetCode 347: Top K Frequent Elements

Question:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Given:
- nums: List[int] (an array of integers)
- k: int (number of top frequent elements to return)
- Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array].
    - It is guaranteed that the answer is unique.

Output:
- List[int]: The k most frequent elements in any order.

Examples:
- Example 1:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

- Example 2:
    Input: nums = [1], k = 1
    Output: [1]

- Example 3:
    Input: nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k = 2
    Output: [1, 2]

Follow up:
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort approach: O(n) time, O(n) space
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Group elements by their frequency
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Traverse buckets from highest frequency to lowest
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1],
        },
        {
            "nums": [1, 2, 1, 2, 1, 2, 3, 1, 3, 2],
            "k": 2,
            "expected": [1, 2],
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_nums = test["nums"]
        given_k = test["k"]
        expected_output = test["expected"]
        actual_output = solution.topKFrequent(given_nums, given_k)
        
        # LeetCode accepts answer in any order
        is_pass = sorted(actual_output) == sorted(expected_output)
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    nums = {given_nums}, k = {given_k}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
