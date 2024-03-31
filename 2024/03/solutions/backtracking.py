def valid_move(bitmasks: list[list[int]], row: int, col: int, num: int) -> bool:
    row_mask = bitmasks[0][row]
    col_mask = bitmasks[1][col]
    box_mask = bitmasks[2][((row // 3) * 3) + (col // 3)]

    num_mask = 1 << num
    return not (row_mask & num_mask or col_mask & num_mask or box_mask & num_mask)


def solve(grid: list[list[int]], bitmasks: list[list[int]]) -> bool:
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if valid_move(bitmasks, r, c, num):
                        grid[r][c] = num
                        num_mask = 1 << num
                        bitmasks[0][r] |= num_mask
                        bitmasks[1][c] |= num_mask
                        bitmasks[2][((r // 3) * 3) + (c // 3)] |= num_mask

                        if solve(grid, bitmasks):
                            return True

                        grid[r][c] = 0
                        bitmasks[0][r] &= ~num_mask
                        bitmasks[1][c] &= ~num_mask
                        bitmasks[2][((r // 3) * 3) + (c // 3)] &= ~num_mask
                return False
    return True


def sudoku(grid: list[list[int]]) -> list[list[int]]:
    """Backtracking.

    - Uses bit masks for O(1) checking
    """
    # Create bitmasks for rows, columns, and boxes.
    bitmasks = [[0] * 9 for _ in range(3)]  # [row_masks, col_masks, box_masks]
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                num_mask = 1 << grid[r][c]
                bitmasks[0][r] |= num_mask  # row_mask
                bitmasks[1][c] |= num_mask  # col_mask
                bitmasks[2][((r // 3) * 3) + (c // 3)] |= num_mask  # box_mask

    solved = solve(grid, bitmasks)
    return grid if solved else "No solution."
