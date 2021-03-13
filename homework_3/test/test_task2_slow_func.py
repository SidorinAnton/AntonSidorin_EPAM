import homework_3.src.task2_slow_func as slow


def test_slow_func():
    assert slow.time_with_parallelization() < 60
