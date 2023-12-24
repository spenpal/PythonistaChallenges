import re
from pprint import pprint


def parse(original_map: str) -> list[list[int]]:
    m = []
    for line in original_map.splitlines():
        line = re.sub(
            r"[^\.ST]", "", line
        )  # remove everything, except periods and letters
        if line:
            m.append(line)
    return m


def create_map(original_map: str) -> list[list[int]]:
    # Parse the original map into a 2D list
    m = parse(original_map)

    # Find coordinates of sensors and tags
    sensors, tags = [], []
    for i, line in enumerate(m):
        for j, char in enumerate(line):
            if char == "S":
                sensors.append((i, j))
            elif char == "T":
                tags.append((i, j))

    # Find the closest tag for each sensor (using Manhattan distance)
    pairs = [
        (
            sensor,
            min(
                tags, key=lambda tag: abs(sensor[0] - tag[0]) + abs(sensor[1] - tag[1])
            ),
        )
        for sensor in sensors
    ]

    # Replace entire map with 1's
    m = [[1 for _ in line] for line in m]

    # Find dead zones using Taxicab geometry and fill dead zones with 0's
    for sensor, tag in pairs:
        xd, yd = sensor[0] - tag[0], sensor[1] - tag[1]
        radius = abs(xd) + abs(yd)

        # Fill in dead zones line by line, starting from the center. Ensure you are still in bounds of the map.
        x, y = sensor
        for i, length in enumerate(range(radius * 2 + 1, 0, -2)):
            row_top, row_bottom = max(x - i, 0), min(x + i, len(m) - 1)
            left, right = max(y - length // 2, 0), min(y + length // 2 + 1, len(m[0]))
            m[row_top][left:right] = [0] * length
            m[row_bottom][left:right] = [0] * length

    return m


def print_map(m: str, commas: bool = True):
    # Print 2D list with only elements
    # print("\n".join(["".join(map(str, line)) for line in m]))

    # Print 2D list in nested format, with choice of commas or not
    sep = "," if commas else ""
    print(
        "[\n"
        + "\n".join(["  [" + sep.join(map(str, line)) + "]" for line in m])
        + "\n]"
    )

    # Print 2D list compactly
    # pprint(m, compact=True, width=len(f"{m[0]}") + 2)


with open("input.txt") as f:
    original_map = f.read()
    final_map = create_map(original_map)
    print_map(final_map)
