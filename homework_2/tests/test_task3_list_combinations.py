from typing import Any, List, Tuple

import pytest
from src.task3_list_combinations import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([[1, 2], [3, 4]], [(1, 3), (1, 4), (2, 3), (2, 4)]),
        ([[], []], []),
        ([[]], []),
        ([[1], [2], [3]], [(1, 2, 3)]),
    ],
)
def test_check_major_and_minor_elem(
    value: List[List[Any]], expected_result: List[Tuple[Any]]
):
    actual_result = combinations(*value)

    assert actual_result == expected_result
