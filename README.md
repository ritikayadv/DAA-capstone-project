
# Mini-Courier Planner

**Capstone Assignment – B.Tech | Integrated Algorithms Project**

## 1. Overview
Mini-Courier Planner is a modular Python prototype that combines:
1. Merge Sort for parcel prioritization.
2. 0/1 Knapsack Dynamic Programming for truck/package selection.
3. Dijkstra's algorithm for shortest paths.
4. Nearest-Neighbor TSP approximation for the overall delivery route.
5. Runtime benchmarking for scalability analysis.

The design follows the five phases specified in the capstone assignment: planning, package prioritization/box filling, route making/graph processing, performance testing, and final reporting.

## 2. Project Structure
```text
Mini-Courier-Planner/
├── main.py
├── run_benchmark.py
├── generate_charts.py
├── mini_courier_planner.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── sorting.py
│   ├── knapsack.py
│   ├── graph.py
│   └── benchmark.py
├── datasets/
│   ├── parcels.csv
│   └── routes.csv
├── images/
│   ├── runtime_comparison.png
│   ├── sorting_ms.png
│   ├── knapsack_ms.png
│   ├── dijkstra_ms.png
│   └── route_visualization.png
├── outputs/
│   └── runtime_results.csv
└── docs/
    └── Capstone_Report.md
```

## 3. Installation
Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
```

## 4. Run the application
```bash
python main.py
```

## 5. Run performance testing
```bash
python run_benchmark.py
python generate_charts.py
```

## 6. Run the notebook
```bash
jupyter notebook mini_courier_planner.ipynb
```

## 7. Algorithm Summary

| Module | Algorithm | Purpose | Complexity |
|---|---|---|---|
| Prioritization | Merge Sort | Sort by deadline, priority and weight | O(n log n) |
| Packing | 0/1 Knapsack DP | Maximize parcel value within capacity | O(nW) |
| Shortest path | Dijkstra | Find minimum distance between two nodes | O((V+E) log V) with heap |
| Route planning | Nearest Neighbor TSP | Approximate a multi-stop route | O(k²) after shortest-path preprocessing |

Here, `n` is the number of parcels, `W` is truck capacity, and `V/E` are graph vertices/edges.

## 8. GitHub Submission
Create a private repository and push this project. Then tag the final commit exactly as:

```bash
git add .
git commit -m "Final Mini-Courier Planner submission"
git tag v1.0-final-submission
git push origin main --tags
```

Submit the repository URL through the LMS/Zosima portal.

## 9. Academic Note
This project is an educational prototype. The route coordinates used for the visualization are schematic; route distances themselves come from the weighted graph dataset. The TSP method is intentionally a nearest-neighbor approximation, as required by the assignment.
