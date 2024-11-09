# November Monthly Challenge

_Countdown_

This month, you'll be recreating the game show Countdown. You will be given a sequence of integers, and a target number. You must determine what equation using the integers provided will produce the closest number to the target number.
When given the following input: `(1, 2, 3), 7`, the ideal output would be `"1+2*3"` (7) (~~P~~EDMAS applies here, but no parentheses allowed!). If the target number is `8`, the ideal output is still 7: `"1+2*3"`, since getting to a 9 would involve parentheses: `"3*(1+2)"`.
The operators you're allowed to use are `+`, `-`, `*`, `/`, and `^`, and you must use ALL of the integers provided.
Your output must produce whole numbers (no decimals).

Your code should contain a `countdown` function that takes 2 arguments, the sequence of numbers and the target number, and returns a string containing your output.

```python
def countdown(numbers: tuple[int, ...], target: int) -> str:
    ...
```

### Your test cases:

Since the actual output can be in whatever format you want as long as the equation is valid and boils down to (one of) the closest number(s), I'll just be providing the correct number(s) here.
You can use `eval` on your outputs for testing, but don't forget to remove the tests before submitting!
`eval(countdown(test_input)) in test_output` should do the trick.

The result of your code should be **one of** the results listed for each case.

1. `(1,2), 3` -> `(3,)` (1+2)
2. `(1,2), 2` -> `(2,)` (1\*2)
3. `(3,3,1), 8` -> `(8,)` (3\*3-1)
4. `(3,3,1), 25` -> `(26,)` (3^3-1)
5. `(10,4,5), 5` -> `(2,8)` (5\*4/10 OR 4\*5/10)

### Bonus Challenges:

1. No imports
2. No brute forcing equations to find the right one
