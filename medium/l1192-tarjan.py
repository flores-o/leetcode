"""
1192. Critical Connections in a Network
Hard
5.9K
174
Companies
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
"""

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize discovery and low arrays and the result list
        disc = [-1] * n
        low = [-1] * n
        self.time = 0
        bridges = []
        
        def dfs(node, parent):
            # Assign discovery time and low value
            disc[node] = self.time
            low[node] = self.time
            print(f"Visiting node {node}. Set discovery time to {disc[node]}")
            self.time += 1
                    
            for neighbor in graph[node]:
                # If neighbor is the parent, skip it
                if neighbor == parent:
                    continue
                # If neighbor is not visited, visit it
                if disc[neighbor] == -1:
                    dfs(neighbor, node)
                    # Propagate the low value to the parent node
                    low[node] = min(low[node], low[neighbor])
                    print(f"Backtracking to node {node}. Updated low value to {low[node]}")
                    # Check for a bridge
                    if disc[node] < low[neighbor]:
                        bridges.append([node, neighbor])
                        print(f"Found a bridge: {node} -> {neighbor}")
                # If neighbor is already visited, update the low value
                else:
                    low[node] = min(low[node], disc[neighbor])
                    print(f"Neighbor {neighbor} already visited. Updated low[{node}] to {low[node]}")

            
        # Start DFS from the first node (can start from any node as the graph is connected)
        dfs(0, -1)
        
        return bridges

if __name__ == '__main__':
    sol = Solution()
    print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])) # Expected: [[1,3]]
    print(sol.criticalConnections(2, [[0,1]]))                   # Expected: [[0,1]]
