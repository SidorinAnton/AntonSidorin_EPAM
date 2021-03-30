"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

import numpy as np


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    # As I understand from example, numbers in our sub-array go sequentially ([3, 6, 7], not [5, 6, 7])

    assert k > 0
    assert k <= len(nums)

    min_sum = -np.inf
    for i in range(k, len(nums) + 1):
        sum_of_sublist = sum(nums[(i - k) : i])

        if sum_of_sublist > min_sum:
            min_sum = sum_of_sublist

    return min_sum
