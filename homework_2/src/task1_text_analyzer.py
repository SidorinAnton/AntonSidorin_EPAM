"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from collections import Counter
from typing import List


def read_file_by_char(file_path):
    with open(file_path, encoding="unicode-escape") as data_input:
        for line in data_input:
            for char in line:
                yield char


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as data_input:

        # Initialize a dictionary for calculating word metrics
        quantitative_dict = dict()

        # Repeats_counter is required so that one word does not replace another
        repeats_counter_in_dict_keys = 0

        for line in data_input:
            list_of_words = line.strip().split()

            for word in list_of_words:
                word = word.strip(string.punctuation)

                length_of_word = len(word)
                num_of_unique_symbols = len(set(word))

                key = (
                    length_of_word,
                    num_of_unique_symbols,
                    repeats_counter_in_dict_keys,
                )

                if key not in quantitative_dict:
                    quantitative_dict[key] = word
                else:
                    repeats_counter_in_dict_keys += 1
                    key = (
                        length_of_word,
                        num_of_unique_symbols,
                        repeats_counter_in_dict_keys,
                    )
                    quantitative_dict[key] = word

    # Firstly, get words with largest amount of unique symbols, then - longest words
    sorted_keys = sorted(
        quantitative_dict.keys(), key=lambda x: (x[1], x[0]), reverse=True
    )

    # Get top 10 longest words
    top_ten_words = set()
    for required_key in sorted_keys:
        if len(top_ten_words) < 10:
            top_ten_words.add(quantitative_dict[required_key])
            continue
        else:
            return list(top_ten_words)

    # if number of words less than 10
    return list(top_ten_words)


def get_rarest_char(file_path: str) -> str:
    counter = Counter()
    for char in read_file_by_char(file_path):
        counter[char] += 1

    counter_of_chars = counter.most_common()

    if len(counter_of_chars) > 0:
        return counter_of_chars[-1][0]
    else:
        return "There is an empty file"


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    for char in read_file_by_char(file_path):
        if char in string.punctuation:
            counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """Return number of non-ascii chars (including digits, punctuation and whitespace)"""
    counter = 0
    for char in read_file_by_char(file_path):
        if char not in string.ascii_letters:
            counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Return most common non-ascii char (including digits, punctuation and whitespace)"""

    counter = Counter()

    for char in read_file_by_char(file_path):
        if char not in string.ascii_letters:
            counter[char] += 1

    non_ascii = counter.most_common()

    if len(non_ascii) > 0:
        return non_ascii[0][0]
    else:
        return "No non-ascii char"
