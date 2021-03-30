from types import FunctionType

import homework_5.src.task2_save_original_info as task2


@task2.print_result
def my_function(a):
    """Sum of two elements"""
    return a * 2


def test_my_func_result():
    res = my_function(5)

    assert res == 10


def test_my_func_doc():
    doc = my_function.__doc__

    assert doc == "Sum of two elements"


def test_my_func_name():
    name = my_function.__name__

    assert name == "my_function"


def test_my_func_function():
    func = my_function.__original_func
    assert isinstance(func, FunctionType)


def test_my_func_function_result():
    func = my_function.__original_func
    res = func(2)
    assert res == 4
