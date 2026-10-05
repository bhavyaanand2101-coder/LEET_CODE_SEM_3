"""
LeetCode 54: Spiral Matrix

Question:
Given an m x n matrix, return all elements of the matrix in spiral order.

Given:
- matrix: List[List[int]] (2D array of dimensions m x n)
- Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 10
    - -100 <= matrix[i][j] <= 100

Output:
- List[int]: Elements of the matrix visited in clockwise spiral order.

Examples:
- Example 1:
    Input: matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

- Example 2:
    Input: matrix = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverses an m x n matrix in clockwise spiral order using boundary pointers.

        Approach (Four Boundaries):
        1. Maintain four boundary pointers:
           - top: index of top-most unprocessed row (starts at 0)
           - bottom: index of bottom-most unprocessed row (starts at m - 1)
           - left: index of left-most unprocessed column (starts at 0)
           - right: index of right-most unprocessed column (starts at n - 1)

        2. In each iteration (while top <= bottom and left <= right):
           - Move right across row 'top': from 'left' to 'right', then top += 1
           - Move down along column 'right': from 'top' to 'bottom', then right -= 1
           - If top <= bottom:
               Move left across row 'bottom': from 'right' down to 'left', then bottom -= 1
           - If left <= right:
               Move up along column 'left': from 'bottom' down to 'top', then left += 1

        Complexity:
        - Time Complexity: O(m * n) where m is the number of rows and n is the number of columns.
          Every cell is visited and added to the output list exactly once.
        - Space Complexity: O(1) auxiliary space (excluding the output list of size m * n).
        """
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Right along top boundary
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse Down along right boundary
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Traverse Left along bottom boundary (if row remains)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse Up along left boundary (if column remains)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res


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
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "description": "3x3 Square Matrix (Example 1)",
        },
        {
            "matrix": [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "description": "3x4 Rectangular Matrix (Example 2)",
        },
        {
            "matrix": [[1]],
            "expected": [1],
            "description": "1x1 Single Element Matrix",
        },
        {
            "matrix": [[1, 2, 3, 4, 5]],
            "expected": [1, 2, 3, 4, 5],
            "description": "1x5 Single Row Matrix",
        },
        {
            "matrix": [
                [1],
                [2],
                [3],
                [4],
                [5],
            ],
            "expected": [1, 2, 3, 4, 5],
            "description": "5x1 Single Column Matrix",
        },
        {
            "matrix": [
                [1, 2],
                [3, 4],
            ],
            "expected": [1, 2, 4, 3],
            "description": "2x2 Square Matrix",
        },
    ]

    for i, test in enumerate(test_cases, 1):
        mat_input = test["matrix"]
        expected_output = test["expected"]
        actual_output = solution.spiralOrder(mat_input)
        is_pass = actual_output == expected_output

        print(f"--- Test Case {i}: {test['description']} ---")
        print(f"Input Matrix:    {mat_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output:   {actual_output}")
        print(f"Status:          {'PASS' if is_pass else 'FAIL'}\n")
