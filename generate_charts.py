
from pathlib import Path
import csv
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, str(Path(__file__).parent))
from src.data_loader import load_graph
from src.graph import nearest_neighbor_tsp
from src.data_loader import load_parcels
from src.sorting import prioritize_parcels
from src.knapsack import knapsack_01

ROOT = Path(__file__).parent
IMG = ROOT / "images"
OUT = ROOT / "outputs"
IMG.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

# Runtime chart
rows=[]
with open(OUT/"runtime_results.csv", newline="", encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
x=[int(r["input_size"]) for r in rows]
for col, label in [("sorting_ms","Merge Sort"),("knapsack_ms","Knapsack DP"),("dijkstra_ms","Dijkstra")]:
    y=[float(r[col]) for r in rows]
    plt.figure(figsize=(7,4.5))
    plt.plot(x,y,marker="o",label=label)
    plt.xlabel("Input size")
    plt.ylabel("Runtime (ms)")
    plt.title(f"Runtime of {label}")
    plt.grid(True, alpha=.3)
    plt.tight_layout()
    plt.savefig(IMG/f"{col}.png", dpi=160)
    plt.close()

# Combined runtime comparison
plt.figure(figsize=(8,5))
for col,label in [("sorting_ms","Merge Sort"),("knapsack_ms","Knapsack DP"),("dijkstra_ms","Dijkstra")]:
    plt.plot(x,[float(r[col]) for r in rows],marker="o",label=label)
plt.xlabel("Input size")
plt.ylabel("Runtime (ms)")
plt.title("Mini-Courier Planner Runtime Comparison")
plt.legend()
plt.grid(True, alpha=.3)
plt.tight_layout()
plt.savefig(IMG/"runtime_comparison.png", dpi=180)
plt.close()

# Route visualization (schematic coordinates for sample Delhi-NCR graph)
coords={"Warehouse":(0,0),"Delhi":(2,5),"Gurgaon":(6,4),"Noida":(7,1),"Faridabad":(3,-2),"Ghaziabad":(8,4)}
parcels=load_parcels(ROOT/"datasets/parcels.csv")
graph=load_graph(ROOT/"datasets/routes.csv")
ordered=prioritize_parcels(parcels)
selected,_,_,_=knapsack_01(ordered,25)
dest=list(dict.fromkeys(p["destination"] for p in selected))
route,total,_=nearest_neighbor_tsp(graph,"Warehouse",dest)

plt.figure(figsize=(8,6))
for node,(xx,yy) in coords.items():
    plt.scatter(xx,yy,s=120)
    plt.text(xx+0.15,yy+0.15,node,fontsize=9)
for a,b in zip(route,route[1:]):
    xa,ya=coords[a]; xb,yb=coords[b]
    plt.annotate("",xy=(xb,yb),xytext=(xa,ya),arrowprops=dict(arrowstyle="->",lw=1.8))
plt.title(f"Nearest-Neighbor Delivery Route ({total:.1f} km)")
plt.axis("off")
plt.tight_layout()
plt.savefig(IMG/"route_visualization.png",dpi=180)
plt.close()

print("Charts and route visualization generated in images/.")
