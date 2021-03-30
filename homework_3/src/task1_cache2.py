"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'

 f()     # will remember previous value
'1'

f()     # but use it up to two times only
'1'

 f()
? 2
'2'
"""
from typing import Callable


def cache(times: int) -> Callable:
    if not isinstance(times, int):
        raise TypeError(f"{type(times)} cannot be interpreted as an integer")

    def cache_decorator(func: Callable):

        if times == 0:
            return func

        cache_value = dict()  # {params_of_func: [result_of_func, counter_times]}
        counter_times = 0

        def wrap_cache(*args):
            params_of_func = args
            # result_of_func = func(*args)

            nonlocal counter_times
            nonlocal cache_value

            try:
                if cache_value[params_of_func][1] == times:
                    del cache_value[params_of_func]
            except KeyError:
                print("Cache with the given parameters is empty")

            if params_of_func not in cache_value:
                print(f"Initializing the cache with {params_of_func}")
                counter_times = 0
                cache_value[params_of_func] = [func(*args), counter_times]
            else:
                cache_value[params_of_func][1] += 1  # counter_times in cache value

            return cache_value[params_of_func][0]

        return wrap_cache

    return cache_decorator
