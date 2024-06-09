def post_office(grid: list[list[int]], direction: str = "DR") -> int:
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    dp = [0] * (m + 1)

    row_range = range(n - 1, -1, -1) if direction in ["DR", "UL"] else range(n)

    for i in row_range:
        for j in range(m - 1, -1, -1):
            dp[j] = grid[i][j] + max(dp[j], dp[j + 1])

    return dp[0]
