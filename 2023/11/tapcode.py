def convert(value: str) -> str:
    """
    Base Solution
    """
    if not value:
        return ""

    if value[0] == ".":  # convert tap code to word
        parts = value.split()
        res = []
        for idx in range(0, len(parts), 2):
            row, col = len(parts[idx]) - 1, len(parts[idx + 1]) - 1
            pos = row * 5 + col  # relative position to "a"
            pos += pos >= 10  # adjust for "k"
            let = chr(ord("a") + pos)
            res.append(let)
        return "".join(res)
    else:  # convert word to tap code
        res = []
        for let in value.lower():
            match let:
                case "k":
                    row, col = 0, 2
                case _ if let >= "l":  # adjust for "k"
                    row, col = divmod(ord(let) - ord("a") - 1, 5)
                case _:
                    row, col = divmod(ord(let) - ord("a"), 5)
            res.append("." * (row + 1) + " " + "." * (col + 1))
        return " ".join(res)


def convert(value: str) -> str:
    """
    Minified Base Solution
    """
    if not value:
        return ""

    if value[0] == ".":  # convert tap code to word
        parts = value.split()
        return "".join(
            chr(
                ord("a")
                + (len(parts[i]) - 1) * 5
                + (len(parts[i + 1]) - 1)
                + (len(parts[i]) - 1 >= 2)
            )
            for i in range(0, len(parts), 2)
        )

    # convert word to tap code
    return " ".join(
        "." * (row + 1) + " " + "." * (col + 1)
        for let in value.lower()
        for row, col in [
            (0, 2)
            if let == "k"
            else divmod(ord(let) - ord("a") - 1, 5)
            if let >= "l"
            else divmod(ord(let) - ord("a"), 5)
        ]
    )


def convert(value: str) -> str:
    """
    Bonus Challenge Solution
    """
    if not value:
        return ""

    if value[0] == ".":  # convert tap code to word
        idx = 0
        res = ""
        while idx < len(value):
            row = col = -1
            while value[idx] == ".":
                row += 1
                idx += 1
            idx += 1
            while idx < len(value) and value[idx] == ".":
                col += 1
                idx += 1
            idx += 1
            pos = row * 5 + col
            pos += pos >= 10
            let = chr(ord("a") + pos)
            res += let
        return res
    else:  # convert word to tap code
        res = ""
        for let in value.lower():
            match let:
                case "k":
                    row, col = 0, 2
                case _ if let >= "l":  # adjust for "k"
                    row, col = divmod(ord(let) - ord("a") - 1, 5)
                case _:
                    row, col = divmod(ord(let) - ord("a"), 5)
            res += "." * (row + 1) + " " + "." * (col + 1) + " "
        return res[:-1]


# Test Cases
print(convert("BREAK"))  # . .. .... .. . ..... . . . ...
print(
    convert("greeting")
)  # .. .. .... .. . ..... . ..... .... .... .. .... ... ... .. ..
print(convert("ankle"))  # . . ... ... . ... ... . . .....
print(convert(".... .... ... .... ... ... .. .... .. .. .. ... .... ...."))  # tonight
print(convert(". . .. . .. . .. .... ... ... .. .... .... .... ..... ...."))  # affinity
