import pytest

from homework_3.src.task4_Armstrong import is_armstrong


@pytest.mark.parametrize(["number", "expected_result"], [(i, True) for i in range(10)])
def test_one_digit_numbers(number, expected_result):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(153, True), (371, True), (9474, True), (407, True)],
)
def test_armstrong_numbers(number, expected_result):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(10, False), (100, False), (99, False), (122, False)],
)
def test_not_armstrong_numbers(number, expected_result):
    actual_result = is_armstrong(number)

    assert actual_result == expected_result
