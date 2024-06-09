# June Monthly Challenge

_Post Office_

The post office has a grid of mail boxes (represented as a 2D array of ints), and they would like to know how many letters they can pick from those mail boxes if they can only go down and to the right. You'll start at the top left of the grid and end at the bottom right. By only going down and to the right in the grid, you need to find the route that collects the most letters.

For example, if you have a mailbox grid like this:

```python
[
    [5, 2],
    [5, 2]
]
```

You start in the top left (5), and to collect the most letters, you'd go down (5), and then end in the bottom right (2). So the most letters you could collect here is 12 (5,5,2).

Your code should contain a `post_office` function that takes 1 argument, the 2D array of ints, and returns the count of letters.

```python
def post_office(grid: list[list[int]]) -> int:
    ...
```

**Note: if your code involves editing the input array in any way, you must copy the array since timeit passes the same array on every iteration**

Your test cases:

1. `[[]]` -> `0`
2. `[[1]]` -> `1`
3. `[[5, 2], [5, 2]]` -> `12`
4. `[[9, 9, 9], [0, 0, 9], [0, 0, 9]]` -> `45`

Bonus Challenges:

1. Add an argument to your `post_office` function that modifies the directions taken by your program. It should default to "DR"
   Your program will need to figure out the starting point based on the directions provided so that it travels from corner to corner.
   Eg. if you receive `DR` (the default, down and right), you'd travel from the top left to the bottom right.
   If you receive `UL` (up and left), you'd travel from the top right to the bottom left.
    ```python
    def post_office(grid: list[list[int]], direction: str = "DR") -> int:
        ...
    ```
