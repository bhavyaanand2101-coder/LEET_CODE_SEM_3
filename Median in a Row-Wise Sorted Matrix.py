"""
Median in a Row-Wise Sorted Matrix
Difficulty: Medium | Accuracy: 55.05% | Points: 4

Given a row-wise sorted matrix mat[][], where the number of rows and columns is always odd.
Return the median of the matrix.

Examples:

Input: mat[][] = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

Input: mat[][] = [[2, 4, 9], [3, 6, 7], [4, 7, 10]]
Output: 6
Explanation: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.

Input: mat = [[3], [4], [8]]
Output: 4
Explanation: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.

Constraints:
1 <= mat.size(), mat[i].size() <= 400
1 <= mat[i][j] <= 2*10^3
"""

from bisect import bisect_right
from typing import List


class Solution:
    def median(self, mat: List[List[int]], *args) -> int:
        """
        Finds the median in a row-wise sorted matrix.
        
        Time Complexity: O(32 * R * log(C)) where R is number of rows and C is number of columns.
        Space Complexity: O(1)
        """
        r = len(mat)
        c = len(mat[0])
        
        # The minimum element is the minimum of the first column
        low = min(row[0] for row in mat)
        # The maximum element is the maximum of the last column
        high = max(row[-1] for row in mat)
        
        # Desired count of elements <= median: (R * C + 1) // 2
        desired_count = (r * c + 1) // 2
        
        while low < high:
            mid = (low + high) // 2
            
            # Count elements <= mid across all rows
            count = sum(bisect_right(row, mid) for row in mat)
            
            if count < desired_count:
                low = mid + 1
            else:
                high = mid
                
        return low


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 5),
        ([[2, 4, 9], [3, 6, 7], [4, 7, 10]], 6),
        ([[3], [4], [8]], 4),
    ]

    for i, (mat, expected) in enumerate(test_cases, 1):
        result = sol.median(mat)
        print(f"Test Case {i}:")
        print(f"  Input: {mat}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        assert result == expected, f"Assertion failed: expected {expected}, got {result}"
        print("  Status: PASSED\n")

    print("All test cases passed successfully!")
