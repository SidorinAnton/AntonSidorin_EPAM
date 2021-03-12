import random

import pytest

from homework_2.src.task4_cache import cache


@pytest.fixture
def test_function():
    def func(a, b):
        return a * b

    return func


@pytest.fixture
def test_random_function():
    def random_func(a, b):
        return random.randint(a, b)

    return random_func


@pytest.fixture
def test_nonlocal_variable():
    def func_with_glob_var(a, b):
        global test_var
        test_var += 1
        return a + b

    return func_with_glob_var


def test_if_vaule_is_cached(test_random_function):
    test_random_function = cache(test_random_function)

    first_value = test_random_function(1, 1000)
    second_value = test_random_function(1, 1000)
    third_value = test_random_function(1, 1000)

    assert first_value == second_value == third_value


test_var = 0  # For test_nonlocal_variable function


def test_of_cache_function(test_nonlocal_variable):
    test_nonlocal_variable = cache(test_nonlocal_variable)

    first_value = test_nonlocal_variable(1, 1)
    second_value = test_nonlocal_variable(1, 1)
    third_value = test_nonlocal_variable(1, 1)

    assert test_var == 1


def test_of_cache_func(test_function):
    cache_function = cache(test_function)

    first_val = cache_function(1, 2)
    second_val = cache_function(1, 2)

    assert first_val == second_val


def test_of_cache_values(test_function):
    cache_function = cache(test_function)

    cached_val = cache_function(100, 200)
    not_cached_val = test_function(100, 200)

    assert cached_val == not_cached_val
