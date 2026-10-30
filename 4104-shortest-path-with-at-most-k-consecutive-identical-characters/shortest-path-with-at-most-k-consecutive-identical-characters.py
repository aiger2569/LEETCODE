import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: adj[u] = list of (v, w)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        # dist[u][cnt] stores min weight to reach node u with 'cnt' consecutive labels[u]
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        # Priority queue stores tuples: (current_cost, u, count)
        pq = []
        
        # Base case: starting at node 0 with count 1
        dist[0][1] = 0
        heapq.heappush(pq, (0, 0, 1))
        
        while pq:
            d, u, cnt = heapq.heappop(pq)
            
            # Skip if we already found a shorter path to this state
            if d > dist[u][cnt]:
                continue
            
            # If we reached the target node n - 1, return the cost
            if u == n - 1:
                return d
            
            for v, w in adj[u]:
                # Calculate consecutive count for the neighbor
                next_cnt = cnt + 1 if labels[v] == labels[u] else 1
                
                # Check if it satisfies the constraint k
                if next_cnt <= k:
                    if d + w < dist[v][next_cnt]:
                        dist[v][next_cnt] = d + w
                        heapq.heappush(pq, (d + w, v, next_cnt))
                        
        return -1  # Return -1 if no valid path exists