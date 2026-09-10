"""
LeetCode 11: Container With Most Water

Question:
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Given:
- height: List[int] (array of heights representing vertical lines)
- Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4

Output:
- int: The maximum amount of water the container can store.

Examples:
- Example 1:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: The max area is between index 1 (height 8) and index 8 (height 7).
                 Area = min(8, 7) * (8 - 1) = 7 * 7 = 49.

- Example 2:
    Input: height = [1, 1]
    Output: 1
    Explanation: Area = min(1, 1) * (1 - 0) = 1 * 1 = 1.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach: O(n) time, O(1) space
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_water = max(max_water, current_area)
            
            # Move the pointer with the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
        },
        {
            "height": [1, 1],
            "expected": 1,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_height = test["height"]
        expected_output = test["expected"]
        actual_output = solution.maxArea(given_height)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    height = {given_height}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
