"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence) -> bool:
    if len(data) == 1:
        if data[0] == 0:  # only element of sequence is 0
            return True
        return False

    elif len(data) == 2:
        if data[0] == 0 and data[1] == 1:  # elements are 0 and 1
            return True
        return False

    # Take third number and check, whether it is equal to the sum of first and second
    for i in range(3, len(data)):
        first, second, third = data[i - 3], data[i - 2], data[i - 1]
        if (first + second) != third:
            return False
    return True
