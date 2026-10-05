"""
LeetCode 1572: Matrix Diagonal Sum

Question:
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements
on the secondary diagonal that are not part of the primary diagonal.

Given:
- mat: List[List[int]] (square 2D integer array of dimensions n x n)
- Constraints:
    - n == mat.length == mat[i].length
    - 1 <= n <= 100
    - 1 <= mat[i][j] <= 100

Output:
- int: Sum of the primary and secondary diagonal elements, counting intersection only once.

Examples:
- Example 1:
    Input: mat = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
    Output: 25
    Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
    Notice that element mat[1][1] = 5 is counted only once.

- Example 2:
    Input: mat = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
    Output: 8

- Example 3:
    Input: mat = [[5]]
    Output: 5
"""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Calculates the sum of both the primary and secondary diagonals of a square matrix.
        If the matrix dimension n is odd, the center element is shared by both diagonals
        and is included only once.

        Approach (Single Pass O(n)):
        1. Iterate through each row index i from 0 to n - 1:
           - Primary diagonal element is at mat[i][i].
           - Secondary diagonal element is at mat[i][n - 1 - i].
        2. Add both diagonal elements to total.
        3. If n is odd, the middle element at mat[n // 2][n // 2] is added twice,
           so subtract it once at the end (or skip adding secondary if i == n - 1 - i).

        Complexity:
        - Time Complexity: O(n) where n is the number of rows/columns. We visit each row once.
        - Space Complexity: O(1) auxiliary space as only a single accumulator variable is maintained.
        """
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]
            # Avoid double counting the center element when n is odd
            if i != n - 1 - i:
                total += mat[i][n - 1 - i]

        return total


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "mat": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            "expected": 25,
            "description": "3x3 Odd dimension matrix (center element 5 counted once)",
        },
        {
            "mat": [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
            ],
            "expected": 8,
            "description": "4x4 Even dimension matrix (no overlapping center element)",
        },
        {
            "mat": [[5]],
            "expected": 5,
            "description": "1x1 Single element matrix",
        },
        {
            "mat": [
                [1, 2],
                [3, 4],
            ],
            "expected": 10,
            "description": "2x2 Even dimension matrix: 1 + 4 + 2 + 3 = 10",
        },
        {
            "mat": [
                [7, 3, 1, 9],
                [3, 4, 6, 2],
                [6, 9, 1, 5],
                [8, 5, 2, 4],
            ],
            "expected": 48,
            "description": "4x4 Arbitrary values: (7+4+1+4) + (9+6+9+8) = 48",
        },
    ]

    for i, test in enumerate(test_cases, 1):
        mat_input = test["mat"]
        expected_output = test["expected"]
        actual_output = solution.diagonalSum(mat_input)
        is_pass = actual_output == expected_output

        print(f"--- Test Case {i}: {test['description']} ---")
        print(f"Input Matrix:    {mat_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output:   {actual_output}")
        print(f"Status:          {'PASS' if is_pass else 'FAIL'}\n")
