import pytest
from src.task4_cache import cache


@pytest.fixture
def test_function():
    def func(a, b):
        return a * b

    return func


def test_of_cache_func(test_function):
    cache_function = cache(test_function)

    first_val = cache_function(1, 2)
    second_val = cache_function(1, 2)

    assert first_val is second_val


def test_of_cache_values(test_function):
    cache_function = cache(test_function)

    cached_val = cache_function(100, 200)
    not_cached_val = test_function(100, 200)

    assert cached_val == not_cached_val
