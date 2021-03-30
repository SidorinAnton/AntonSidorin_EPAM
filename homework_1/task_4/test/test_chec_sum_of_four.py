import pytest
from compute_tuples.compute_tuples import check_sum_of_four


@pytest.mark.parametrize(
    ["value_A", "value_B", "value_C", "value_D", "expected_result"],
    [
        ([1], [1], [-1], [-1], 1),
        ([5, 10], [3, 2], [-3, -10], [-5, 0], 1),
        ([1], [2], [3], [4], 0),
        ([0, 5], [5, 0], [-5, 0], [0, -5], 6),
    ],
)
def test_check_sum_of_four(
    value_A: list, value_B: list, value_C: list, value_D: list, expected_result: tuple
):
    actual_result = check_sum_of_four(value_A, value_B, value_C, value_D)

    assert actual_result == expected_result
