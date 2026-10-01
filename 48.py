"""
LeetCode 48: Rotate Image

Question:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Given:
- matrix: List[List[int]] (square 2D integer array of dimensions n x n)
- Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000

Output:
- None: Modify the matrix in-place.

Examples:
- Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

- Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the n x n matrix 90 degrees clockwise in-place.

        Approach (Transpose + Reverse):
        A 90-degree clockwise rotation can be decomposed into two simple steps:
        1. Transpose the matrix:
           Swap matrix[i][j] with matrix[j][i] along the main diagonal.
           Original:
             [1, 2, 3]       [1, 4, 7]
             [4, 5, 6]  -->  [2, 5, 8]
             [7, 8, 9]       [3, 6, 9]

        2. Reverse each row:
           Reflect elements horizontally (two-pointer swap per row).
             [1, 4, 7]       [7, 4, 1]
             [2, 5, 8]  -->  [8, 5, 2]
             [3, 6, 9]       [9, 6, 3]

        Time Complexity: O(n^2) - Transpose visits n*(n-1)/2 elements, reverse visits n*(n/2) elements.
        Space Complexity: O(1) - All modifications are performed in-place with no extra memory.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix in-place across the main diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "matrix": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            "expected": [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ],
        },
        {
            "matrix": [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16],
            ],
            "expected": [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11],
            ],
        },
        {
            "matrix": [[1]],
            "expected": [[1]],
        },
        {
            "matrix": [
                [1, 2],
                [3, 4],
            ],
            "expected": [
                [3, 1],
                [4, 2],
            ],
        },
    ]

    for i, test in enumerate(test_cases, 1):
        # Deep copy for display before mutation
        original_matrix = [row[:] for row in test["matrix"]]
        matrix_to_rotate = [row[:] for row in test["matrix"]]
        expected_output = test["expected"]

        # In-place rotation
        solution.rotate(matrix_to_rotate)

        is_pass = matrix_to_rotate == expected_output

        print(f"--- Example {i} ---")
        print(f"Given (Input):    matrix = {original_matrix}")
        print(f"Expected Output:  {expected_output}")
        print(f"Actual Output:    {matrix_to_rotate}")
        print(f"Status:           {'PASS' if is_pass else 'FAIL'}\n")
