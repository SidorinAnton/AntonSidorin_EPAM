from pathlib import Path

import pytest
from max_and_min.find_max_and_min import find_minimum_and_maximum


@pytest.mark.parametrize(
    ["name_of_file", "expected_result"],
    [
        ("data.txt", (-3, 5)),
        ("data_with_repeats.txt", (1, 3)),
        ("data_with_one_value.txt", (10, 10)),
        ("empty_file.txt", (float("inf"), -float("inf"))),
    ],
)
def test_check_min_and_max_finding_func(name_of_file: str, expected_result: tuple):
    actual_result = find_minimum_and_maximum(
        Path("./homework_1/task_3/test/test_data").joinpath(name_of_file)
    )

    assert actual_result == expected_result
