"""
LeetCode 9: Palindrome Number

Question:
Given an integer x, return true if x is a palindrome, and false otherwise.

Given:
- x: int (input integer)
- Constraints:
    - -2^31 <= x <= 2^31 - 1

Output:
- bool: True if x is a palindrome, False otherwise.

Examples:
- Example 1:
    Input: x = 121
    Output: True
    Explanation: 121 reads as 121 from left to right and from right to left.

- Example 2:
    Input: x = -121
    Output: False
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
                 Therefore it is not a palindrome.

- Example 3:
    Input: x = 10
    Output: False
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Optimal Approach: Revert Half of the Number (No String Conversion).

        Why Revert Only Half?
        - Reversing the entire integer could theoretically overflow a 32-bit integer
          in languages with fixed-width integers (like C++/Java).
        - By reversing only half of the number, we compare the first half and the second half,
          guaranteeing no overflow and cutting the number of iterations in half.

        Algorithm:
        1. Special Cases:
           - All negative numbers are not palindromes (e.g., -121 reversed is 121-).
           - If the last digit is 0, the first digit must also be 0 for it to be a palindrome.
             Only 0 itself satisfies this condition (e.g., 10, 100 are not palindromes).
        2. Reverse digits from the right into `reverted_number` until `x <= reverted_number`.
           At that point, we've processed half of the digits.
        3. For even number of digits (e.g., 1221):
           - `x` will be 12, `reverted_number` will be 12. Check `x == reverted_number`.
        4. For odd number of digits (e.g., 12321):
           - `x` will be 12, `reverted_number` will be 123. The middle digit doesn't matter,
             so check `x == reverted_number // 10`.

        Time Complexity: O(log10(n)) - We divide by 10 in every iteration.
        Space Complexity: O(1) - Constant auxiliary space, no string conversion.
        """
        # Special cases:
        # 1. Negative numbers can never be palindromes due to '-' sign.
        # 2. If the last digit is 0, the number must be 0 to be a palindrome.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by reverted_number // 10
        # For example when the input is 12321, at the end of the while loop we get x = 12, reverted_number = 123
        return x == reverted_number or x == reverted_number // 10

    def isPalindromeFullReversal(self, x: int) -> bool:
        """
        Alternative Math Approach: Reversing the entire number (No String Conversion).

        Time Complexity: O(log10(n))
        Space Complexity: O(1)
        """
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return original == reversed_num

    def isPalindromeString(self, x: int) -> bool:
        """
        String Conversion Approach (Baseline):
        Convert integer to string and compare with its reverse.

        Time Complexity: O(n) where n is the number of digits.
        Space Complexity: O(n) for string allocation.
        """
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()

    # Test cases with inputs, expected outputs, and descriptions
    test_cases = [
        {
            "input": 121,
            "expected": True,
            "description": "Odd number of digits palindrome",
        },
        {
            "input": -121,
            "expected": False,
            "description": "Negative number with minus sign",
        },
        {
            "input": 10,
            "expected": False,
            "description": "Number ending with zero (non-zero)",
        },
        {
            "input": 0,
            "expected": True,
            "description": "Single digit zero",
        },
        {
            "input": 7,
            "expected": True,
            "description": "Single digit non-zero",
        },
        {
            "input": 1221,
            "expected": True,
            "description": "Even number of digits palindrome",
        },
        {
            "input": 1001,
            "expected": True,
            "description": "Even number of digits with middle zeros",
        },
        {
            "input": 1000021,
            "expected": False,
            "description": "Non-palindrome with zeros in between",
        },
        {
            "input": 123454321,
            "expected": True,
            "description": "Large odd-length palindrome",
        },
        {
            "input": 2147483647,
            "expected": False,
            "description": "Max 32-bit signed integer (not palindrome)",
        },
    ]

    print("Running Tests for LeetCode 9: Palindrome Number\n" + "=" * 65)

    for i, test in enumerate(test_cases, 1):
        x_val = test["input"]
        expected = test["expected"]
        desc = test["description"]

        # Run all three implementations
        result_half = solution.isPalindrome(x_val)
        result_full = solution.isPalindromeFullReversal(x_val)
        result_str = solution.isPalindromeString(x_val)

        print(f"Test Case {i} ({desc}):")
        print(f"  Input:         {x_val}")
        print(f"  Expected:      {expected}")
        print(f"  Half-Reversal: {result_half} -> {'PASS' if result_half == expected else 'FAIL'}")
        print(f"  Full-Reversal: {result_full} -> {'PASS' if result_full == expected else 'FAIL'}")
        print(f"  String-Based:  {result_str} -> {'PASS' if result_str == expected else 'FAIL'}")
        print("-" * 65)

        assert result_half == expected, f"Half-Reversal failed for {x_val}: got {result_half}, expected {expected}"
        assert result_full == expected, f"Full-Reversal failed for {x_val}: got {result_full}, expected {expected}"
        assert result_str == expected, f"String-based failed for {x_val}: got {result_str}, expected {expected}"

    print("All test cases passed successfully!")
