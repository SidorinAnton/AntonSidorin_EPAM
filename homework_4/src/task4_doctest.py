"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    This function gets the number N and return the fizzbuzz numbers from 1 to N.
    To run doctest of this function, you should:

     - Write test, starts with >>> func
     - Write result of test in the next line (see below)
     - Open command line (cmd on Windows or terminal on Unix)
     - In terminal run following command:
        python -m doctest -v path_to_your_file.py

    As I'm in the dir AntonSidorin_EPAM, I run command:
        python -m doctest -v ./homework_4/src/task4_doctest.py


    Here are some tests:

    >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    >>> fizzbuzz(0)
    Traceback (most recent call last):
    ...
    ValueError: n should be >= 1. Your input is 0



    :param n: input an integer number N
    :return: N FizzBuzz numbers

    """

    # Check, whether n >= 1
    if n < 1:
        raise ValueError(f"n should be >= 1. Your input is {n}")

    result = list()

    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("fizzbuzz")
        elif number % 3 == 0:
            result.append("fizz")
        elif number % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(number))

    return result
