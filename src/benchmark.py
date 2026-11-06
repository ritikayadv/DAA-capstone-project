
import random, time
from .sorting import prioritize_parcels
from .knapsack import knapsack_01
from .graph import dijkstra

def synthetic_parcels(n, seed=42):
    rng = random.Random(seed)
    priorities = ["Critical","High","Medium","Low"]
    return [{
        "parcel_id": f"S{i:04d}",
        "item": "Synthetic",
        "destination": "D" + str(rng.randint(1, 20)),
        "deadline": f"2026-10-{rng.randint(7,28):02d}",
        "priority": rng.choice(priorities),
        "weight": str(rng.randint(1, 15)),
        "value": str(rng.randint(1000, 100000)),
        "volume": str(rng.randint(1, 8))
    } for i in range(n)]

def synthetic_graph(n, seed=42):
    rng = random.Random(seed)
    nodes = [f"N{i}" for i in range(n)]
    g = {u: [] for u in nodes}
    # Ring guarantees connectivity.
    for i in range(n):
        a, b = nodes[i], nodes[(i+1) % n]
        w = rng.randint(1, 20)
        g[a].append((b, w)); g[b].append((a, w))
    # Additional random edges.
    for _ in range(max(n, 2*n)):
        a, b = rng.sample(nodes, 2)
        w = rng.randint(1, 30)
        g[a].append((b, w))
        g[b].append((a, w))
    return g

def benchmark():
    rows = []
    for n in [10, 50, 100, 200, 500]:
        parcels = synthetic_parcels(n)
        t0 = time.perf_counter(); prioritize_parcels(parcels); t1 = time.perf_counter()
        # Keep knapsack capacity moderate for scalable experiments.
        t2 = time.perf_counter(); knapsack_01(parcels[:min(n, 60)], 100); t3 = time.perf_counter()
        g = synthetic_graph(n)
        t4 = time.perf_counter(); dijkstra(g, "N0"); t5 = time.perf_counter()
        rows.append({
            "input_size": n,
            "sorting_ms": (t1-t0)*1000,
            "knapsack_ms": (t3-t2)*1000,
            "dijkstra_ms": (t5-t4)*1000
        })
    return rows
