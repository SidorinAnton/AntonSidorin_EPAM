from collections.abc import Sequence

import pytest
from fib_sequence.fib_sequence import check_fibonacci

# black things, that it is better ...
long_fib_data = (
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0], True),
        ([0, 1], True),
        ([1], False),
        ([1, 2], False),
        ([1, 2, 3], True),
        (long_fib_data, True),
        ((0, 1, 1, 2, 3), True),
    ],
)
def test_check_fib_function(value: Sequence, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
