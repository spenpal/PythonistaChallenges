# August Monthly Challenge

_Puzzle Sorting_

This month, you've started a job at the puzzle factory! You arrive for your first day of work, and they give you your first task. Somehow the factory has mixed pieces from other puzzles into their puzzle generating algorithm, and they want you to sort them out. Your boss has some instructions for you to filter out bad pieces:

Each piece has a condensed form that looks like this: `@T00122320@L00-3-4-4-3-10@B02442001@R01442001`.
You can decode the condensed form to a proper piece knowing that an `@` precedes each section, along with a letter indicating which edge the section contains. The sections are marked as follows: @T section is the top, @B is the bottom, @L is the left, and @R is the right. They can appear in any order.
For example, a section that looks like `@B02442001` is the bottom edge, and each digit is a bump/groove in the piece (bumps/grooves will never be more than one digit). Positive numbers indicate an outwards bump, while negative numbers indicate an inwards groove (Note that the corners appear in both of the sides that touch that corner (the 1 appears at the end of both section R and section B)).

When decoded, the piece looks like this:

```
 0 0 1 2 2 3 2 0
 0             1
-3             4
-4             4
-4             2
-3             0
-1             0
 0 2 4 4 2 0 0 1
```

A piece should be discarded if any of the following is found:

-   The piece is missing a side
-   All sides of the piece are not of equal length
-   The size (length of the sides) of the piece is not the same as the majority of the other pieces
-   Opposite ends of the puzzle piece would collide (ex there are two -5s across from each other (either vertically or horizontally), when the piece size is only 8. An inward bump of -5 from both sides would simply cut the piece in half).
    -   This includes if one groove is larger or equal to the positive bump on the other side (a groove of -9 on the left with a corresponding bump of 1 on the piece size of 8 would still cut the piece in half), but not if the groove is smaller than the bump on the other side (a groove of -8 on the top with a corresponding bump of 3 would be OK). Horizontal and vertical collisions can be ignored.

Your code should contain a `sort` function that takes 1 argument, a list of encoded puzzle pieces, and returns a list of valid pieces in the same format.

```python
def sort(pieces: list[str]) -> list[str]:
    ...
```

Your test cases:
https://mystb.in/32f772d5891c6b569c

Bonus Challenges:

1. implement vertical/horizontal collisions under the function name `advanced_sort` (all other rules remain the same. This likely won't produce valid puzzles but is more just for fun)
