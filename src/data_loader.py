
import csv
from pathlib import Path

def load_parcels(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_graph(path):
    graph = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            u, v = row["source"], row["destination"]
            w = float(row["distance_km"])
            graph.setdefault(u, []).append((v, w))
    return graph
