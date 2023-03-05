def minesweeper(grid: list[list[int]]) -> list[list[int]]:
    return [
        [
            9
            if grid[r][c] == 1
            else sum(
                1
                for i in range(max(0, r - 1), min(len(grid) - 1, r + 1) + 1)
                for j in range(max(0, c - 1), min(len(grid[0]) - 1, c + 1) + 1)
                if (i, j) != (r, c) and grid[i][j] == 1
            )
            for c in range(len(grid[0]))
        ]
        for r in range(len(grid))
    ]
