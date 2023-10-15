"""
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
"""
from typing import List
class Solution:
    def generateAdjList(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(n)]
        for edge in connections:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        return adjList
    
    def removeEdgeFromAdjList(self, adjList: List[List[int]], node1: int, node2: int) -> List[List[int]]:
        adjList[node1].remove(node2)
        adjList[node2].remove(node1)
        return adjList

    def addEdgeToAdjList(self, adjList: List[List[int]], node1: int, node2: int) -> List[List[int]]:
        adjList[node1].append(node2)
        adjList[node2].append(node1)
        return adjList

    def areNodesConnected(self, node1: int, node2: int, adjList: List[List[int]]) -> bool:
        queue = [node1]
        visited = set([node1])
        while queue:
            current = queue.pop(0)
            for neighbor in adjList[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                if neighbor == node2:
                    return True
        return False

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        criticalEdges = []
        adjList = self.generateAdjList(n, connections)

        for edge in connections:
            # Remove edge between node1 and node2
            node1, node2 = edge
            adjList = self.removeEdgeFromAdjList(adjList, node1, node2)
            if not self.areNodesConnected(node1, node2, adjList):
                # If removing this edge disconnects the graph, it is a critical edge
                criticalEdges.append(edge)
            adjList = self.addEdgeToAdjList(adjList, node1, node2)

        return criticalEdges

if __name__ == '__main__':
    assert(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]])
    assert(Solution().criticalConnections(2, [[0,1]]) == [[0,1]])

