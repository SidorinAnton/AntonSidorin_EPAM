"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    if len(data) == 0:
        return False  # However, this is a controversial point

    elif len(data) == 1:
        if data[0] == 0:  # only element of sequence is 0
            return True
        return False

    elif len(data) == 2:
        if data[0] == 0 and data[1] == 1:  # elements are 0 and 1
            return True
        return False

    f_n2 = 0
    f_n1 = 1

    # So F(n-2) + F(n-1) = F(n), n > 1
    # Works with 0, 1, 1, 2, 3, 5 ...
    for element in data[2:]:
        f_n2, f_n1 = f_n1, (f_n1 + f_n2)

        if f_n1 != element:
            return False
    return True
