from itertools import permutations, product


def is_valid_integer(num: float) -> bool:
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())


def countdown(numbers: tuple[int, ...], target: int) -> str:
    numbers = list(map(str, numbers))
    operator_perms = product(["+", "-", "*", "/", "**"], repeat=len(numbers) - 1)
    best_result = float("-inf")

    for num_perm in permutations(numbers):
        for op_perm in operator_perms:
            expr = "".join(
                [num + op for num, op in zip(num_perm, op_perm)] + [num_perm[-1]]
            )

            try:
                result = eval(expr)  # noqa: S307
                if not is_valid_integer(result):
                    continue
                best_result = (
                    int(result)
                    if abs(result - target) < abs(best_result - target)
                    else best_result
                )
                if best_result == target:
                    return best_result
            except ZeroDivisionError:
                continue

    return best_result
