"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    # Analyze first two lists (a and b)
    first_half = []
    for first_elm in a:
        for second_elm in b:
            # Add sum of combinations a and b
            first_half.append(first_elm + second_elm)

    # Analyze second two lists (c and d)
    second_half = []
    for third_elm in c:
        for fourth_elm in d:
            # Add sum of combinations c and d
            second_half.append(third_elm + fourth_elm)

    # Combine these two result (ab and cd)
    counter = 0
    for half_one in first_half:
        for half_two in second_half:
            if (half_one + half_two) == 0:
                counter += 1

    return counter
