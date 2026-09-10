"""
LeetCode 167: Two Sum II - Input Array Is Sorted

Question:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one,
as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Given:
- numbers: List[int] (1-indexed array sorted in non-decreasing order)
- target: int
- Constraints:
    - 2 <= numbers.length <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - numbers is sorted in non-decreasing order.
    - -1000 <= target <= 1000
    - The tests are generated such that there is exactly one solution.

Output:
- List[int]: [index1, index2] (1-indexed indices of the two numbers that sum to target).

Examples:
- Example 1:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

- Example 2:
    Input: numbers = [2, 3, 4], target = 6
    Output: [1, 3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

- Example 3:
    Input: numbers = [-1, 0], target = -1
    Output: [1, 2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two-pointer approach: O(n) time, O(1) space
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # 1-indexed response
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return []


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "numbers": [2, 7, 11, 15],
            "target": 9,
            "expected": [1, 2],
        },
        {
            "numbers": [2, 3, 4],
            "target": 6,
            "expected": [1, 3],
        },
        {
            "numbers": [-1, 0],
            "target": -1,
            "expected": [1, 2],
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_numbers = test["numbers"]
        given_target = test["target"]
        expected_output = test["expected"]
        actual_output = solution.twoSum(given_numbers, given_target)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    numbers = {given_numbers}, target = {given_target}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
