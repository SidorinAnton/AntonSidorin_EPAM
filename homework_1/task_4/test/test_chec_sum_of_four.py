import pytest
from compute_tuples.compute_tuples import check_sum_of_four


@pytest.mark.parametrize(
    ["value_a", "value_b", "value_c", "value_d", "expected_result"],
    [
        ([1], [1], [-1], [-1], 1),
        ([5, 10], [3, 2], [-3, -10], [-5, 0], 1),
        ([1], [2], [3], [4], 0),
        ([0, 5], [5, 0], [-5, 0], [0, -5], 6),
    ],
)
def test_check_sum_of_four(
    value_a: list, value_b: list, value_c: list, value_d: list, expected_result: tuple
):
    actual_result = check_sum_of_four(value_a, value_b, value_c, value_d)

    assert actual_result == expected_result
