# May Monthly Challenge

_Movie Theatre_

You and your friends want to watch a movie. There are `N` of you, and you need to find seats! The online seating portal displays a 2D list of 0s and 1s, where 1 indicates the seat is taken:

```
[[1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 1],
[1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 0, 0]]
```

Given the 2D list, how many places are there where `N` of you can sit?

Your code should contain a `find_seats` function that takes 2 arguments, the seating arrangement and how many of you there are, and returns the amount of places your group can sit.

```python
def find_seats(seats: list[list[int]], n: int) -> int:
    ...
```

Your test cases:

1. `([[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0]], 2)` -> `2`
2. `([[1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0],[0, 0, 1, 1, 1, 1, 1],[1, 0, 1, 1, 0, 0, 1],[1, 1, 1, 0, 1, 0, 1],[0, 1, 1, 1, 1, 0, 0]], 2)` -> `3`
3. `([[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0]], 7)` -> `1`

Bonus Challenges:

1. Find the best seats for you and your friends, where the perfect seats are the direct center of the theatre, and your position is the center of your friend group (via taxicab geometry)
