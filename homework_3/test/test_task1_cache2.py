import pytest

from homework_3.src.task1_cache2 import cache

glob_counter = 0


@cache(times=2)
def func(a, b):
    global glob_counter
    glob_counter += 1

    return a * b


def test_cache_2():
    assert func(5, 10) == 50
    assert glob_counter == 1

    func(5, 10)
    func(5, 10)

    assert glob_counter == 1

    func(5, 10)

    assert glob_counter == 2
