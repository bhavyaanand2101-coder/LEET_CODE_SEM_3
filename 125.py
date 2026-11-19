"""
LeetCode 125: Valid Palindrome

Question:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Given:
- s: str (input string consisting of printable ASCII characters)
- Constraints:
    - 1 <= s.length <= 2 * 10^5
    - s consists only of printable ASCII characters.

Output:
- bool: True if s is a palindrome, False otherwise.

Examples:
- Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

- Example 2:
    Input: s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.

- Example 3:
    Input: s = " "
    Output: True
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
                 Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two-Pointer Approach (In-Place, Optimal O(1) Auxiliary Space):

        Steps:
        1. Initialize `left` at index 0 and `right` at the last index (`len(s) - 1`).
        2. Move `left` forward until it encounters an alphanumeric character.
        3. Move `right` backward until it encounters an alphanumeric character.
        4. Compare characters (case-insensitively using `.lower()`):
           - If they don't match, return False immediately.
        5. Move `left` forward and `right` backward by 1.
        6. Repeat until `left >= right`. If all checks match, return True.

        Time Complexity: O(n) - We visit each character at most once.
        Space Complexity: O(1) - No extra string allocations; checks are done in-place.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase versions of the characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isPalindromeFiltered(self, s: str) -> bool:
        """
        Filtering & Reversal Approach:
        Filters out non-alphanumeric characters, converts to lowercase,
        and checks if the cleaned string equals its reverse.

        Time Complexity: O(n)
        Space Complexity: O(n) - Requires storing the filtered string.
        """
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    solution = Solution()

    # Test cases with inputs, expected outputs, and descriptions
    test_cases = [
        {
            "input": "A man, a plan, a canal: Panama",
            "expected": True,
            "description": "Standard sentence with spaces and punctuation",
        },
        {
            "input": "race a car",
            "expected": False,
            "description": "Not a palindrome",
        },
        {
            "input": " ",
            "expected": True,
            "description": "Only whitespace (empty when cleaned)",
        },
        {
            "input": "0P",
            "expected": False,
            "description": "Alphanumeric mismatch with digits",
        },
        {
            "input": "ab_a",
            "expected": True,
            "description": "Contains underscore (non-alphanumeric character)",
        },
        {
            "input": "a.",
            "expected": True,
            "description": "Single letter followed by punctuation",
        },
        {
            "input": "Was it a car or a cat I saw?",
            "expected": True,
            "description": "Another valid palindrome sentence",
        },
        {
            "input": "12321",
            "expected": True,
            "description": "Numeric palindrome",
        },
        {
            "input": "123456",
            "expected": False,
            "description": "Numeric non-palindrome",
        },
    ]

    print("Running Tests for LeetCode 125: Valid Palindrome\n" + "=" * 65)

    for i, test in enumerate(test_cases, 1):
        s_input = test["input"]
        expected = test["expected"]
        desc = test["description"]

        # Test Two-Pointer Approach
        result_two_pointer = solution.isPalindrome(s_input)

        # Test Filtered Approach
        result_filtered = solution.isPalindromeFiltered(s_input)

        print(f"Test Case {i} ({desc}):")
        print(f"  Input:        '{s_input}'")
        print(f"  Expected:     {expected}")
        print(f"  Two-Pointer:  {result_two_pointer} -> {'PASS' if result_two_pointer == expected else 'FAIL'}")
        print(f"  Filtered:     {result_filtered} -> {'PASS' if result_filtered == expected else 'FAIL'}")
        print("-" * 65)

        assert result_two_pointer == expected, (
            f"Two-pointer failed for '{s_input}': got {result_two_pointer}, expected {expected}"
        )
        assert result_filtered == expected, (
            f"Filtered failed for '{s_input}': got {result_filtered}, expected {expected}"
        )

    print("All test cases passed successfully!")
