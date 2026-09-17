"""
LeetCode 3: Longest Substring Without Repeating Characters

Question:
Given a string s, find the length of the longest substring without duplicate characters.

Given:
- s: str (input string consisting of English letters, digits, symbols, and spaces)
- Constraints:
    - 0 <= s.length <= 10^5
    - s consists of English letters, digits, symbols and spaces.

Output:
- int: The length of the longest substring without repeating characters.

Examples:
- Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

- Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

- Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dynamic-size Sliding Window with Hash Map: O(n) time, O(min(m, n)) space
        last_seen = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            # If the character was seen inside the current window, move the left boundary
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "s": "abcabcbb",
            "expected": 3,
        },
        {
            "s": "bbbbb",
            "expected": 1,
        },
        {
            "s": "pwwkew",
            "expected": 3,
        },
        {
            "s": "",
            "expected": 0,
        },
        {
            "s": " ",
            "expected": 1,
        },
        {
            "s": "au",
            "expected": 2,
        },
        {
            "s": "tmmzuxt",
            "expected": 5,
        },
    ]

    for i, test in enumerate(test_cases, 1):
        given_s = test["s"]
        expected_output = test["expected"]
        actual_output = solution.lengthOfLongestSubstring(given_s)

        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    s = \"{given_s}\"")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
