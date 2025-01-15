from typing import Generator
from src.generators import filter_by_currency, card_number_generator
from tests.conftest import result_one, result_two
import pytest

def test_filter_by_currency_fixture(filter_by_currency_review: list) -> None:
    assert next(filter_by_currency(filter_by_currency_review, "USD")) == result_one[0]
    assert next(filter_by_currency(filter_by_currency_review, "RUB")) == result_two[0]


def test_transaction_descriptions_fixture(transaction_descriptions_review: Generator) -> None:
    assert next(transaction_descriptions_review) == "Перевод организации"
    assert next(transaction_descriptions_review) == "Перевод со счета на счет"
    assert next(transaction_descriptions_review) == "Перевод со счета на счет"
    assert next(transaction_descriptions_review) == "Перевод с карты на карту"
    assert next(transaction_descriptions_review) == "Перевод организации"


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, ["0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005"]),
    (1055555, 1055560, ["0000 0000 0105 5555",
                           "0000 0000 0105 5556",
                           "0000 0000 0105 5557",
                           "0000 0000 0105 5558",
                           "0000 0000 0105 5559",
                           "0000 0000 0105 5560"]),
    ("", "", ["Введены некорректные данные"]),
    ({}, {}, ["Введены некорректные данные"]),
    ([], [], ["Введены некорректные данные"]),
])
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    print(start, stop)
    assert list(card_number_generator(start, stop)) == expected