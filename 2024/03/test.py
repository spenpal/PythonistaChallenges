import json
from ast import literal_eval
from pathlib import Path

import pytest
from sudoku import sudoku

num_of_test_cases = 0


def load_test_cases() -> list[tuple[str, str]]:
    with Path("test_cases.json").open() as file:
        test_cases = [
            (test_case.get("input"), test_case.get("expected"))
            for test_case in json.load(file)
        ]
        global num_of_test_cases
        num_of_test_cases = len(test_cases)
        return test_cases


@pytest.mark.parametrize(
    ("test_input", "expected"), load_test_cases(), ids=range(1, num_of_test_cases + 1)
)
def test(test_input: str, expected: str) -> None:
    test_input = literal_eval(test_input)
    expected = literal_eval(expected)

    test_output = sudoku(test_input)
    assert test_output == expected
