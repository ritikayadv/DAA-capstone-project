
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

from src.data_loader import load_parcels, load_graph
from src.sorting import prioritize_parcels
from src.knapsack import knapsack_01
from src.graph import shortest_path, nearest_neighbor_tsp

ROOT = Path(__file__).parent
PARCEL_FILE = ROOT / "datasets" / "parcels.csv"
GRAPH_FILE = ROOT / "datasets" / "routes.csv"

def money(x):
    return f"₹{x:,.0f}"

def main():
    parcels = load_parcels(PARCEL_FILE)
    graph = load_graph(GRAPH_FILE)

    print("="*72)
    print("                 MINI-COURIER PLANNER")
    print("="*72)

    # Phase 2: sorting
    ordered = prioritize_parcels(parcels)
    print("\n[1] PARCEL PRIORITIZATION")
    print(f"{'ID':<5}{'Destination':<14}{'Deadline':<13}{'Priority':<10}{'Weight':>8}{'Value':>12}")
    for p in ordered:
        print(f"{p['parcel_id']:<5}{p['destination']:<14}{p['deadline']:<13}{p['priority']:<10}"
              f"{float(p['weight']):>8.1f}{money(float(p['value'])):>12}")

    # Phase 2: DP packing
    capacity = 25
    selected, total_weight, total_value, dp = knapsack_01(ordered, capacity)
    print("\n[2] OPTIMAL PACKING PLAN (0/1 KNAPSACK)")
    print(f"Truck capacity: {capacity} kg")
    print("Selected parcels:", ", ".join(p["parcel_id"] for p in selected))
    print(f"Total weight: {total_weight} kg")
    print(f"Total value : {money(total_value)}")
    print(f"DP table size: {len(dp)} x {len(dp[0])}")

    # Phase 3: shortest path example
    print("\n[3] DIJKSTRA SHORTEST PATH")
    path, dist = shortest_path(graph, "Warehouse", "Noida")
    print("Warehouse -> Noida:", " -> ".join(path), f"({dist:.1f} km)")

    # Phase 3: TSP approximation
    destinations = list(dict.fromkeys(p["destination"] for p in selected))
    route, route_length, _ = nearest_neighbor_tsp(graph, "Warehouse", destinations)
    print("\n[4] NEAREST-NEIGHBOR TSP APPROXIMATION")
    print("Delivery route:", " -> ".join(route))
    print(f"Total route length: {route_length:.1f} km")

    print("\n[5] FINAL RESULT")
    print(f"Parcels delivered: {len(selected)}/{len(parcels)}")
    print(f"Truck utilization: {total_weight/capacity*100:.1f}%")
    print(f"Route distance: {route_length:.1f} km")
    print("Planning pipeline: Sort -> Knapsack DP -> Dijkstra -> TSP Approximation")
    print("="*72)

if __name__ == "__main__":
    main()
