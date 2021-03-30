import random

import pytest

from homework_3.src.task1_cache2 import cache

glob_counter = 0


@cache(times=2)
def func(a, b):
    global glob_counter
    glob_counter += 1

    return a * b


@cache(times=2)
def random_func(a, b):
    return random.randint(a, b)


def test_of_func_with_glob_var_with_one_set_of_params():
    expected_result = [1, 1, 1, 2]
    actual_result = [0, 0, 0, 0]

    global glob_counter
    glob_counter = 0

    func(1, 2)  # Initializing the cache
    actual_result[0] = glob_counter  # Should be 1

    func(1, 2)  # First time
    actual_result[1] = glob_counter  # Should be 1

    func(1, 2)  # Second time
    actual_result[2] = glob_counter  # Should be 1

    func(1, 2)  # Restart cache
    actual_result[3] = glob_counter  # Should be 1

    assert expected_result == actual_result


def test_of_random_function():
    first_result = random_func(1, 10 ** 6)
    second_result = random_func(1, 10 ** 6)
    third_result = random_func(1, 10 ** 6)

    assert (first_result == second_result) != third_result


def test_of_different_arguments_of_func_using_random_func():
    first_1_100 = random_func(1, 100)  # 1 (for 1-100)
    first_101_200 = random_func(101, 200)  # 1 (for 101-200)

    second_101_200 = random_func(101, 200)  # 2 (for 101-200)
    second_1_100 = random_func(1, 100)  # 2 (for 101-200)

    new_first_1_100 = random_func(1, 100)  # 1

    assert ((first_1_100 == second_1_100) != new_first_1_100) and (
        first_101_200 == second_101_200
    )


def test_of_the_value_of_function():
    result = func(2, 5)

    assert result == 10
