"""
LeetCode 867: Transpose Matrix

Question:
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Given:
- matrix: List[List[int]] (2D integer array of dimensions m x n)
- Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 1000
    - 1 <= m * n <= 10^5
    - -10^9 <= matrix[i][j] <= 10^9

Output:
- List[List[int]]: The transposed matrix of dimensions n x m.

Examples:
- Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

- Example 2:
    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Transposes the given m x n matrix into an n x m matrix.

        Approach:
        1. Determine the dimensions of the original matrix:
           - m = number of rows = len(matrix)
           - n = number of columns = len(matrix[0])
        2. Create a new result matrix with dimensions n x m initialized to 0.
        3. Traverse each cell (r, c) of the original matrix and place it at (c, r) in the transposed matrix:
           transposed[c][r] = matrix[r][c]

        Time Complexity: O(m * n) - We visit every element in the matrix once.
        Space Complexity: O(m * n) - Space needed to store the transposed matrix.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Initialize transposed matrix of dimensions n x m
        transposed = [[0] * m for _ in range(n)]

        # Map matrix[r][c] to transposed[c][r]
        for r in range(m):
            for c in range(n):
                transposed[c][r] = matrix[r][c]

        return transposed

    def transpose_pythonic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Alternative Pythonic one-liner using zip and unpacking (*):
        zip(*matrix) groups the elements of matrix by their column indices.
        """
        return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        },
        {
            "matrix": [[1, 2, 3], [4, 5, 6]],
            "expected": [[1, 4], [2, 5], [3, 6]],
        },
        {
            "matrix": [[1]],
            "expected": [[1]],
        },
        {
            "matrix": [[1, 2, 3]],
            "expected": [[1], [2], [3]],
        },
        {
            "matrix": [[1], [2], [3]],
            "expected": [[1, 2, 3]],
        },
    ]

    for i, test in enumerate(test_cases, 1):
        given_matrix = test["matrix"]
        expected_output = test["expected"]
        actual_output = solution.transpose(given_matrix)

        is_pass = actual_output == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    matrix = {given_matrix}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {actual_output}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
