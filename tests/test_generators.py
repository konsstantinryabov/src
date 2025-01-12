from typing import Generator
from src.generators import filter_by_currency
from tests.conftest import result_one, result_two


def test_filter_by_currency_fixture(filter_by_currency_review: list) -> None:
    assert next(filter_by_currency(filter_by_currency_review, "USD")) == result_one
    assert next(filter_by_currency(filter_by_currency_review, "RUB")) == result_two


def test_transaction_descriptions_fixture(transaction_descriptions_review: Generator) -> None:
    assert next(transaction_descriptions_review) == "Перевод организации"
    assert next(transaction_descriptions_review) == "Перевод со счета на счет"
    assert next(transaction_descriptions_review) == "Перевод со счета на счет"
    assert next(transaction_descriptions_review) == "Перевод с карты на карту"
    assert next(transaction_descriptions_review) == "Перевод организации"

