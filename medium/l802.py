"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
"""
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe_nodes = []
        for idx in range(len(graph)):
            if graph[idx] == []:
                safe_nodes.append(idx)
        
        found_safe_nodes = set(safe_nodes)
        
        while safe_nodes:
            node = safe_nodes.pop()

            for idx in range(len(graph)):
                if node in graph[idx]:
                    graph[idx].remove(node)
                    if graph[idx] == []:
                        if idx not in found_safe_nodes:
                            found_safe_nodes.add(idx)
                            safe_nodes.append(idx)

        return sorted(list(found_safe_nodes))
    
    def eventualSafeNodesOptimized(self, graph: List[List[int]]) -> List[int]:
        incoming_nodes = [[] for _ in range(len(graph))]
        outgoing_edges_counter = [0 for _ in range(len(graph))]
        safe_nodes = []
        result = []

        for idx in range(len(graph)):
            for node in graph[idx]:
                incoming_nodes[node].append(idx)
                outgoing_edges_counter[idx] += 1

        for idx in range(len(graph)):
            if graph[idx] == []:
                safe_nodes.append(idx)
                result.append(idx)
        
        while(safe_nodes):
            node = safe_nodes.pop()

            for incoming_node in incoming_nodes[node]:
                outgoing_edges_counter[incoming_node] -= 1
                if outgoing_edges_counter[incoming_node] == 0:
                    safe_nodes.append(incoming_node)
                    result.append(incoming_node)
        
        return sorted(result)

            

if __name__ == '__main__':
    result_1 = Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
    print(result_1)

    result_2 = Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])
    print(result_2)

    assert Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6]
    assert Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4]