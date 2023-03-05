# March Monthly Challenge
## *Cover Up A Minesweeper Grid*

Your challenge this month is to take a minesweeper grid, which is a 2-D list of zeros and ones (where one means theres a mine, and zero means an empty space), and output another grid where each position contains the amount of neighbouring mines. If the position is a mine, the number outputted should be `9`.

eg, an input like this:
```python
[
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]
```
would output a grid like this:
```python
[
  [1, 9, 2, 1],
  [2, 3, 9, 2],
  [3, 9, 4, 9],
  [9, 9, 3, 1]
]
```

Your entry should contain a `minesweeper` function, which takes the initial grid, and outputs the new grid with the proximities.
```python
def minesweeper(grid: list[list[int]]) -> list[list[int]]:
    ...
```

The only available extra challenge will be to one-line.

An additional test:
```python
in:
[
  [0, 0, 0, 1],
  [0, 1, 0, 0],
  [1, 0, 0, 0],
  [0, 0, 1, 0]
]
out:
[
  [1, 1, 2, 9],
  [2, 9, 2, 1],
  [9, 3, 2, 1],
  [1, 2, 9, 1]
]
```

Submissions will close at the end of March!

