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
        negative = False

        for side in self.piece[1:].split("@"):
            nums = []
            for char in side[1:]:
                if char == "-":
                    negative = True
                elif char.isdigit():
                    digit = int(char)
                    if negative:
                        digit = -digit
                        negative = False
                    nums.append(digit)
            sides[side[0]] = tuple(nums)

        lengths = list(map(len, sides.values()))
        if len(set(lengths)) == 1:
            self.length = lengths[0]

        return sides

    def validate(self) -> bool:
        # Missing side(s)
        if len(self.sides) != 4:
            return False
        # Not all sides have the same length
        if not self.length:
            return False
        # Parallel collision(s) detected
        for (left, right), (top, bottom) in zip(
            zip(self.sides["L"], self.sides["R"]), zip(self.sides["T"], self.sides["B"])
        ):
            if (left + self.length + right <= 0) or (top + self.length + bottom <= 0):
                return False
        return True

    def advanced_validate(self) -> bool:
        # Missing side(s)
        if len(self.sides) != 4:
            return False
        # Not all sides have the same length
        if not self.length:
            return False
        # Parallel collision(s) detected
        for (left, right), (top, bottom) in zip(
            zip(self.sides["L"], self.sides["R"]), zip(self.sides["T"], self.sides["B"])
        ):
            if (left + self.length + right <= 0) or (top + self.length + bottom <= 0):
                return False
        # Perpendicular collision(s) detected
        for idx, (left, right) in enumerate(
            zip(self.sides["L"], self.sides["R"]), start=1
        ):
            if left < 0 and (
                any(groove <= -idx for groove in self.sides["T"][:-left])
                or any(
                    groove <= -(self.length - idx + 1)
                    for groove in self.sides["B"][:-left]
                )
            ):
                return False
            if right < 0 and (
                any(groove <= -idx for groove in self.sides["T"][right:])
                or any(
                    groove <= -(self.length - idx + 1)
                    for groove in self.sides["B"][right:]
                )
            ):
                return False

        return True

    def __str__(self) -> str:
        if not self.length or len(self.sides) != 4:
            return "Cannot print invalid piece."

        empty, base, bump, groove = ".", "■", "▣", "□"
        max_side = 9
        max_length = self.length + max_side * 2

        # Create base grid
        grid = [
            ([empty] * max_side) + ([base] * self.length) + ([empty] * max_side)
            for _ in range(self.length)
        ]

        grid = (
            [[empty] * max_length for _ in range(max_side)]
            + grid
            + [[empty] * max_length for _ in range(max_side)]
        )

        # Add left and right bumps
        for idx, (left, right) in enumerate(
            zip(self.sides["L"], self.sides["R"]), start=max_side
        ):
            grid[idx][max_side - left : max_side] = [bump] * left
            grid[idx][max_side + self.length : max_side + self.length + right] = [
                bump
            ] * right

        # Add left and right grooves
        for idx, (left, right) in enumerate(
            zip(self.sides["L"], self.sides["R"]), start=max_side
        ):
            if left < 0:
                left = -left
                grid[idx][max_side : max_side + left] = [groove] * left
            if right < 0:
                right = -right
                grid[idx][max_side + self.length - right : max_side + self.length] = [
                    groove
                ] * right

        # Transpose grid
        grid = list(map(list, zip(*grid)))

        # Add top and bottom bumps
        for idx, (top, bottom) in enumerate(
            zip(self.sides["T"], self.sides["B"]), start=max_side
        ):
            grid[idx][max_side - top : max_side] = [bump] * top
            grid[idx][max_side + self.length : max_side + self.length + bottom] = [
                bump
            ] * bottom

        # Add top and bottom grooves
        for idx, (top, bottom) in enumerate(
            zip(self.sides["T"], self.sides["B"]), start=max_side
        ):
            if top < 0:
                top = -top
                grid[idx][max_side : max_side + top] = [groove] * top
            if bottom < 0:
                bottom = -bottom
                grid[idx][max_side + self.length - bottom : max_side + self.length] = [
                    groove
                ] * bottom

        # Transpose grid
        grid = list(map(list, zip(*grid)))

        return "\n".join("".join(row) for row in grid)


def sort(pieces: list[str]) -> list[str]:
    if not pieces:
        return []

    pieces = [Piece(piece) for piece in pieces]

    # Remove pieces that do not have the same length as the majority of the other pieces
    common_length = Counter(piece.length for piece in pieces).most_common(1)[0][0]
    pieces = [piece for piece in pieces if piece.length == common_length]

    # Remove invalid pieces
    return [piece.piece for piece in pieces if piece.validate()]


def advanced_sort(pieces: list[str]) -> list[str]:
    if not pieces:
        return []

    pieces = [Piece(piece) for piece in pieces]

    # Remove pieces that do not have the same length as the majority of the other pieces
    common_length = Counter(piece.length for piece in pieces).most_common(1)[0][0]
    pieces = [piece for piece in pieces if piece.length == common_length]

    # Remove invalid pieces
    return [piece.piece for piece in pieces if piece.advanced_validate()]
