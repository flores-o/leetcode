"""
1. Queue containing root

Pop node from queue
2. 
Add to the queue the inNodes, and outNodes of the current Node.
Mark the node as visited when adding to the queue

Add the node only if not visited 

If outNode, increment count.


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

"""
from typing import List

class Solution:
    def createInOutNeighbours(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        in_neighbours = [ [] for _ in range(n) ]
        out_neighbours = [ [] for _ in range(n) ]

        for connection in connections:
            out_neighbours[connection[0]].append(connection[1])
            in_neighbours[connection[1]].append(connection[0])

        return in_neighbours, out_neighbours
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 1. Queue containing root
        queue = [0]
        visited = {0}
        count = 0

        # 2. Pop node from queue
        while queue:
            current = queue.pop(0)

            #3. Add to the queue the inNodes, and outNodes of the current Node.
            in_neighbours, out_neighbours = self.createInOutNeighbours(n, connections)
            for neighbour in in_neighbours[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

            for neighbour in out_neighbours[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    count += 1
        
        return count

if __name__ == '__main__':
    assert(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3)
    assert(Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]]) == 2)
    assert(Solution().minReorder(3, [[1,0],[2,0]]) == 0)



