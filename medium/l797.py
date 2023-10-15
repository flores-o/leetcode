"""
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

from typing import List
class Solution:
    def recordPaths(self, edges: List[List[int]], currentNode: int, target: int, currentPath: List[int], allPaths: List[List[int]]) -> List[List[int]]:
        currentPath.append(currentNode)
        if currentNode == target:
            allPaths.append(list(currentPath))
        else:
            for neighbor in edges[currentNode]:
                self.recordPaths(edges, neighbor, target, currentPath, allPaths)
                currentPath.pop()
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        allPaths = []
        currentPath = []

        self.recordPaths(graph, 0, n-1, currentPath, allPaths)

        return allPaths

if __name__ == '__main__':
    graph = [[1,2],[3],[3],[]]
    assert (Solution().allPathsSourceTarget(graph) == [[0,1,3],[0,2,3]])

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    assert (Solution().allPathsSourceTarget(graph) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
        