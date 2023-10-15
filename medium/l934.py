"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

[[0,1]
 [1,0]]


[[0,1,0],
[0,0,0], 
[0,0,1]]

[[1,1,1,1,1],
[1,0,0,0,1],
[1,0,1,0,1],
[1,0,0,0,1],
[1,1,1,1,1]]

"""
from typing import List

class Solution:
    def get_grid_dimensions(self, grid: List[List[int]]) -> List[int]:
        assert(len(grid))
        assert(len(grid[0]))

        return [len(grid), len(grid[0])]
    

    def is_valid_cell(self, grid: List[List[int]], cell: List[int]) -> bool:
        m, n = self.get_grid_dimensions(grid)
        row, col = cell
        return row >= 0 and row < m and col >= 0 and col < n
    

    def mark_island(self, grid: List[List[int]], row: int, col: int):
        if not self.is_valid_cell(grid, [row, col]):
            return
        if grid[row][col] != 1:
            return
        grid[row][col] = 2
        self.mark_island(grid, row + 1, col)
        self.mark_island(grid, row - 1, col)
        self.mark_island(grid, row, col + 1)
        self.mark_island(grid, row, col - 1)
    

    def shortest_bridge_from_given_cell(self, grid: List[List[int]], start_row: int, start_col: int, target_value:int) -> int:
        m, n = self.get_grid_dimensions(grid)
        queue = [(start_row, start_col, 0)]
        visited = set([(start_row, start_col)])
        while queue:
            row, col, distance = queue.pop(0)
            if grid[row][col] == target_value:
                return distance - 1
            for neighbor in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if self.is_valid_cell(grid, neighbor) and tuple(neighbor) not in visited:
                    queue.append((neighbor[0], neighbor[1], distance + 1))
                    visited.add(tuple(neighbor))
        return -1
    

    def shortest_bridge_from_island(self, grid: List[List[int]], start_value, target_value) -> int:
        shortest_bridge = float('inf')
        m, n = self.get_grid_dimensions(grid)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == start_value:
                    shortest_bridge = min(shortest_bridge, self.shortest_bridge_from_given_cell(grid, row, col, target_value))
        return shortest_bridge


    def shortestBridge(self, grid: List[List[int]]) -> int:
        grid_copy = [row[:] for row in grid]

        m, n = self.get_grid_dimensions(grid)
        # Mark the first island
        for row in range(m):
            for col in range(n):
                if grid_copy[row][col] == 1:
                    self.mark_island(grid_copy, row, col)
                    break
            else:
                continue
            break
        # Find the shortest bridge from the first island to the second island
        return self.shortest_bridge_from_island(grid_copy, 2, 1)
    
if __name__ == '__main__':
    sol = Solution()
    grid = [[0,1],[1,0]]
    print(sol.shortestBridge(grid))
    assert(sol.shortestBridge(grid) == 1)

    grid = [[0,1,0],[0,0,0],[0,0,1]]
    print(sol.shortestBridge(grid))
    assert(sol.shortestBridge(grid) == 2)

    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(sol.shortestBridge(grid))
    assert(sol.shortestBridge(grid) == 1)
