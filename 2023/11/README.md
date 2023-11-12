# November monthly challenge
*tap codes*

Tap code is a morse code style cipher to turn a word into taps (represented in this challenge with `.`).
It is based on a 5x5 square, where the letter "K" is combined into the letter "C". 
The square looks like this:
```
   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
```
A letter is translated into its row and column numbers (in that order), with a pause in between (represented with a space).
As an example, the letter B would become `. ..`  (Row 1, Column 2).
Additionally, between each letter there is another space.
As an example, the word BREAK would become `. .. .... .. . ..... . . . ...`

### The challenge
Your task is to write a function that converts to **and** from tap code. If given a word or sentence, it should convert *to* tap code. If given tap code, it should convert *from* tap code.

Your entry should contain a `convert` function that takes one argument, the input string. It should return a string.
```py
def convert(value: str) -> str:
    ...
```

We will be judging on both performance *and* creativity of the solution.

This month has one bonus challenge:
- Don't use lists or dicts (or any subclass/variation of them. Eg. no OrderedDicts or deques).


### Test Cases
`"greeting" -> ".. .. .... .. . ..... . ..... .... .... .. .... ... ... .. .."`
`"ankle" -> ". . ... ... . ... ... . . ....."`
`".... .... ... .... ... ... .. .... .. .. .. ... .... ...." -> "tonight"`
`". . .. . .. . .. .... ... ... .. .... .... .... ..... ...." -> "affinity"`