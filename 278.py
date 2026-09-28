"""
LeetCode 278: First Bad Version

Question:
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad
version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number
of calls to the API.

Given:
- n: int (number of versions from 1 to n)
- API: isBadVersion(version: int) -> bool
- Constraints:
    - 1 <= bad <= n <= 2^31 - 1

Output:
- int: The version number of the first bad version.

Examples:
- Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
        call isBadVersion(3) -> False
        call isBadVersion(5) -> True
        call isBadVersion(4) -> True
        Then 4 is the first bad version.

- Example 2:
    Input: n = 1, bad = 1
    Output: 1
"""


# The isBadVersion API is already defined for you on LeetCode.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary Search:
        Since all versions after a bad version are also bad, the boolean array
        [isBadVersion(1), isBadVersion(2), ..., isBadVersion(n)] is sorted in the
        form: [False, False, ..., True, True].
        We can find the boundary between False and True in O(log n) time.

        Time Complexity: O(log n) API calls
        Space Complexity: O(1)
        """
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid is bad, the first bad version could be mid or to its left
                right = mid
            else:
                # mid is good, the first bad version must be strictly after mid
                left = mid + 1

        return left


if __name__ == "__main__":
    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "n": 5,
            "bad": 4,
            "expected": 4,
        },
        {
            "n": 1,
            "bad": 1,
            "expected": 1,
        },
        {
            "n": 10,
            "bad": 1,
            "expected": 1,
        },
        {
            "n": 10,
            "bad": 10,
            "expected": 10,
        },
        {
            "n": 2147483647,
            "bad": 2147483647,
            "expected": 2147483647,
        },
        {
            "n": 2147483647,
            "bad": 1700000000,
            "expected": 1700000000,
        },
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        n = test["n"]
        bad = test["bad"]
        expected_output = test["expected"]

        # Mock isBadVersion API for the current test case
        def isBadVersion(version: int, current_bad: int = bad) -> bool:
            return version >= current_bad

        actual_output = solution.firstBadVersion(n)
        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    n = {n}, bad = {bad}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
