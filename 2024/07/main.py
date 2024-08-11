CON_SEQS = "0123456789 9876543210"


def break_code(code: str) -> tuple[int, bool]:
    # Any string which doesn't have a consecutive sequence at the beginning,
    # or any string which has 4 of the same digits
    if code[:2] not in CON_SEQS:
        return int(max(code)), True

    # Any string which is fully consecutive
    if code in CON_SEQS:
        return 0, True

    return int(code[2] if code[:3] not in CON_SEQS else code[3]), False


def decipher(codes: list[str]) -> str:
    codes_len = len(codes)
    res = []
    i = -1

    while len(res) < 4:
        total = 0

        while True:
            i += 1
            code = codes[i % codes_len]
            num, break_flag = break_code(code)
            total += num
            if break_flag:
                break

        res.append(str(total % 10))

    return "".join(res)
