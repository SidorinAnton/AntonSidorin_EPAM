import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def time_with_parallelization():
    numbers = [i for i in range(500)]

    start_time_sec = time.time()

    with Pool(100) as p:
        result = p.map(slow_calculate, numbers)

    end_time_sec = time.time()

    return end_time_sec - start_time_sec
