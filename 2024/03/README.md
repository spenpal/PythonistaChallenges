# March monthly challenge

_sudoku but fast_

Your challenge this month is to build a program that will solve a sudoku grid. A standard 9x9 sudoku grid looks something like this:

```
3 9 7 | 4 6 2 | 8 5 1
8 2 6 | 5 1 7 | 3 4 9
4 5 1 | 3 8 9 | 7 2 6
------+-------+------
1 4 9 | 2 3 6 | 5 8 7
2 7 5 | 9 4 8 | 1 6 3
6 8 3 | 1 7 5 | 2 9 4
------+-------+------
7 6 4 | 8 5 3 | 9 1 2
5 1 2 | 7 9 4 | 6 3 8
9 3 8 | 6 2 1 | 4 7 5
```

And has 3 simple rules:

1. each _row_ must have each digit (1-9) exactly ONCE
2. each _column_ must have each digit (1-9) exactly ONCE
3. each 3x3 sub-grid must have each digit (1-9) exactly ONCE

The above grid is solved, but an unsolved grid will look like this:

```
3 0 0 | 4 0 2 | 8 0 1
0 2 0 | 5 0 0 | 0 0 9
0 0 0 | 0 8 0 | 7 2 0
------+-------+------
0 4 0 | 2 3 6 | 5 0 0
0 0 0 | 0 0 0 | 0 0 0
6 0 0 | 0 7 0 | 0 0 0
------+-------+------
0 6 0 | 0 0 3 | 9 1 2
0 0 2 | 0 9 0 | 0 3 8
0 0 8 | 0 0 0 | 0 0 0
```

Your code must replace all of the 0's with the correct digit (there is only one solution).

you will be given a 2-d list of ints, as shown below, and must replace all the 0's with the correct digit.
`[[3, 0, 0, 4, 0, 2, 8, 0, 1], [0, 2, 0, 5, 0, 0, 0, 0, 9], [0, 0, 0, 0, 8, 0, 7, 2, 0], [0, 4, 0, 2, 3, 6, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 7, 0, 0, 0, 0], [0, 6, 0, 0, 0, 3, 9, 1, 2], [0, 0, 2, 0, 9, 0, 0, 3, 8], [0, 0, 8, 0, 0, 0, 0, 0, 0]]`

your code must contain a `sudoku` function that takes 1 argument, the 2-d grid, and returns a solved 2-d grid.

```py
def sudoku(grid: list[list[int]]) -> list[list[int]]:
  ...
```

Your test cases:
Too long so i uploaded them to mystbin: <https://mystb.in/MediterraneanGatewayWalter>

There will be no bonuses this month (incl. onelining)
