from math import ceil


def find_seats(seats: list[list[int]], n: int) -> int:
    rows, cols = len(seats), len(seats[0])
    if not (1 <= n <= cols):
        return 0

    groups = 0
    for r in range(rows):
        prev = -1
        for c in range(cols):
            if seats[r][c] == 1:
                groups += max(0, c - prev - n)
                prev = c
        groups += max(0, cols - prev - n)
    return groups


def optimal_seats(seats: list[list[int]], n: int) -> tuple[int, int] | None:
    rows, cols = len(seats), len(seats[0])
    if not (1 <= n <= cols):
        return 0

    center = (len(seats) // 2, len(seats[0]) // 2)
    best_group, min_dist = None, float("inf")
    for r in range(rows):
        # Sliding window
        ones = seats[r][: n - 1].count(1)
        for i in range(cols - n + 1):
            ones += seats[r][i + n - 1] == 1

            if not ones:
                # Calculate distance to center
                pos = (r, i + ceil(n / 2) - 1)
                dist = abs(pos[0] - center[0]) + abs(pos[1] - center[1])
                if dist < min_dist:
                    min_dist = dist
                    best_group = pos

            ones -= seats[r][i] == 1

    return best_group
