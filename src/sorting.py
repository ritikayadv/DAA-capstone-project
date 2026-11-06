
def merge_sort(items, key):
    """Stable merge sort. Returns a new sorted list."""
    if len(items) <= 1:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], key)
    right = merge_sort(items[mid:], key)
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

def priority_rank(priority):
    return {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}.get(priority, 4)

def prioritize_parcels(parcels):
    # Earlier deadline first; priority breaks ties; lower weight breaks further ties.
    return merge_sort(
        parcels,
        key=lambda p: (p["deadline"], priority_rank(p["priority"]), float(p["weight"]))
    )
