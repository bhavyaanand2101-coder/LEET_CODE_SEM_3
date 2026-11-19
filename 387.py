"""
LeetCode 387: First Unique Character in a String

Question:
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Given:
- s: str (input string consisting of lowercase English letters)
- Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only lowercase English letters.

Output:
- int: The index of the first non-repeating character, or -1 if none exists.

Examples:
- Example 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

- Example 2:
    Input: s = "loveleetcode"
    Output: 2
    Explanation: The character 'v' at index 2 is the first character that does not occur at any other index.

- Example 3:
    Input: s = "aabb"
    Output: -1
    Explanation: All characters appear more than once.
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Two-Pass Hash Map / Frequency Counter Approach:

        Steps:
        1. Build a frequency count of each character in string `s`.
        2. Iterate through string `s` with indices from left to right.
        3. Return the index of the first character whose frequency is 1.
        4. If no character has a frequency of 1, return -1.

        Time Complexity: O(n) - One pass to count frequencies, second pass to find the index.
        Space Complexity: O(1) - The character set is fixed (at most 26 lowercase English letters).
        """
        char_count = Counter(s)

        for i, ch in enumerate(s):
            if char_count[ch] == 1:
                return i

        return -1

    def firstUniqCharArray(self, s: str) -> int:
        """
        Fixed-size Frequency Array Approach:
        Uses an array of size 26 instead of a hash table for minimal overhead.

        Time Complexity: O(n)
        Space Complexity: O(1) - Exactly 26 integers.
        """
        counts = [0] * 26
        base = ord("a")

        # Pass 1: Count character occurrences
        for ch in s:
            counts[ord(ch) - base] += 1

        # Pass 2: Find the first character with frequency 1
        for i, ch in enumerate(s):
            if counts[ord(ch) - base] == 1:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test cases with input strings, expected outputs, and descriptions
    test_cases = [
        {
            "input": "leetcode",
            "expected": 0,
            "description": "Unique character at the beginning ('l')",
        },
        {
            "input": "loveleetcode",
            "expected": 2,
            "description": "Unique character in the middle ('v')",
        },
        {
            "input": "aabb",
            "expected": -1,
            "description": "No unique characters",
        },
        {
            "input": "z",
            "expected": 0,
            "description": "Single character string",
        },
        {
            "input": "aabbccd",
            "expected": 6,
            "description": "Unique character at the very end ('d')",
        },
        {
            "input": "abcdef",
            "expected": 0,
            "description": "All characters are unique, returns first index",
        },
        {
            "input": "dddccdbba",
            "expected": 8,
            "description": "Last character is the only unique one ('a')",
        },
    ]

    print("Running Tests for LeetCode 387: First Unique Character in a String\n" + "=" * 65)

    for i, test in enumerate(test_cases, 1):
        s_input = test["input"]
        expected = test["expected"]
        desc = test["description"]

        # Test both Counter and Array approaches
        result_counter = solution.firstUniqChar(s_input)
        result_array = solution.firstUniqCharArray(s_input)

        print(f"Test Case {i} ({desc}):")
        print(f"  Input:    '{s_input}'")
        print(f"  Expected: {expected}")
        print(f"  Counter:  {result_counter} -> {'PASS' if result_counter == expected else 'FAIL'}")
        print(f"  Array:    {result_array} -> {'PASS' if result_array == expected else 'FAIL'}")
        print("-" * 65)

        assert result_counter == expected, f"Counter failed for {s_input}: got {result_counter}, expected {expected}"
        assert result_array == expected, f"Array failed for {s_input}: got {result_array}, expected {expected}"

    print("All test cases passed successfully!")
