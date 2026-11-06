
def knapsack_01(parcels, capacity):
    """0/1 knapsack maximizing parcel value under weight capacity.
    Returns selected parcels, total weight, total value and DP table.
    """
    n = len(parcels)
    weights = [int(float(p["weight"])) for p in parcels]
    values = [float(p["value"]) for p in parcels]
    cap = int(capacity)

    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i-1], values[i-1]
        for c in range(cap + 1):
            dp[i][c] = dp[i-1][c]
            if wt <= c:
                dp[i][c] = max(dp[i][c], dp[i-1][c-wt] + val)

    selected = []
    c = cap
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            selected.append(parcels[i-1])
            c -= weights[i-1]
    selected.reverse()

    total_weight = sum(int(float(p["weight"])) for p in selected)
    total_value = sum(float(p["value"]) for p in selected)
    return selected, total_weight, total_value, dp
