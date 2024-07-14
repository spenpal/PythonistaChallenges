def break_code(code: tuple[int]) -> int | None:
    # No possible consecutive sequence
    if abs(code[0] - code[1]) != 1:
        return max(code)

    # Check for all numbers being the same
    if code[0] == code[1] == code[2] == code[3]:
        return code[0]

    # Check for full consecutive sequence
    if (
        abs(code[0] - code[1]) == 1
        and abs(code[1] - code[2]) == 1
        and abs(code[2] - code[3]) == 1
    ):
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
                break
            total += code[2] if abs(code[2] - code[1]) != 1 else code[3]

        total += final
        res.append(str(total % 10))

    return "".join(res)
