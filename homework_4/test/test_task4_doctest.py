"""
Repeat doctest
"""
import pytest

from homework_4.src.task4_doctest import fizzbuzz


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (1, ["1"]),
        (5, ["1", "2", "fizz", "4", "buzz"]),
        (
            15,
            [
                "1",
                "2",
                "fizz",
                "4",
                "buzz",
                "fizz",
                "7",
                "8",
                "fizz",
                "buzz",
                "11",
                "fizz",
                "13",
                "14",
                "fizzbuzz",
            ],
        ),
    ],
)
def test_fizzbuzz_sequence_1_5_and_15(value, expected_result):
    actual_result = fizzbuzz(value)

    assert expected_result == actual_result


def test_fizzbuzz_get_number_less_then_1():
    with pytest.raises(ValueError, match="n should be >= 1. Your input is"):
        fizzbuzz(0)
