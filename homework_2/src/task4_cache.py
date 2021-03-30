"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_value = dict()
    # Structure of this dict will be: cache_value = {tuple_values_of_function: result_of_function}

    def wrap_cache(*args):  # Here we will cache params of our function
        params_of_func = args  # Tuple of params

        if params_of_func not in cache_value:
            # Remember params and result of some function
            cache_value[params_of_func] = func(*params_of_func)

        # Return values from dict (cache_value)
        # If the value is in this dict, we just get it without calculation (running function again)
        return cache_value[params_of_func]

    return wrap_cache
