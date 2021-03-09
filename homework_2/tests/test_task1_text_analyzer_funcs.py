from pathlib import Path
from typing import List

import pytest
from src.task1_text_analyzer import *

# I now, that use star in import is very bad.
# However, I'm sure, that I haven't got any functions with the same names here.

ten_longest_words = [
    "five",
    "Someverylongword",
    "nine",
    "seven",
    "eight",
    "three",
    "six",
    "four",
    "two",
    "One",
]


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("one_longest_word.txt", ["Hi"]),
        ("empty_file.txt", []),
        ("ten_longest_words.txt", ten_longest_words),
    ],
)
def test_check_get_longest_diverse_words(file_name: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(
        Path("./homework_2/tests/test_data_task1").joinpath(file_name)
    )

    actual_result = set(actual_result)
    expected_result = set(expected_result)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("rarest_char.txt", "y"),
        ("empty_file.txt", "There is an empty file"),
    ],
)
def test_check_get_rarest_char(file_name: str, expected_result: str):
    actual_result = get_rarest_char(
        Path("./homework_2/tests/test_data_task1").joinpath(file_name)
    )

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("punctuation.txt", 4),
        ("empty_file.txt", 0),
    ],
)
def test_check_count_punctuation_chars(file_name: str, expected_result: int):
    actual_result = count_punctuation_chars(
        Path("./homework_2/tests/test_data_task1").joinpath(file_name)
    )

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("non_ascii.txt", 3),
        ("punctuation.txt", 0),
        ("empty_file.txt", 0),
    ],
)
def test_check_count_non_ascii_chars(file_name: str, expected_result: int):
    actual_result = count_non_ascii_chars(
        Path("./homework_2/tests/test_data_task1").joinpath(file_name)
    )

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("most_common_non_ascii.txt", "\u00dd"),
        ("punctuation.txt", "No non-ascii char"),
        ("empty_file.txt", "No non-ascii char"),
    ],
)
def test_check_get_most_common_non_ascii_char(file_name: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(
        Path("./homework_2/tests/test_data_task1").joinpath(file_name)
    )

    assert actual_result == expected_result
