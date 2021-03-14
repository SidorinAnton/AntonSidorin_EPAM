import pytest
import requests

from homework_4.src.task2_mock_input import count_dots_on_i


def test_of_count_dots_on_i_when_result_is_3(monkeypatch):
    class MockResult3:
        text = "iii"

        def __init__(self, url):
            self.url = url

    monkeypatch.setattr(requests, "get", MockResult3)
    # Now in function "count_dots_on_i" html = requests.MockResult3("https://example.com/").text
    actual_result = count_dots_on_i("https://example.com/")

    assert actual_result == 3


def test_of_count_dots_on_i_with_network_error(monkeypatch):
    def mock_connection_error(url):
        raise ValueError(f"Unreachable {url}")

    monkeypatch.setattr(requests, "get", mock_connection_error)

    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://something_wrong")
