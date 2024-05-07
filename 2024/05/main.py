def find_seats(seats: list[list[int]], n: int) -> int:
    rows, cols = len(seats), len(seats[0])
    groups = 0
    for r in range(rows):
        prev = -1
        for c in range(cols):
            if seats[r][c] == 1:
                groups += max(0, c - prev - n)
                prev = c
        groups += max(0, cols - prev - n)
    return groups
