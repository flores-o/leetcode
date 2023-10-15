"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

from typing import List

class Solution:
    def get_matrix_dimensions(self, mat: List[List[int]]) -> List[int]:
        assert(len(mat))
        assert(len(mat[0]))

        return [len(mat), len(mat[0])]
    
    def is_valid_cell(self, mat: List[List[int]], cell: List[int]) -> bool:
        m, n = self.get_matrix_dimensions(mat)
        row, col = cell
        return row >= 0 and row < m and col >= 0 and col < n
    
    def get_neighbors(self, mat: List[List[int]], cell: List[int]) -> List[List[int]]:
        row, col = cell
        neighbors = []
        for neighbor in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            if self.is_valid_cell(mat, neighbor):
                neighbors.append(neighbor)
        return neighbors
    
    def closest_zero_given_cell(self, mat: List[List[int]], cell: List[int]) -> int:
        m, n = self.get_matrix_dimensions(mat)
        row, col = cell
        if mat[row][col] == 0:
            return 0
        queue = [(cell, 0)]
        visited = set([tuple(cell)])
        while queue:
            current, distance = queue.pop(0)
            if mat[current[0]][current[1]] == 0:
                return distance
            for neighbor in self.get_neighbors(mat, current):
                if tuple(neighbor) not in visited:
                    queue.append((neighbor, distance+1))
                    visited.add(tuple(neighbor))
        return -1
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col] = self.closest_zero_given_cell(mat, [row, col])
        return mat
    
if __name__ == '__main__':
    input = [[0,0,0],[0,1,0],[0,0,0]]
    output = [[0,0,0],[0,1,0],[0,0,0]]
    assert(Solution().updateMatrix(input) == output)

    input = [[0,0,0],[0,1,0],[1,1,1]]
    output = [[0,0,0],[0,1,0],[1,2,1]]
    assert(Solution().updateMatrix(input) == output)