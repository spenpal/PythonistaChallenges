from collections import defaultdict


def solve(
    grid: list[list[int]],
    zeros: list[tuple[int]],
    rows: defaultdict[set],
    cols: defaultdict[set],
    boxes: defaultdict[set],
) -> bool:
    if not zeros:
        return True

    # Sort zeros by the number of remaining candidates
    zeros.sort(
        key=lambda x: 9 - len(rows[x[0]] | cols[x[1]] | boxes[(x[0] // 3, x[1] // 3)])
    )

    r, c = zeros[0]
    candidates = set(range(1, 10)) - (rows[r] | cols[c] | boxes[(r // 3, c // 3)])

    for num in candidates:
        grid[r][c] = num
        rows[r].add(num)
        cols[c].add(num)
        boxes[(r // 3, c // 3)].add(num)

        if solve(grid, zeros[1:], rows, cols, boxes):
            return True

        grid[r][c] = 0
        rows[r].remove(num)
        cols[c].remove(num)
        boxes[(r // 3, c // 3)].remove(num)

    return False


def sudoku(grid: list[list[int]]) -> list[list[int]]:
    """Constraint satisfaction problem.

    - Uses Minimum Remaining Values (MRV) heuristic
    """
    # Find all locations of zero in the grid
    zeros = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]

    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            num = grid[r][c]
            if num == 0:
                continue
            rows[r].add(num)
            cols[c].add(num)
            boxes[(r // 3, c // 3)].add(num)

    solved = solve(grid, zeros, rows, cols, boxes)
    return grid if solved else "No solution"
