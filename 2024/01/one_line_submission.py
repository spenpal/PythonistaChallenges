def binarify(time: str) -> str:
    return '\n'.join(''.join(line) for line in zip("  " + bin(int(time[0]))[2:].zfill(2), bin(int(time[1]))[2:].zfill(4), "    ", " " + bin(int(time[3]))[2:].zfill(3), bin(int(time[4]))[2:].zfill(4), "    ", " " + bin(int(time[6]))[2:].zfill(3), bin(int(time[7]))[2:].zfill(4)))

def clockify(bin_clock: str) -> str:
    return ''.join(str(int(num.strip(), 2)) if num.strip() else ':' for num in (''.join(line) for line in zip(*bin_clock.splitlines())))
