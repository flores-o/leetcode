"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from typing import List

class Solution:
    def visitIsland(self, isConnected: List[List[int]], visited: List[List[bool]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(isConnected) or j >= len(isConnected[0]) or visited[i][j] or isConnected[i][j] == 0:
            return
        
        visited[i][j] = True

        self.visitIsland(isConnected, visited, i-1, j)
        self.visitIsland(isConnected, visited, i+1, j)
        self.visitIsland(isConnected, visited, i, j-1)
        self.visitIsland(isConnected, visited, i, j+1)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        if not isConnected:
            return 0
        if not isConnected[0]:
            return 0
        
        rows = len(isConnected)
        cols = len(isConnected[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # Visit each unvisited island and increment count
        count = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and isConnected[i][j] == 1:
                    self.visitIsland(isConnected, visited, i, j)
                    count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    # Test case 1
    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
    # Test case 2
    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

        