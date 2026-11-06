
from pathlib import Path
import sys, csv
sys.path.insert(0, str(Path(__file__).parent))
from src.benchmark import benchmark

ROOT = Path(__file__).parent
rows = benchmark()
out = ROOT / "outputs" / "runtime_results.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

print("Runtime benchmark completed.")
for r in rows:
    print(r)
print(f"Saved: {out}")
