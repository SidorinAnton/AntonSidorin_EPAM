"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

from typing import Any, List, Sequence


def custom_range(iterable: Sequence[Any], *args) -> List[Any]:

    # Check number of arguments
    if len(args) > 3:
        raise TypeError(f"Expected at most 3 arguments, got {len(args)}")

    # Check length of iterable
    if len(iterable) == 0:
        return []

    # Get indexes of args
    if len(args) == 1:
        # The only argument (zero pos) is the stop position
        stop_index = iterable.index(args[0])
        start_index = 0
        step = 1

    elif len(args) == 2:
        # Two values - start (zero pos) and stop (first pos)
        stop_index = iterable.index(args[1])
        start_index = iterable.index(args[0])
        step = 1

    else:  # len(args) == 3:
        # Three values - start (zero pos), stop (first pos) and step (second pos)
        stop_index = iterable.index(args[1])
        start_index = iterable.index(args[0])
        step = args[2]

    result = [i for i in iterable[start_index:stop_index:step]]
    return result
