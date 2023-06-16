"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    self.markIsland(grid, i, j)
                    count += 1
        return count
    
    def markIsland(self, grid: List[List[str]], i:int, j:int) -> int:
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            grid[i][j] = 'x'
            if i > 0 and grid[i-1][j] == '1':
                queue.append((i-1, j))
            if i < len(grid)-1 and grid[i+1][j] == '1':
                queue.append((i+1, j))
            if j > 0 and grid[i][j-1] == '1':
                queue.append((i, j-1))
            if j < len(grid[i])-1 and grid[i][j+1] == '1':
                queue.append((i, j+1))
        return grid

if __name__ == "__main__":
    # use assert to validate the test cases
    solution = Solution()
    assert solution.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]) == 1
    assert solution.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]) == 3
    assert solution.numIslands([
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]) == 1
    assert solution.numIslands([
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]) == 1  
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        return num_islands

if __name__ == "__main__":
    # use assert to validate the test cases
    solution = Solution()
    assert solution.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]) == 1
    assert solution.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]) == 3
    assert solution.numIslands([
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]) == 1
    assert solution.numIslands([
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]) == 1

