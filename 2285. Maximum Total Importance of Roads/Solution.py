def maximumImportance(n: int, roads: list[list[int]]) -> int:
    count = [0] * n
    for u, v in roads:
        count[u] += 1
        count[v] += 1

    count.sort()
    ans = 0
    for i, c in enumerate(count, 1):
        ans += (i * c)

    return ans