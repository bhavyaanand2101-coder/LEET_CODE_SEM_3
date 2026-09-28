"""
LeetCode 441: Arranging Coins

Question:
You have n coins and you want to build a staircase with these coins. The staircase
consists of k rows where the ith row has exactly i coins. The last row of the staircase
may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Given:
- n: int (number of coins)
- Constraints:
    - 1 <= n <= 2^31 - 1

Output:
- int: Number of complete rows formed.

Examples:
- Example 1:
    Input: n = 5
    Output: 2
    Explanation: Because the 3rd row is incomplete, we return 2.

- Example 2:
    Input: n = 8
    Output: 3
    Explanation: Because the 4th row is incomplete, we return 3.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Binary Search Approach:
        The total number of coins required to build k complete rows is:
            total_coins = k * (k + 1) // 2

        We want to find the largest integer k such that k * (k + 1) // 2 <= n.
        Since total_coins strictly increases with k, we can binary search over
        the range [1, n].

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "n": 5,
            "expected": 2,
        },
        {
            "n": 8,
            "expected": 3,
        },
        {
            "n": 1,
            "expected": 1,
        },
        {
            "n": 3,
            "expected": 2,
        },
        {
            "n": 6,
            "expected": 3,
        },
        {
            "n": 10,
            "expected": 4,
        },
        {
            "n": 2147483647,
            "expected": 65535,
        },
    ]

    for i, test in enumerate(test_cases, 1):
        given_n = test["n"]
        expected_output = test["expected"]
        actual_output = solution.arrangeCoins(given_n)

        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    n = {given_n}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
