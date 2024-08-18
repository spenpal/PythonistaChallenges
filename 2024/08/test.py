import json
import timeit
from ast import literal_eval
from pathlib import Path

from main import advanced_sort, sort


def run_tests(test_cases_file, func, iterations=10_000) -> None:
    with Path(test_cases_file).open() as file:
        test_cases = json.load(file)

    print(f"INPUT: {test_cases_file}")
    for i, test_case in enumerate(test_cases, start=1):
        inputs = literal_eval(test_case["input"])
        expected_output = literal_eval(test_case["expected"])

        total_time = timeit.timeit(lambda: func(*inputs), number=iterations)  # noqa: B023
        avg_time = total_time / iterations

        output = func(*inputs)
        if output == expected_output:
            print(f"TEST CASE #{i}: PASSED ({avg_time:.5f} s)")
        else:
            print(f"TEST CASE #{i}: FAILED ({output} != {expected_output})")


if __name__ == "__main__":
    # TODO: Add function(s) to test
    run_tests("test_cases.json", sort)
    run_tests("advanced_test_cases.json", advanced_sort)