import homework_3.src.task3_filter as hw_filter


def test_of_sample_data():
    expected_result = [
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]
    actual_result = hw_filter.make_filter(name="polly", type="bird").apply(
        hw_filter.sample_data
    )

    assert actual_result == expected_result


def test_of_data_without_key():
    test_data = [
        # Has key (DNA_str)
        {"DNA_str": "ATGC"},
        # Don't have key (DNA_str)
        {"DNA_list": ["A", "T", "G", "C"]},
        {"RNA_str": "AUGC"},
        {"RNA_list": ["A", "U", "G", "C"]},
    ]

    expected_result = [{"DNA_str": "ATGC"}]
    actual_result = hw_filter.make_filter(DNA_str="ATGC").apply(test_data)

    assert expected_result == actual_result
