# September Monthly Challenge

_Solve the puzzle_

After spending a month unmixing the pieces of the puzzles, your boss wants you to assemble the puzzles. You'll need to take the puzzles from last month, and solve the puzzles. You'll be receiving the mixed up inputs from last month (though not necessarily the same ones), so you'll need to use your sorting algorithm again.

A piece matches another when opposing edges (eg the top of one piece and the bottom of the other) are opposites of each other.
Using the example piece from part 1, the top of the piece (`0 0 1 2 2 3 2 0`) would match a piece with the following bottom: `0 0 -1 -2 -2 -3 -2 0`.

Take note of the following:

-   All pieces are oriented correctly, you will not need to rotate any pieces.
-   Any piece with an entire side that is completely zeroed should be considered an edge piece, and that edge will not have a counterpart.
-   Taking feedback from last month, the test case pieces will be the same on the input and output.
-   While the order of the output didn't matter last month, it does this month for obvious reasons.

Take the following two pieces (horizontal only). The piece on the left has a jut of 2 and a jut of 1. The piece on the right has the opposite feature, therefor it fits.

```
     0 0 0 2 0 0                     0 0 0 1 0 0
     0         0                     0         0
 # # 2         2 # #                -2# #      3 # # #
     0         1 #                  -1#        1 #
     0         0                     0         0
     0 0 3 1 0 0                     0 0-3 0 0 0
```

Now, if we were to add the verticals into consideration, we'd need to check that the verticals _and_ horizontal edges match

```
     0 0 0 2 0 0                     0 0 0 1 0 0                     0 0 0 3 0 0
     0         0                     0         0                     0         0
 # # 2         2 # #                -2# #$     2 # #                -2# #      2 # #
     0         1 #                  -1#  $     1 #                  -1#        1 #
     0         0                     0   $     0                     0         0
     0 0 3 1 0 0                     0 0-3 0 0 0                     0 0 2 0 0 0
         $ $                                                             $
         $                                                               $
         $                                                               $
                                                                         $
     0 0-3-1 0 0                     0 0-2 0 0 0                     0 0 3 0 0 0
     0   $ $   0                     0   $     0                     0         0
    -1#  $     3 # # #              -3# #$#    1 #                  -1#        0
    -2# #$ $   2 # #                -2# #      1 #                  -1#     # -1
     0     $   0                     0         0                     0   $     0
     0 0 0-2 0 0                     0 0-4-3 0 0                     0 0-1 0 0 0
```

-# Note that this is not a full puzzle, which is why the edges are not zeros

Now, the middle top piece doesn't fit with the piece below it. But if we swap the middle and right top pieces, everything fits:

```
     0 0 0 2 0 0                     0 0 0 1 0 0                     0 0 0 3 0 0
     0         0                     0         0                     0         0
 # # 2         2 # #                -2# #      2 # #                -2# #$     2 # #
     0         1 #                  -1#        1 #                  -1#  $     1 #
     0         0                     0         0                     0   $     0
     0 0 3 1 0 0                     0 0 2 0 0 0                     0 0-3 0 0 0
         $ $                             $
         $                               $                               $
         $                                                               $
                                                                         $
     0 0-3-1 0 0                     0 0-2 0 0 0                     0 0 3 0 0 0
     0   $ $   0                     0   $     0                     0         0
    -1#  $     3 # # #              -3# #$#    1 #                  -1#        0
    -2# #$ $   2 # #                -2# #      1 #                  -1#     # -1
     0     $   0                     0         0                     0   $     0
     0 0 0-2 0 0                     0 0-4-3 0 0                     0 0-1 0 0 0
```

Once you've assembled the puzzle, you will arrange it into a single list, one row at a time from top to bottom (**not a 2d list**).

Your code should contain a `solve` function that takes 1 argument, a list of encoded puzzle pieces, and returns a list of valid pieces in the same format.

```python
def solve(pieces: list[str]) -> list[str]:
    ...
```

Your test cases:
https://mystb.in/2251325b9ec78a3f02
