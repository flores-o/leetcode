"""
1926. Nearest Exit from Entrance in Maze
Medium
2.1K
79
Companies
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""

from typing import List 

class Solution:
    def get_maze_dimensions(self, maze: List[List[str]]) -> List[int]:
        assert(len(maze))
        assert(len(maze[0]))

        return [len(maze), len(maze[0])]

    def is_valid_cell(self, maze: List[List[str]], cell: List[int]) -> bool:
        m, n = self.get_maze_dimensions(maze)
        row, col = cell
        return row >= 0 and row < m and col >= 0 and col < n
    
    def get_neighbors(self, maze: List[List[str]], cell: List[int]) -> List[List[int]]:
        row, col = cell
        neighbors = []
        for neighbor in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            if self.is_valid_cell(maze, neighbor):
                neighbors.append(neighbor)
        return neighbors
    
    def is_exit(self, maze: List[List[str]], cell: List[int], entrance: List[int]) -> bool:
        if cell == entrance:
            return False
        
        m, n = self.get_maze_dimensions(maze)
        row, col = cell
        return row == 0 or row == m-1 or col == 0 or col == n-1

    def is_empty_cell(self, maze: List[List[str]], cell: List[int]) -> bool:
        row, col = cell
        return maze[row][col] == '.'
    
    def nearest_exit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = self.get_maze_dimensions(maze)
        queue = [(entrance, 0)]
        visited = set([tuple(entrance)])
        while queue:
            current, distance = queue.pop(0)
            if self.is_exit(maze, current, entrance):
                return distance
            for neighbor in self.get_neighbors(maze, current):
                if tuple(neighbor) not in visited and self.is_empty_cell(maze, neighbor):
                    queue.append((neighbor, distance+1))
                    visited.add(tuple(neighbor))
        return -1   

if __name__ == '__main__':
    sol = Solution()
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    print(sol.nearest_exit(maze, entrance))
    assert(sol.nearest_exit(maze, entrance) == 1)

    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    print(sol.nearest_exit(maze, entrance))
    assert(sol.nearest_exit(maze, entrance) == 2)

    maze = [[".","+"]]
    entrance = [0,0]
    print(sol.nearest_exit(maze, entrance))
    assert(sol.nearest_exit(maze, entrance) == -1)



