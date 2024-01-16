from pprint import pprint


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


def binarify_one_line(time: str) -> str:
    return "\n".join(
        "".join(line)
        for line in zip(
            "  " + bin(int(time[0]))[2:].zfill(2),
            bin(int(time[1]))[2:].zfill(4),
            "    ",
            " " + bin(int(time[3]))[2:].zfill(3),
            bin(int(time[4]))[2:].zfill(4),
            "    ",
            " " + bin(int(time[6]))[2:].zfill(3),
            bin(int(time[7]))[2:].zfill(4),
        )
    )


def clockify(bin_clock: str) -> str:
    bin_time = tuple("".join(line) for line in zip(*bin_clock.splitlines()))
    time = "".join(str(int(num.strip(), 2)) if num.strip() else ":" for num in bin_time)
    return time


def clockify_one_line(bin_clock: str) -> str:
    return "".join(
        str(int(num.strip(), 2)) if num.strip() else ":"
        for num in ("".join(line) for line in zip(*bin_clock.splitlines()))
    )


# binarify test cases
print(binarify("12:30:15") == " 0  0  0\n 0 00 01\n01 10 00\n10 10 11")
print(binarify("18:57:31") == " 1  0  0\n 0 11 00\n00 01 10\n10 11 11")
print(binarify("10:37:49") == " 0  0  1\n 0 01 10\n00 11 00\n10 11 01")
print(binarify("07:24:16") == " 0  0  0\n 1 01 01\n01 10 01\n01 00 10")
print()

print(binarify_one_line("12:30:15") == " 0  0  0\n 0 00 01\n01 10 00\n10 10 11")
print(binarify_one_line("18:57:31") == " 1  0  0\n 0 11 00\n00 01 10\n10 11 11")
print(binarify_one_line("10:37:49") == " 0  0  1\n 0 01 10\n00 11 00\n10 11 01")
print(binarify_one_line("07:24:16") == " 0  0  0\n 1 01 01\n01 10 01\n01 00 10")
print()

# clockify test cases
print(clockify(" 0  0  0\n 0 00 01\n01 10 00\n10 10 11") == "12:30:15")
print(clockify(" 1  0  0\n 0 11 00\n00 01 10\n10 11 11") == "18:57:31")
print(clockify(" 0  0  1\n 0 01 10\n00 11 00\n10 11 01") == "10:37:49")
print(clockify(" 0  0  0\n 1 01 01\n01 10 01\n01 00 10") == "07:24:16")
print()

print(clockify_one_line(" 0  0  0\n 0 00 01\n01 10 00\n10 10 11") == "12:30:15")
print(clockify_one_line(" 1  0  0\n 0 11 00\n00 01 10\n10 11 11") == "18:57:31")
print(clockify_one_line(" 0  0  1\n 0 01 10\n00 11 00\n10 11 01") == "10:37:49")
print(clockify_one_line(" 0  0  0\n 1 01 01\n01 10 01\n01 00 10") == "07:24:16")
print()
