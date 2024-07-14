# July Monthly Challenge

### Find the Code

You are stuck inside a bank; While attempting to steal your millions, the security systems activated. The only way out
is via a door with a pin-lock. You must successfully find the `4` digit pin.

You are given a list of strings (`list[str]`), with each string containing `4` integers each, between `0-9` inclusive. E.g. `1234`
Your task is to decipher the pin-code (also a `4` digit string between `0-9` inclusive) needed to break out of the bank. To do this you will need to cycle through the given strings
and look for clues.

To get the next digit for your pin-code you should total together the first occurrence of a non-consecutive number in the given string until you hit a break.

**A break is one of the following:**

-   Any string which is fully consecutive. E.g. `1234` or `8765`
-   Any string which has 4 of the same digits. E.g. `2222` or `0000`
-   Any string which doesn't have a consecutive sequence at the beginning. E.g. The first two digits are not consecutive.

**Each break has a special rule:**

-   Any string which is fully consecutive: You should `+= 0`.
-   Any string which has 4 of the same digits: You should `+= that digit` E.g. `4444` would be `+= 4`
-   Any string which doesn't have a consecutive sequence at the beginning: You should `+=` the largest digit.

**When you hit a break, the total will be your next digit in the code:**

-   If the total is more than `1` digit long: Add the last digit only. E.g. `258` == `8`

**Considerations:**

-   Breaks are resets.
-   All strings are `4` digits long always. And only contain digits between `0-9`.
-   Digits can never be negative.
-   Consecutive numbers are from left to right only, always starting at the first digit.
-   Consecutive numbers count in both directions: E.g. `1234` and `4321`. But are only considered consecutive when they move in one direction from the beginning; `12..` the next digit to continue considering this string as consecutive must be `3`. Similarly `432.` the next digit can only be `1` to consider this string fully consecutive.
-   Your final code should only be `4` digits long.
-   You should recycle the list until you have a 4 digit code.

Your test cases:

1. `["1233", "1234", "1243"]` -> `"3777"`
2. `["1235", "2346", "3457", "9999", "3333", "5559", "4567"]` -> `"7390"`

**Case 1:**
`1233`: The last `3` is not consecutive: `+= 3`
`1234`: The entire string is consecutive, this is a break: `+= 0` == `3`. Reset.
`1243`: The `4` is not consecutive: `+= 4`
`Recycle the list`
`1233`: The last `3` is not consecutive: `+= 3`
`1234`: The entire string is consecutive, this is a break: `+= 0` == `7`. Reset.
`continue doing this...`

**Case 2:**
`1235`: `+= 5`
`2346`: `+= 6`
`3457`: `+= 7`
`9999`: `+= 9` break. Digit is `7` the last digit of `27`.
`3333`: `+= 3` break. Digit is `3`.
`5559`: `+= 9` break. Digit is `9`. _No consecutive sequence at the beginning._
`4567`: `+= 0` break. Digit is `0`. _Fully consecutive._

Your code should contain a function named: `decipher` which returns a string and takes `one` argument: `codes`; a list of strings.

```py
def decipher(codes: list[str]) -> str:
    ...
```
