# January monthly challenge
*binary clocks*

A binary clock is a clock that tells time using binary bits. Each digit in a normal time gets its own column, and the rows in each column represent a specific bit.
When you add the sum of the bits together, you get the current time for that digit.

E.g. 12:30:15 on a binary clock would look like this:
```
 0  0  0
 0 00 01
01 10 00
10 10 11
```
When you break that down, you're looking at a binary number in each column.
```
 0  0  0 <- 8
 0 00 01 <- 4
01 10 00 <- 2
10 10 11 <- 1
---------
12 30 15
```
Note that digits that can never be reached are removed, e.g. the 4 and 8 bits on the first column.

Your job is to make a program that converts digital clocks into binary clocks. Your program will be given a time in the format `HH:MM:SS` (e.g. `18:57:31`, note that these clocks use 24 hour time!). Your code will convert it to binary clock form
(e.g.
```
 1  0  0
 0 11 00
00 01 10
10 11 11
```
).

Your code should contain a `binarify` function that takes 1 argument, a time string, and returns a string containing the binary clock time:
```py
def binarify(time: str) -> str:
  ...
```

Your test cases:
1. `18:57:31` -> ` 1  0  0\n 0 11 00\n00 01 10\n10 11 11`
2. `10:37:49` -> ` 0  0  1\n 0 01 10\n00 11 00\n10 11 01`
3. `07:24:16` -> ` 0  0  0\n 1 01 01\n01 10 01\n01 00 10`

### Bonus challenges:
This month's bonus challenge is to write a `clockify` function that performs the opposite of the `binarify` function. It should take a binary time and convert it into the corresponding digits. Simply reverse the test cases.

As per usual, onelining is a bonus challenge.