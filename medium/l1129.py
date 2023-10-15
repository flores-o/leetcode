"""
1129. Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n


Scratchpad:

0 -> 1 -> 2

red 
0: [1]
1:  [2]

start_blue []

   0  1  2 
0  0  1  0
1  
2

start_red 

   0  1  2 
0
1
2


"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        shortest_path_ending_in_red = [[ -1 for _ in range(n) ] for _ in range(n)]
        shortest_path_ending_in_blue = [[ -1 for _ in range(n) ] for _ in range(n)]

        shortest_path_ending_in_red[0][0] = 0
        shortest_path_ending_in_blue[0][0] = 0

        # build neighbor list
        red_neighbors = [ [] for _ in range(n) ]
        blue_neighbors = [ [] for _ in range(n) ]

        for edge in redEdges:
            red_neighbors[edge[0]].append(edge[1])

        for edge in blueEdges:
            blue_neighbors[edge[0]].append(edge[1])	

        red_queue = [0]
        blue_queue = [0]

        while len(red_queue) > 0 or len(blue_queue) > 0:
            if len(red_queue) > 0:
                node = red_queue.pop(0)
                for neighbor in blue_neighbors[node]:
                    if shortest_path_ending_in_red[0][node] != -1:
                        shortest_path_ending_in_blue[0][neighbor] = shortest_path_ending_in_red[0][node] + 1
                    blue_queue.append(neighbor)
            if len(blue_queue) > 0:
                node = blue_queue.pop(0)
                for neighbor in red_neighbors[node]:
                    if shortest_path_ending_in_blue[0][node] != -1:
                        shortest_path_ending_in_red[0][neighbor] = shortest_path_ending_in_blue[0][node] + 1
                    red_queue.append(neighbor)
        
        result = []
        for i in range(n):
            if shortest_path_ending_in_red[0][i] == -1 and shortest_path_ending_in_blue[0][i] == -1:
                result.append(-1)
            elif shortest_path_ending_in_red[0][i] == -1:
                result.append(shortest_path_ending_in_blue[0][i])
            elif shortest_path_ending_in_blue[0][i] == -1:
                result.append(shortest_path_ending_in_red[0][i])
            else:
                result.append(min(shortest_path_ending_in_red[0][i], shortest_path_ending_in_blue[0][i]))
        return result
                        