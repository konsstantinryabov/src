import pytest


# test_masks

@pytest.fixture
def card_review() -> list[str | int]:
    return ["7000792289606361", "73654108430135874305", 7000792289606361, 73654108430135874305]


# test_widget
@pytest.fixture
def card_name_review() -> str:
    return "Maestro"

@pytest.fixture
def card_number_review() -> str:
    return "1596837868705199"

@pytest.fixture
def get_date_review() -> str:
    return "2024-03-11T02:26:18.671407"


# test_processing
@pytest.fixture
def filter_by_state_review() -> list:
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]