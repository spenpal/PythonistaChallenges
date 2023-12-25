import re
def create_map(m):
    m, s, t = re.sub(r"[^\.ST\n]", "", m).strip().splitlines(), [], []
    [s.append((i, j)) if c == "S" else t.append((i, j)) if c == "T" else c for i, r in enumerate(m) for j, c in enumerate(r)]
    p = [(s, min(t, key=lambda x: abs(s[0] - x[0]) + abs(s[1] - x[1]))) for s in s]
    m = [[1 for _ in line] for line in m]
    [[m[r].__setitem__(c, 0) for c in range(le, ri)] for s, t in p for i, l in enumerate(range((abs(s[0] - t[0]) + abs(s[1] - t[1])) * 2 + 1, 0, -2)) for r in [max(s[0] - i, 0), min(s[0] + i, len(m) - 1)] for le, ri in [(max(s[1] - l // 2, 0), min(s[1] + l // 2 + 1, len(m[0])))]]
    return m

