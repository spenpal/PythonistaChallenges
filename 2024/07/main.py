def break_code(code: tuple[int]) -> int | None:
    # Any string which has 4 of the same digits
    if code[0] == code[1] == code[2] == code[3]:
        return code[0]

    # Any string which doesn't have a consecutive sequence at the beginning
    if abs(code[0] - code[1]) != 1:
        return max(code)

    # Any string which is fully consecutive
    if (code[0] - code[1]) == (code[1] - code[2]) == (code[2] - code[3]):
        return 0

    return None


def decipher(codes: list[str]) -> str:
    codes_len = len(codes)
    codes = [tuple(map(int, code)) for code in codes]  # Convert codes to numbers
    res = []
    i = -1

    while len(res) < 4:
        total = 0

        while True:
            i += 1
            code = codes[i % codes_len]
            final = break_code(code)
            if final is not None:
                total += final
                break
            total += (
                code[3] if (code[0] + ((code[1] - code[0]) * 2) == code[2]) else code[2]
            )

        res.append(str(total % 10))

    return "".join(res)
