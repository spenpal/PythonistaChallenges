from collections import Counter


class Piece:
    def __init__(self, piece: str) -> None:
        self.piece = piece
        self.length = None
        self.sides = self.parse()

    def parse(self) -> dict:
        if not self.piece:
            self.length = 0
            return {}

        sides = {}
        for side in self.piece[1:].split("@"):
            nums = []
            negative = False
            for char in side[1:]:
                if char == "-":
                    negative = True
                elif char.isdigit():
                    digit = int(char)
                    nums.append(-digit if negative else digit)
                    negative = False
            sides[side[0]] = tuple(nums)

        lengths = set(map(len, sides.values()))
        self.length = lengths.pop() if len(lengths) == 1 else None
        return sides

    def validate(self, advanced=False) -> bool:
        # Missing side(s) or not all sides have the same length
        if len(self.sides) != 4 or not self.length:
            return False

        L, R, T, B = self.sides["L"], self.sides["R"], self.sides["T"], self.sides["B"]
        length = self.length

        for row in range(length):
            left, right, top, bottom = L[row], R[row], T[row], B[row]
            # Parallel cut(s) detected
            if (left + length + right <= 0) or (top + length + bottom <= 0):
                return False

            if advanced:
                for col in range(length):
                    intersect = (
                        (left < -col)
                        + (right < -(length - col - 1))
                        + (T[col] < -row)
                        + (B[col] < -(length - row - 1))
                    )
                    # Perpendicular cut(s) detected
                    if intersect > 1:
                        return False

        return True

    def __str__(self) -> str:
        if len(self.sides) != 4 or not self.length:
            return "Cannot print invalid piece."

        empty, base, bump, groove = ".", "■", "▣", "□"
        max_side = 9
        max_length = self.length + max_side * 2

        # Create base grid
        grid = [[empty] * max_length for _ in range(max_length)]
        length = self.length

        for idx in range(length):
            row_idx = idx + max_side
            grid[row_idx][max_side : max_side + length] = [base] * length

        L, R, T, B = self.sides["L"], self.sides["R"], self.sides["T"], self.sides["B"]

        # Add left/right bumps/grooves
        for idx, (left, right) in enumerate(zip(L, R), start=max_side):
            grid[idx][max_side - left : max_side] = [bump] * left
            grid[idx][max_side + length : max_side + length + right] = [bump] * right
            grid[idx][max_side : max_side - left] = [groove] * -left
            grid[idx][max_side + length + right : max_side + length] = [groove] * -right

        # Transpose grid
        grid = list(map(list, zip(*grid)))

        # Add top/bottom bumps/grooves
        for idx, (top, bottom) in enumerate(zip(T, B), start=max_side):
            grid[idx][max_side - top : max_side] = [bump] * top
            grid[idx][max_side + length : max_side + length + bottom] = [bump] * bottom
            grid[idx][max_side : max_side - top] = [groove] * -top
            grid[idx][max_side + length + bottom : max_side + length] = [
                groove
            ] * -bottom

        # Transpose grid
        grid = list(map(list, zip(*grid)))

        return "\n".join("".join(row) for row in grid)


def sort(pieces: list[str]) -> list[str]:
    if not pieces:
        return []

    pieces = [Piece(p) for p in pieces]
    common_length = Counter(p.length for p in pieces).most_common(1)[0][0]
    return [p.piece for p in pieces if p.length == common_length and p.validate()]


def advanced_sort(pieces: list[str]) -> list[str]:
    if not pieces:
        return []

    pieces = [Piece(p) for p in pieces]
    common_length = Counter(p.length for p in pieces).most_common(1)[0][0]
    return [
        p.piece
        for p in pieces
        if p.length == common_length and p.validate(advanced=True)
    ]
