import heapq
class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edges(self, u, v, cost):
        self.edges.setdefault(u, {})[v] = cost
        self.edges.setdefault(v, {})[u] = cost

    def shortest_paths(self, start):
        dist = {node: float('inf') for node in self.edges}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, cost in self.edges[node].items():
                if d + cost < dist[neighbor]:
                    dist[neighbor] = d + cost
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return dist
    
graph = Graph()
graph.add_edges("A", "B", 1)
graph.add_edges("B", "C", 2)
graph.add_edges("A", "C", 4)

print("Shortest Distance from A", graph.shortest_paths("A"))
print("Shortest Distance from B", graph.shortest_paths("B"))
print("Shortest Distance from C", graph.shortest_paths("C"))
