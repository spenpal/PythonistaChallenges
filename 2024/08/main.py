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

        # Parallel collision(s) detected
        for (left, right), (top, bottom) in zip(
            zip(self.sides["L"], self.sides["R"]), zip(self.sides["T"], self.sides["B"])
        ):
            if (left + self.length + right <= 0) or (top + self.length + bottom <= 0):
                return False

        # Perpendicular collision(s) detected
        if advanced:
            for idx, (left, right) in enumerate(
                zip(self.sides["L"], self.sides["R"]), start=1
            ):
                if (
                    left < 0
                    and (
                        any(num <= -idx for num in self.sides["T"][:-left])
                        or any(
                            num <= -(self.length - idx + 1)
                            for num in self.sides["B"][:-left]
                        )
                    )
                ) or (
                    right < 0
                    and (
                        any(num <= -idx for num in self.sides["T"][right:])
                        or any(
                            num <= -(self.length - idx + 1)
                            for num in self.sides["B"][right:]
                        )
                    )
                ):
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

        for idx in range(self.length):
            row_idx = idx + max_side
            grid[row_idx][max_side : max_side + self.length] = [base] * self.length

        # Add left/right bumps/grooves
        for idx, (left, right) in enumerate(
            zip(self.sides["L"], self.sides["R"]), start=max_side
        ):
            # Add bumps
            grid[idx][max_side - left : max_side] = [bump] * left
            grid[idx][max_side + self.length : max_side + self.length + right] = [
                bump
            ] * right

            # Add grooves
            grid[idx][max_side : max_side - left] = [groove] * -left
            grid[idx][max_side + self.length + right : max_side + self.length] = [
                groove
            ] * -right

        # Transpose grid
        grid = list(map(list, zip(*grid)))

        # Add top/bottom bumps/grooves
        for idx, (top, bottom) in enumerate(
            zip(self.sides["T"], self.sides["B"]), start=max_side
        ):
            # Add bumps
            grid[idx][max_side - top : max_side] = [bump] * top
            grid[idx][max_side + self.length : max_side + self.length + bottom] = [
                bump
            ] * bottom

            # Add grooves
            grid[idx][max_side : max_side - top] = [groove] * -top
            grid[idx][max_side + self.length + bottom : max_side + self.length] = [
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


def main():
    pieces = [
        "@T00000@L04300@B02410@R00000",
        "@B00000@T000-7-5@L00000@R00000",
        "@T00000@B03400@L00000@R0-4-300",
        "@R00100@T0-3-400@L00000@B00000",
        "@L000002054@R00000-5-512@B000003-231@T000002-24-4",
        "@L00-100@R00000@T0-2-4-10@B00000",
    ]
    for piece in pieces:
        p = Piece(piece)
        print(p.sides)
        print(p)


if __name__ == "__main__":
    main()
