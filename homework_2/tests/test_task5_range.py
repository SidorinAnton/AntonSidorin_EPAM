import string
from typing import Any, List, Sequence

import pytest
from src.task5_range import custom_range


@pytest.mark.parametrize(
    ["iterable", "stop", "expected_result"],
    [
        ([], 2, []),
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        ("123", "3", ["1", "2"]),
        ([1, 2, 3], 3, [1, 2]),
    ],
)
def test_custom_range_with_one_arg(
    iterable: Sequence, stop: Any, expected_result: List[Any]
):
    actual_result = custom_range(iterable, stop)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable", "start", "stop", "expected_result"],
    [
        ([], 2, 4, []),
        (
            string.ascii_lowercase,
            "g",
            "p",
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ("123", "2", "3", ["2"]),
        ([1, 2, 3], 2, 3, [2]),
        ([1, 2, 3], 3, 2, []),
    ],
)
def test_custom_range_with_two_arg(
    iterable: Sequence, start: Any, stop: Any, expected_result: List[Any]
):
    actual_result = custom_range(iterable, stop, stop)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable", "start", "stop", "step", "expected_result"],
    [
        ([], 2, 5, 2, []),
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
        ("12345", "2", "5", 2, ["2", "4"]),
        ([1, 2, 3, 4, 5], 2, 5, 2, [2, 4]),
        ([1, 2, 3], 3, 2, 2, []),
    ],
)
def test_custom_range_with_two_arg(
    iterable: Sequence, start: Any, stop: Any, step: int, expected_result: List[Any]
):
    actual_result = custom_range(iterable, start, stop, step)
    assert actual_result == expected_result


def test_custom_range_multiple_args():
    with pytest.raises(TypeError):
        custom_range([1, 2, 3], 1, 2, 1, 1, 1)


def test_custom_range_args_not_in_iterable():
    with pytest.raises(ValueError):
        custom_range([1, 2, 3], 100, 200)
