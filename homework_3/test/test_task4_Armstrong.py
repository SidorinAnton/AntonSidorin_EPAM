import pytest

from homework_3.src.task4_Armstrong import *


@pytest.mark.parametrize(["number", "expected_result"], [(i, True) for i in range(10)])
def test_one_digit_numbers_on_armstrong_number(number, expected_result):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result


@pytest.mark.parametrize("number", [i for i in range(-1, -10, -1)])
def test_negative_one_digit_numbers_on_armstrong_number(number):
    with pytest.raises(ValueError, match="Number"):
        is_armstrong(number)


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (153, True),
        (371, True),
        (9474, True),
        (407, True),
        (10, False),
        (100, False),
        (99, False),
        (122, False),
    ],
)
def test_armstrong_numbers(number, expected_result):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (153, True),
        (371, True),
        (9474, True),
        (407, True),
        (10, False),
        (100, False),
        (99, False),
        (122, False),
    ],
)
def test_one_line_armstrong_numbers(number, expected_result):
    actual_result = one_line_is_armstrong(number)

    assert actual_result == expected_result
