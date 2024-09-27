from collections import Counter

OPPOSITE_SIDE = {"T": "B", "L": "R", "R": "L", "B": "T"}
DIRECTIONS = {"T": (-1, 0), "L": (0, -1), "R": (0, 1), "B": (1, 0)}


class Piece:
    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.length = None
        self.sides = self.parse()
        self.valid = self.validate()

    def parse(self) -> dict:
        if not self.raw:
            return {}

        sides = {}
        for side in self.raw[1:].split("@"):
            values, negative = [], False
            for char in side[1:]:
                if char == "-":
                    negative = True
                elif char.isdigit():
                    num = int(char)
                    values.append(-num if negative else num)
                    negative = False
            sides[side[0]] = tuple(values)

        lengths = set(map(len, sides.values()))
        self.length = lengths.pop() if len(lengths) == 1 else None
        return sides

    def validate(self) -> bool:
        # Missing side(s) or not all sides have the same length
        if len(self.sides) != 4 or not self.length:
            return False

        L, R, T, B = self.sides["L"], self.sides["R"], self.sides["T"], self.sides["B"]

        for row in range(self.length):
            left, right, top, bottom = L[row], R[row], T[row], B[row]
            # Parallel cut(s) detected
            if (left + self.length + right <= 0) or (top + self.length + bottom <= 0):
                return False

        return True

    def get_edges(self) -> str:
        return "".join(
            side for side in "TBLR" if self.sides.get(side) == (0,) * self.length
        )


def next_position(dims: tuple[int, int], position: tuple[int, int]) -> tuple[int, int]:
    rows, cols = dims
    x, y = position
    if y < cols - 1:
        return (x, y + 1)
    if x < rows - 1:
        return (x + 1, 0)
    return None


def get_valid_sides(
    grid: list[list[Piece]],
    dims: tuple[int, int],
    position: tuple[int, int],
    piece_length: int,
) -> dict[str, tuple]:
    valid_sides = {}
    rows, cols = dims
    x, y = position

    for side, (dr, dc) in DIRECTIONS.items():
        # Out of bounds = edge
        if not (0 <= x + dr < rows and 0 <= y + dc < cols):
            valid_sides[side] = (0,) * piece_length
        # Adjacent piece exists
        elif grid[x + dr][y + dc]:
            adjacent = grid[x + dr][y + dc]
            valid_sides[side] = tuple(
                -num for num in adjacent.sides[OPPOSITE_SIDE[side]]
            )

    return valid_sides


def backtrack(
    grid: list[list[Piece]],
    dims: tuple[int, int],
    position: tuple[int, int],
    pieces: set[Piece],
    piece_length: int,
) -> bool:
    if not (position or pieces):
        return True

    valid_sides = get_valid_sides(grid, dims, position, piece_length)
    candidates = [p for p in pieces if valid_sides.items() <= p.sides.items()]

    r, c = position
    for piece in candidates:
        grid[r][c] = piece
        pieces.discard(piece)
        if backtrack(grid, dims, next_position(dims, position), pieces, piece_length):
            return True
        pieces.add(piece)
        grid[r][c] = ""

    return False


def sort(pieces: list[str]) -> list[Piece]:
    if not pieces:
        return []

    pieces = [Piece(p) for p in pieces]
    common_length = Counter(p.length for p in pieces if p.length).most_common(1)[0][0]
    return [p for p in pieces if p.length == common_length and p.valid]


def solve(pieces: list[str]) -> list[str]:
    pieces = sort(pieces)
    if not pieces:
        return []

    rows = cols = 0
    for piece in pieces:
        edges = piece.get_edges()
        rows += "L" in edges
        cols += "T" in edges

    grid = [[""] * cols for _ in range(rows)]
    piece_length = pieces[0].length

    # Solve puzzle
    backtrack(grid, (rows, cols), (0, 0), set(pieces), piece_length)

    # Flatten grid
    return [p.raw for row in grid for p in row]
