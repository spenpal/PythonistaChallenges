# February Monthly Challenge
## *Crack The Pin*  
---
A keypad looks like this:
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

When spying on someone who punches in their keycode, you need to account for inaccuracies in what you saw. 
You know that what you've seen could be off by one key horizontally or vertically, but never diagonally.

Your task is to produce a full list of possibilities from the keys you saw pressed (your challenge input).

For example: if you were given an input of `"46"`
```python
# Instead of the 4 it could also be 1, 5, or 7.
# Instead of the 6 it could also be 3, 5, or 9.
>>> crack("46")
["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]
```


Your submission must have a crack function that takes one argument, the pin (as a string), and return a list with all the possible outcomes:
```python
def crack(pin: str) -> list[str]:
    ...
```

tests:
```python
crack_pincode("0") ➞ ["0", "8"]

crack_pincode("2") ➞ ["1", "2", "3", "5"]

crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]
```

We're going with an easier one to start off the year, so if you find this easy, consider the following challenges:
```
- one-line it
- do it in under 100 characters
- no dicts
- no imports
- all at once
```

Submissions close at the end of February!