
import heapq

def dijkstra(graph, source):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0.0
    pq = [(0.0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

def reconstruct_path(prev, source, target):
    if source == target:
        return [source]
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == source:
            return path[::-1]
        cur = prev.get(cur)
    return []

def shortest_path(graph, source, target):
    dist, prev = dijkstra(graph, source)
    return reconstruct_path(prev, source, target), dist.get(target, float("inf"))

def nearest_neighbor_tsp(graph, start, nodes):
    """Greedy TSP approximation using Dijkstra distances between delivery points."""
    nodes = list(dict.fromkeys(nodes))
    if start not in nodes:
        nodes = [start] + nodes

    # All-pairs shortest paths among required nodes.
    all_dist = {}
    all_prev = {}
    for u in nodes:
        all_dist[u], all_prev[u] = dijkstra(graph, u)

    unvisited = set(nodes)
    unvisited.discard(start)
    route = [start]
    total = 0.0

    while unvisited:
        current = route[-1]
        nxt = min(unvisited, key=lambda x: all_dist[current].get(x, float("inf")))
        d = all_dist[current].get(nxt, float("inf"))
        if d == float("inf"):
            raise ValueError(f"No path between {current} and {nxt}")
        total += d
        route.append(nxt)
        unvisited.remove(nxt)

    # Return to warehouse.
    back = all_dist[route[-1]].get(start, float("inf"))
    if back == float("inf"):
        raise ValueError(f"No return path from {route[-1]} to {start}")
    total += back
    route.append(start)
    return route, total, all_dist
