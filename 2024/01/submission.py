def binarify(time: str) -> str:
    hours, minutes, seconds = time.split(":")
    bin_time = (
        "  " + bin(int(hours[0]))[2:].zfill(2),
        bin(int(hours[1]))[2:].zfill(4),
        "    ",
        " " + bin(int(minutes[0]))[2:].zfill(3),
        bin(int(minutes[1]))[2:].zfill(4),
        "    ",
        " " + bin(int(seconds[0]))[2:].zfill(3),
        bin(int(seconds[1]))[2:].zfill(4),
    )
    bin_clock = "\n".join("".join(line) for line in zip(*bin_time))
    return bin_clock


def clockify(bin_clock: str) -> str:
    bin_time = tuple("".join(line) for line in zip(*bin_clock.splitlines()))
    time = "".join(str(int(num.strip(), 2)) if num.strip() else ":" for num in bin_time)
    return time
