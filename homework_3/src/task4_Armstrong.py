"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:
- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:

    if number < 0:
        raise ValueError("Number should be natural (1, 2, 3, 4...)")

    # Get power of the number of digits
    power = len(str(number))

    # Split number into a digits and get their power
    powered_digits = map(lambda x: int(x) ** power, str(number))

    # Get resulted number
    result = sum(list(powered_digits))

    # If result == number -> True
    return result == number


def one_line_is_armstrong(number: int) -> bool:
    return number == sum(map(lambda x: int(x) ** len(str(number)), str(number)))