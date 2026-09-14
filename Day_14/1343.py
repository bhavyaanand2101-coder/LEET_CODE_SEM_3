"""
LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Question:
Given an array of integers arr and two integers k and threshold, return the number of 
sub-arrays of size k and average greater than or equal to threshold.

Given:
- arr: List[int] (an array of integers)
- k: int (size of the sub-array)
- threshold: int (the threshold average)
- Constraints:
    - 1 <= arr.length <= 10^5
    - 1 <= arr[i] <= 10^4
    - 1 <= k <= arr.length
    - 0 <= threshold <= 10^4

Output:
- int: Number of sub-arrays of size k with average >= threshold.

Examples:
- Example 1:
    Input: arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
    Output: 3
    Explanation: Sub-arrays [2, 5, 5], [5, 5, 5] and [5, 5, 8] have averages 4, 5 and 6 respectively. 
                 All other sub-arrays of size 3 have averages less than 4 (the threshold).

- Example 2:
    Input: arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5
    Output: 6
    Explanation: The first 6 sub-arrays of size 3 have averages greater than 5.
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Fixed-size Sliding Window: O(n) time, O(1) space
        # average >= threshold is equivalent to sum >= k * threshold
        target_sum = k * threshold
        current_sum = sum(arr[:k])
        count = 1 if current_sum >= target_sum else 0
        
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1
                
        return count


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "arr": [2, 2, 2, 2, 5, 5, 5, 8],
            "k": 3,
            "threshold": 4,
            "expected": 3,
        },
        {
            "arr": [11, 13, 17, 23, 29, 31, 7, 5, 2, 3],
            "k": 3,
            "threshold": 5,
            "expected": 6,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_arr = test["arr"]
        given_k = test["k"]
        given_threshold = test["threshold"]
        expected_output = test["expected"]
        actual_output = solution.numOfSubarrays(given_arr, given_k, given_threshold)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    arr = {given_arr}, k = {given_k}, threshold = {given_threshold}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
