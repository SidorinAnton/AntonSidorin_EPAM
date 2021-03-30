import pytest
from max_sum_of_subarray.max_sum_of_sub_array import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "window_k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
        ([1, 3, -1, -3, 5, 3, 6, 7], 8, 21),
        ([-1, -1, 2], 2, 1),
        ([0], 1, 0),
    ],
)
def test_check_sum_of_four(nums, window_k, expected_result):
    actual_result = find_maximal_subarray_sum(nums, window_k)

    assert actual_result == expected_result
