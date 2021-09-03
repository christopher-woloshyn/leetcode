"""
Problem:

Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's, and return the matrix.

You must do it in place.
"""
from typing import List


# Time: O(m*n), Space: O(m+n)
class Solution:
    """
    First we create two arrays which will track which row and column indices
    contain a zero. Then we can iterate through each of those lists converting
    each entire row and entire column to 0's. This is less space efficient
    because it, at worst, creates two new arrays of length m and n; hence the
    space complexity is O(m+n). The algorithm must iterate through
    every row of length m and column of length n at least once, converging on
    a time complexity of O(m*n).
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = []
        col = []
        
        # Check for 0's in the matrix and store the indices.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        # Convert all rows that contain a 0 entirely to 0's.
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        # Convert all columns that contain a 0 entirely to 0's.
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0

# Time: O(m*n), Space: O(1)
class Solution:
    """
    The trick to this solution is using the first row and first column as
    memory, instead of creating two new arrays to track which rows and columns
    a zero appears. By storing whether or not a zero appears in the first row
    or column, we know the space complexity will be O(1) since only a constant
    number of new variables are declared. The algorithm must iterate through
    every row of length m and column of length n at least once, converging on
    a time complexity of O(m*n).
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check for 0s in the first row.
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_has_zero = True
                break
        
        # Check for 0s in the first column.
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Check for 0s in all but the first row and column.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Process all rows and columns except for the first row and column.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Process first row.
        if first_row_has_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        # Process first column.
        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                