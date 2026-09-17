"""
LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length

Question:
Given a string s and an integer k, return the maximum number of vowel letters in 
any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Given:
- s: str (input string consisting of lowercase English letters)
- k: int (length of the substring)
- Constraints:
    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
    - 1 <= k <= s.length

Output:
- int: Maximum number of vowel letters in any substring of length k.

Examples:
- Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

- Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

- Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Fixed-size Sliding Window: O(n) time, O(1) space
        vowels = {"a", "e", "i", "o", "u"}
        
        # Count vowels in the first window of size k
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels
        
        # Early exit optimization: cannot have more than k vowels in a substring of length k
        if max_vowels == k:
            return k
            
        # Slide window across the rest of string s
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                if max_vowels == k:
                    return k
                    
        return max_vowels


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "s": "abciiidef",
            "k": 3,
            "expected": 3,
        },
        {
            "s": "aeiou",
            "k": 2,
            "expected": 2,
        },
        {
            "s": "leetcode",
            "k": 3,
            "expected": 2,
        },
        {
            "s": "rhythms",
            "k": 4,
            "expected": 0,
        },
        {
            "s": "tryhard",
            "k": 4,
            "expected": 1,
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        given_s = test["s"]
        given_k = test["k"]
        expected_output = test["expected"]
        actual_output = solution.maxVowels(given_s, given_k)
        
        is_pass = actual_output == expected_output
        
        print(f"--- Example {i} ---")
        print(f"Given (Input):    s = \"{given_s}\", k = {given_k}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
