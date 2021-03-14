import pytest

from homework_4.src.task1_read_file import read_magic_number


def test_read_magic_number_on_file_with_needed_int_number(tmp_path):
    path = tmp_path / "correct_int_number.txt"
    path.write_text("1")

    actual_result = read_magic_number(path)

    assert actual_result is True


@pytest.mark.parametrize("value", ["1", "2"])
def test_read_magic_number_on_file_with_needed_int_number(tmp_path, value):
    path = tmp_path / "correct_int_number.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is True


@pytest.mark.parametrize("value", ["1.0", "1.5", "2.0", "2.99"])
def test_read_magic_number_on_file_with_needed_float_number(tmp_path, value):
    path = tmp_path / "correct_float_number.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is True


@pytest.mark.parametrize("value", ["-1", "0", "3", "4", "120"])
def test_read_magic_number_on_file_with_false_int_number(tmp_path, value):
    path = tmp_path / "false_int_number.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is False


@pytest.mark.parametrize("value", ["-1.31", "0.0", "3.0", "4.131", "120.1321"])
def test_read_magic_number_on_file_with_false_float_number(tmp_path, value):
    path = tmp_path / "false_float_number.txt"
    path.write_text(value)

    actual_result = read_magic_number(path)

    assert actual_result is False


def test_read_magic_number_on_file_with_not_existet_path():
    with pytest.raises(ValueError, match="is not exist"):
        path = "/home/user/something.txt"

        read_magic_number(path)


def test_read_magic_number_on_file_with_not_number(tmp_path):
    with pytest.raises(ValueError, match="could not convert string to float"):
        path = tmp_path / "not_number_file.txt"
        path.write_text("some_name")

        read_magic_number(path)


def test_read_magic_number_on_empty_file(tmp_path):
    with pytest.raises(ValueError, match="could not convert string to float"):
        path = tmp_path / "empty_file.txt"
        path.write_text("")
        read_magic_number(path)
