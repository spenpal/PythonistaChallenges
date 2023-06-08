# June Monthly Challenge
## *Executions*

N prisoners are awaiting execution. The executioner lines them up in a circle, and executes every Kth prisoner, starting from the first prisoner (0). He repeats this process until only one prisoner remains, who is then released. See this image for clarity:

![](https://cdn.idevision.net/content/executions.png)

Given the number of prisoners (N) and the interval (K), where should a prisoner stand to avoid being executed?

Your submission should contain a safety function, which takes N, K and returns the safe place to stand.

```python
def safety(N: int, K: int) -> int:
    ...
```

This month has two bonus challenges:
- Do not use while loops or for loops.
- Solve this equation using purely math.

**Test Cases**
```
safety(9, 2) -> 2
safety(9, 3) -> 0
safety(7, 2) -> 6
```