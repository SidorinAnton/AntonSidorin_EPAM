"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_minimum_and_maximum(file_name: str) -> Tuple[float, float]:
    min_value = float("inf")  # big number
    max_value = -float("inf")  # small number

    with open(file_name, "r") as file_with_numbers:
        for numbers_line in file_with_numbers:
            current_number = float(numbers_line.strip())

            if (
                min_value > current_number
            ):  # Minimum number is greater than it becomes a new minimum
                min_value = current_number

            if (
                max_value < current_number
            ):  # The same with maximum. If current max lesser than new number, change
                max_value = current_number

    return min_value, max_value
