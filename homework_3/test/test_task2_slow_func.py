import homework_3.src.task2_slow_func as slow


def test(*args):
    return 1


def test_parallelization(monkeypatch):
    monkeypatch.setattr(slow, "slow_calculate", test)

    actual_result = slow.time_with_parallelization()
    expected_result = 500

    assert actual_result == expected_result
