from homework_4.src.task3_print_output import my_precious_logger


def test_print_not_error_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()

    assert captured.out == "OK\n"


def test_print_error_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()

    assert captured.err == ""


def test_print_error_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()

    assert captured.err == "error: file not found\n"


def test_print_not_error_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()

    assert captured.out == ""
