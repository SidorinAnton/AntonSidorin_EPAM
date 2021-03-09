from typing import List, Tuple

import pytest
from src.task2_elements_in_array import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([1, 1, 1, 1], (1, 1)),
        ([1], (1, 1)),
        ([1, 1, 1, 2, 3, 3], (1, 2)),
    ],
)
def test_check_major_and_minor_elem(value: List, expected_result: Tuple):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result


def test_mistake_major_and_minor_elem():
    with pytest.raises(AssertionError):
        major_and_minor_elem([])
