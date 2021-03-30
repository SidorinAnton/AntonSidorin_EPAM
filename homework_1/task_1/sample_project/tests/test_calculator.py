import pytest
from calculator.calc import check_power_of_2


# Positive values
@pytest.mark.parametrize(
    ["positive_value", "expected_result"],
    [(0, False), (1, True), (12, False), (32, True), (1024, True)],
)
def test_positive_power_of_2(positive_value: int, expected_result: bool):
    actual_result = check_power_of_2(positive_value)

    assert actual_result == expected_result


# Negative values
@pytest.mark.parametrize(
    ["negative_value", "expected_result"], [(i, False) for i in range(-1, -33, -1)]
)
def test_negative_power_of_2(negative_value: int, expected_result: bool):
    actual_result = check_power_of_2(negative_value)

    assert actual_result == expected_result


# Not appropriate type
@pytest.mark.parametrize(
    ["wrong_type"],
    [
        (4.0,),  # float
        ("4",),  # str
        ([4],),  # list
        ((4,),),  # tuple
        ({4},),  # set
        ({4: 4},),  # dict
    ],
)
def test_type_power_of_2(wrong_type):
    with pytest.raises(ValueError):
        check_power_of_2(wrong_type)
