import time


class CountdownSolver:
    def __init__(self):
        self.solutions = []
        self.target = 0
        self.memo = set()

    def evaluate(self, a: int, b: int, op: str) -> int:
        """Evaluate a simple operation between two numbers"""
        try:
            if op == "+":
                return a + b
            if op == "-" and a > b:
                return a - b
            if op == "*":
                return a * b
            if op == "/" and b != 0 and a % b == 0:
                return a // b
            return None
        except:
            return None

    def format_expression(self, a_expr: str, b_expr: str, op: str) -> str:
        """Format the expression with appropriate parentheses"""
        # Only add parentheses for lower precedence operations inside higher ones
        if op in ["*", "/"]:
            a_needs_parens = any(c in a_expr for c in "+-")
            b_needs_parens = any(c in b_expr for c in "+-")
        else:  # op in ['+', '-']
            a_needs_parens = False
            b_needs_parens = any(c in b_expr for c in "+-")

        a_final = f"({a_expr})" if a_needs_parens else a_expr
        b_final = f"({b_expr})" if b_needs_parens else b_expr

        return f"{a_final} {op} {b_final}"

    def solve_recursive(
        self,
        numbers: list[tuple[int, str]],
        visited: set[tuple[int, ...]],
        deadline: float,
    ) -> None:
        """Recursively find all valid solutions"""
        if time.time() > deadline:
            return

        # Sort numbers for consistent memoization
        key = tuple(sorted(n[0] for n in numbers))
        if key in visited:
            return
        visited.add(key)

        # Check each number against target
        for num, expr in numbers:
            if num > 0:  # Only consider positive numbers
                diff = abs(self.target - num)
                self.solutions.append((diff, len(expr.replace(" ", "")), num, expr))
                if diff == 0:  # If exact match found, return immediately
                    return

        # Try combining pairs of numbers
        n = len(numbers)
        if n < 2:
            return

        for i in range(n):
            for j in range(i + 1, n):
                a_val, a_expr = numbers[i]
                b_val, b_expr = numbers[j]

                remaining = numbers[:i] + numbers[i + 1 : j] + numbers[j + 1 :]

                for op in ["+", "-", "*", "/"]:
                    result = self.evaluate(a_val, b_val, op)
                    if result is not None and 0 < result <= max(self.target * 2, 1000):
                        expr = self.format_expression(a_expr, b_expr, op)
                        self.solve_recursive(
                            remaining + [(result, expr)], visited, deadline
                        )

                    # Try reverse operation for subtraction and division
                    if op in ["-", "/"]:
                        result = self.evaluate(b_val, a_val, op)
                        if result is not None and 0 < result <= max(
                            self.target * 2, 1000
                        ):
                            expr = self.format_expression(b_expr, a_expr, op)
                            self.solve_recursive(
                                remaining + [(result, expr)], visited, deadline
                            )

    def solve(
        self, numbers: tuple[int, ...], target: int, time_limit: float = 1.0
    ) -> str:
        """Solve the Countdown numbers game"""
        self.solutions = []
        self.target = target
        self.memo.clear()

        number_exprs = [(n, str(n)) for n in numbers]
        deadline = time.time() + time_limit

        self.solve_recursive(number_exprs, set(), deadline)

        if not self.solutions:
            return f"No solution found for target {target}"

        # Sort by: 1) distance from target, 2) expression complexity, 3) value
        self.solutions.sort(key=lambda x: (x[0], x[1], x[2]))

        # Return the best solution
        _, _, result, expr = self.solutions[0]
        return f"{expr} = {result}"


def countdown(numbers: tuple[int, ...], target: int) -> str:
    """Wrapper function to maintain the original interface"""
    solver = CountdownSolver()
    return solver.solve(numbers, target)


# Using the wrapper function
result = countdown((10, 5, 9, 1, 6, 3), 20)
print(result)
