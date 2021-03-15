"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    # Check, whether n >= 1
    if n < 1:
        raise ValueError(f"n should be >= 1. Your input is {n}")

    fizzes = ([""] * 2 + ["fizz"]) * ((n // 3) + 1)
    buzzes = ([""] * 4 + ["buzz"]) * ((n // 3) + 1)
    numbers = [str(i) for i in range(1, n + 1)]

    for number in zip(fizzes, buzzes, numbers):
        result = (number[0] + number[1]) or number[2]
        yield result
