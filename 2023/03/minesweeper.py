from pprint import pprint


def neighbor_mines(grid, r, c):
    return sum(
        1
        for i in range(max(0, r - 1), min(len(grid) - 1, r + 1) + 1)
        for j in range(max(0, c - 1), min(len(grid[0]) - 1, c + 1) + 1)
        if grid[i][j] == 1
    )


def minesweeper(grid: list[list[int]]) -> list[list[int]]:
    return [
        [
            9 if grid[r][c] == 1 else neighbor_mines(grid, r, c)
            for c in range(len(grid[0]))
        ]
        for r in range(len(grid))
    ]


# tests
test1 = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]
test2 = [[0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]

pprint(minesweeper(test1))
pprint(minesweeper(test2))

# import random

# # Define matrix dimensions
# num_rows = 1000
# num_cols = 1000

# # Generate matrix filled with random ones or zeroes
# matrix = [[random.randint(0, 1) for j in range(num_cols)] for i in range(num_rows)]
# minesweeper(matrix)
